#!/usr/bin/env python
import sys
import glob, os
import time

#Mackbook MAMP
#path = "/Applications/MAMP/htdocs/Pearson3/pearson-books/"
#IMAC VAGRANT
path = "/Users/vickoman/Enviroments/Vagrant/vickoman-box/public/Pearson3/pearson-books/"
#SERVER
#path = "/var/www/pearson/pearson-books/"
path_two = "/OPS/components/metrodigi/*/index.html"

relative_path = "%s%s/%s%s" % (path, sys.argv[1], sys.argv[2], path_two)

cont=0
cont1=0

arrg_files = []

for name  in glob.glob(relative_path):
        f = open(name, 'r')
        lines = f.read()
        f.close()

        namesearch = lines.find(sys.argv[3])

        if namesearch != -1:
                cont1 = cont1 + 1
                arrg_files.append(namesearch)
                print name

print "Total de archivos que contienen %s (%s):" % (sys.argv[3], cont1)
