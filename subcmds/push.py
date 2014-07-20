#
# Copyright (C) 2010 JiangXin@ossxp.com
# Copyright (C) 2014 zhuxy@gmail.com

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import copy
import re
import sys

from command import InteractiveCommand
from editor import Editor
from error import UploadError, GitError
from project import ReviewableBranch


def _die(fmt, *args):
  msg = fmt % args
  print >>sys.stderr, 'error: %s' % msg
  sys.exit(1)

class Push(InteractiveCommand):
  common = True
  helpSummary = "Upload changes for no code review"
  helpUsage="""
%prog [-u <branch>] [-d <branch/tag>] [-t <tag>] [-x <cmd>] [-r <remote>] [--tags] {[<project>]... }
"""
  helpDescription = """
The '%prog' command is used to push changes to the git server no gerrit code review.


References
----------

ossxp-com: https://github.com/ossxp-com/repo 
http://blog.sina.com.cn/s/blog_89f592f50100vpau.html 
"""

  def _Options(self, p):
    p.add_option('-r',
                 dest='r_remote', metavar='REMOTE',
                 help='Choice the remote group project.')
    p.add_option('-u',
                 dest='new_branch', metavar='BRANCH',
                 help='Create new feature branch on git server.')
    p.add_option('-d', 
                 dest='del_branch',  metavar='NAME',
                 help='Delete branch or tag on git server.')  
    p.add_option('-t', 
                 dest='push_tag',  metavar='TAG',
                 help='Push tag.')
    p.add_option('--tags', 
                 dest='push_alltags',  action='store_true',
                 help='Push all tags.')
    p.add_option('-x', 
                 dest='x_cmd',  metavar='CMD',
                 help='Execute the cmd.')
                 
  def _SingleBranch(self, opt, args, branch):
    project = branch.project
    name = branch.name
    remote = project.GetBranch(name).remote

    date = branch.date
    list = branch.commits
  
    print 'Upload project %s:' % project.name
    print '  branch %s (%2d commit%s, %s):' % (
                name,
                len(list),
                len(list) != 1 and 's' or '',
                date)
    for commit in list:
      print '         %s' % commit

    sys.stdout.write('Upload project %s (y/n)? ' % project.name)
    answer = sys.stdin.readline().strip()
    answer = answer in ('y', 'Y', 'yes', '1', 'true', 't')

    if answer:
      self._UploadAndReport(opt, args, [branch])
    else:
      _die("upload aborted by user")

  def _MultipleBranches(self, opt, args ,pending):
    projects = {}
    branches = {}

    script = []
    print >>sys.stderr, ''
    print >>sys.stderr, '--------------------------------------------'
    script.append('# Uncomment the branches to upload:')
    for project, avail in pending:
      script.append('#')
      script.append('# project %s/:' % project.relpath)
      print '# # # project  %s  ' % project.name
      b = {}
      for branch in avail:
        name = branch.name
        date = branch.date
        list = branch.commits
        
        if b:
          script.append('#')
        script.append('  branch %s (%2d commit%s, %s):' % (
                      name,
                      len(list),
                      len(list) != 1 and 's' or '',
                      date))
        for commit in list:
          script.append('#         %s' % commit)
        b[name] = branch
        
        print '# # # branch %s (%2d commit%s, %s):' % (
                      name,
                      len(list),
                      len(list) != 1 and 's' or '',
                      date)
        for commit in list:
          print '# # #          %s' % commit
        print ''
      
      projects[project.relpath] = project
      branches[project.name] = b
    script.append('') 
    
  #  script = Editor.EditString("\n".join(script)).split("\n")
    
    print ''
    
    if opt.del_branch: 
      sys.stdout.write('Will delete the remote projects branch/tag %s (y/n)? ' % opt.del_branch )
    elif opt.push_tag:
      sys.stdout.write('Will push the tag %s to remote projects (y/n)? ' % opt.push_tag )
    elif opt.push_alltags:
      sys.stdout.write('Will push all the tags to remote project (y/n)? ')
    elif opt.new_branch:
      sys.stdout.write('Will new the remote projects branch %s (y/n)? ' % opt.new_branch )
    elif opt.x_cmd:
      sys.stdout.write('Will execute the cmd git push %s %s (y/n)? ' % opt.x_cmd )
    else:
      sys.stdout.write('Upload the remote projects (y/n)?')
    
    answer = sys.stdin.readline().strip()
    answer = answer in ('y', 'Y', 'yes', '1', 'true', 't')
      
    if answer:
      print >>sys.stderr, ''
      print >>sys.stderr, '--------------------------------------------'
    else:
      _die("upload aborted by user")
    
    project_re = re.compile(r'^#?\s*project\s*([^\s]+)/:$')
    branch_re = re.compile(r'^\s*branch\s*([^\s(]+)\s*\(.*')

    project = None
    todo = []

    for line in script:
      m = project_re.match(line)
      if m:
        name = m.group(1)
        project = projects.get(name)
        if not project:
          _die('project %s not available for upload', name)
        continue

      m = branch_re.match(line)
      if m:
        name = m.group(1)
        if not project:
          _die('project for branch %s not in script', name)
        branch = branches[project.name].get(name)
        if not branch:
          _die('branch %s not in %s', name, project.relpath)
        todo.append(branch)
    if not todo:
      _die("nothing uncommented for upload")

    self._UploadAndReport(opt, args, todo)

  def _UploadAndReport(self, opt, args, todo):
    have_errors = False
    for branch in todo:
      try:
        # Check if there are local changes that may have been forgotten
        if branch.project.HasChanges():
          sys.stdout.write('Uncommitted changes in ' + branch.project.name + ' (did you forget to amend?). Continue uploading? (y/n) ')
          a = sys.stdin.readline().strip().lower()
          if a not in ('y', 'yes', 't', 'true', 'on'):
            print >>sys.stderr, "skipping upload"
            branch.uploaded = False
            branch.error = 'User aborted'
            continue

        branch.project.UploadNoReview(opt, args, branch=branch.name)
        branch.uploaded = True
      except UploadError, e:
        branch.error = e
        branch.uploaded = False
        have_errors = True
      except GitError, e:
        print >>sys.stderr, "Error: "+ str(e)
        sys.exit(1)


    print >>sys.stderr, ''
    print >>sys.stderr, '--------------------------------------------'

    if have_errors:
      for branch in todo:
        if not branch.uploaded:
          print >>sys.stderr, '[FAILED] %-15s %-15s  (%s)' % (
                 branch.project.relpath + '/', \
                 branch.name, \
                 branch.error)
      print >>sys.stderr, ''

    for branch in todo:
        if branch.uploaded:
          print >>sys.stderr, '[OK    ] %-15s %s' % (
                 branch.project.relpath + '/',
                 branch.name)

    if have_errors:
      sys.exit(1)

  def Execute(self, opt, args):
    
    remoteaddr=None
    
    pending = []
    project_list = [] 
    
    if opt.r_remote:
      remoteaddr = opt.r_remote
      for project in self.GetProjects(args[0:]):
        branch = project.GetBranch(project.CurrentBranch)
        if branch.remote.name == remoteaddr:
          project_list.append(project)
    else:
        project_list = self.GetProjects(args[0:])
        
    # if not create new branch, check whether branch has new commit.
    for project in project_list:
      if (not opt.new_branch and 
          not opt.del_branch and 
          not opt.push_tag and 
          not opt.push_alltags and
          not opt.x_cmd and
          project.GetUploadableBranch(project.CurrentBranch) is None):
        continue
      branch = project.GetBranch(project.CurrentBranch)
      rb = ReviewableBranch(project, branch, branch.LocalMerge)
      pending.append((project, [rb]))

    # run git push
    if not pending:
      print >>sys.stdout, "no branches ready for upload"
    elif len(pending) == 1 and len(pending[0][1]) == 1:
      self._SingleBranch(opt, args, pending[0][1][0])
    else:
      self._MultipleBranches(opt, args, pending)