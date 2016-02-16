#!/usr/bin/env python
import sys
import glob
import os

path = "/Users/vickoman/Enviroments/Vagrant/vickoman-box/public/Pearson3/pearson-books/miller-ca-8e/9999999999/OPS/components/metrodigi/"

for name in os.listdir(path):	
	if not os.path.isfile(name) and not name.startswith('.') and name != '_framework':
		print name
