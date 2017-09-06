#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pull latest changes to all Github repos
in a directory.

Pass path to parent directory as arg.

Python 3
"""

import os
import subprocess
import sys

# get abspath of parent directory
repo_parent_dir = os.path.abspath(sys.argv[1])

# get list of directories in repo_parent_dir
repos_list = [f for f in os.listdir(repo_parent_dir) if os.path.isdir(os.path.join(repo_parent_dir, f))]

# git pull each repo
for repo in repos_list:
	git_pull = "cd {} && git pull".format(os.path.join(repo_parent_dir, repo))
	try:
		subprocess.call(git_pull, shell=True)
		print("{} updated successfully!".format(repo))
	except:
		print("Oops! Error with updating {}".format(repo))