#!/usr/bin/env python
import os

for root, dirs, files in os.walk(".", topdown=False):
	for name in files:
		if root[7:-3] == "enhanced_image" and name == 'screenshot-image.png':
			os.remove(name)
			print "%s was deleted" % name