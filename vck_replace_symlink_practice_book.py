#!/usr/bin/env python
import subprocess
import shlex
import glob
import os
import sys

PATH_PRACTICE = "/var/www/pearson/testing/develop/pearson-books-dev_authoring_release_4_13_2015/practice-books/*/OPS/components/metrodigi/_framework"
SUDOPASSWD = "Mm0925163347"

for name in glob.glob(PATH_PRACTICE):
	if os.readlink(name) == '/data/www/Pearson/testing/develop/portal/api/../_framework':
		print name		

# def ls(hidden=False, relative=True):
#     nodes = []
#     for nm in os.listdir(PATH_PRACTICE):
#         if not hidden and nm.startswith('.'):
#             continue
#         if not relative:
#             nm = os.path.join(PATH_PRACTICE, nm)
#         nodes.append(nm)
#     nodes.sort()
#     return nodes
# print ls()
