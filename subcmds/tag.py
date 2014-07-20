# Copyright (C) 2014 zhuxy@gmail.com
#
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

from color import Coloring
from command import Command
from progress import Progress
from command import InteractiveCommand
from editor import Editor
from error import UploadError, GitError
from project import ReviewableBranch

class Tag(Command):
  common = True
  helpSummary = "Create tag "
  helpUsage = """
    %prog <tagname> [-m <msg>] [-x <cmd>] [-r <remote>] [<project>...]
"""
  helpDescription = """
The '%prog' command is used to create the tag.
"""

  def _Options(self, p):
    p.add_option('-m',
                 dest='tag_commit', metavar='TAG',
                 help='Tag commit.')
    p.add_option('-x', 
                 dest='x_cmd',  metavar='CMD',
                 help='Execute the cmd.')   
    p.add_option('-r', 
                 dest='r_remote',  metavar='REMOTE',
                 help='Choice the remote group project.')                  

  def Execute(self, opt, args):
    
    tagname=''
    if opt.x_cmd:
      if opt.r_remote: 
        remoteaddr=opt.r_remote
        project_list = [] 
        for project in self.GetProjects(args[0:]):
          branch = project.GetBranch(project.CurrentBranch)
          if branch.remote.name == remoteaddr:
            project_list.append(project)
      else:
        project_list = self.GetProjects(args[0:]) 
    else:
      if not args:
        print >>sys.stderr, "error:miss arg"
        print >>sys.stderr, "Usage:repo tag <tagname> [-m <msg>] [-r <remote>] [<project>...]"          
        return
      elif opt.r_remote: 
        remoteaddr=opt.r_remote
        tagname=args[0]
        project_list = [] 
        for project in self.GetProjects(args[1:]):
          branch = project.GetBranch(project.CurrentBranch)
          if branch.remote.name == remoteaddr:
            project_list.append(project)
      else:
        project_list = self.GetProjects(args[1:]) 
        tagname=args[0]
    
    if not project_list:
      print >>sys.stdout, "no project ready for create tag"
      
    err = [] 
    
    print >>sys.stderr, ''
    print >>sys.stderr, '--------------------------------------------'
    for project in project_list:
      print '# # # project  %s  ' % project.name
      
    print >>sys.stderr, ''
    
   
    if opt.x_cmd:
      sys.stdout.write('Execut the cmd git tag %s to projects (y/n)?' % opt.x_cmd)
    else:
      sys.stdout.write('Create the tag %s to projects (y/n)?' % tagname)
      
    answer = sys.stdin.readline().strip()
    answer = answer in ('y', 'Y', 'yes', '1', 'true', 't')
    
    if answer:
      print >>sys.stderr, ''
      print >>sys.stderr, '--------------------------------------------'
    else:
      print >>sys.stderr, 'aborted by user' 
      sys.exit(1)
      
    for project in project_list:
       if not project.tag(opt, args, tagname):
         err.append(project)
       
    if err:
      for p in err:
        print >>sys.stderr,\
          "error: project %s: create tag %s error " \
          % (p.name, tagname)
      sys.exit(1)
    print 'create tag %s done!' % tagname