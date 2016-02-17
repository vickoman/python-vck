#!/usr/bin/env python
import sys
import glob, os
import time

#Mackbook MAMP
path = "/Applications/MAMP/htdocs/Pearson3/pearson-books/"
#IMAC VAGRANT
#path = "/Users/vickoman/Enviroments/Vagrant/vickoman-box/public/Pearson3/pearson-books/"
path_two = "/OPS/components/metrodigi/*/index.html"

relative_path = "%s%s/%s%s" % (path, sys.argv[1], sys.argv[2], path_two)
cont=0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0

arrg_ver1 = []
arrg_ver2 = []
arrg_ver3 = []
arrg_ver4 = []

def sublimeText(file):
	command = "%s %s" % ("subl", file)
	return os.system(command)	

def replaceVersions(version, file):
	f =  open(file, 'rw')
	lines = f.read()

	if version == 'v1':
		new_data = lines.replace('responsive.js', 'responsive-v2.js')
	elif version == 'nn':
		new_data = lines.replace('</head>', '<script type="text/javascript" src="../_framework/_base_pearson/responsive-v2.js"></script>\r\n</head>')
	else:
		new_data = lines.replace('', '')	
	f.close()

	nf = open(file, 'w')
	nf.write(new_data)
	nf.close()
	return True

def print_files(arrg):
	for n in arrg:
		print n


for name  in glob.glob(relative_path):
	cont = cont + 1
	#command = "%s %s" % ("subl", name)
	#os.system(command)
	f = open(name, 'r')
	lines = f.read()
	f.close()
	ver3 = lines.find("responsive-v3.js")
	ver2 = lines.find("responsive-v2.js")
	ver1 = lines.find("responsive.js")
	if ver3 != -1:
		cont3 = cont3 + 1
		arrg_ver3.append(name)
		#sublimeText(name)		
	elif ver2 != -1:
		cont2 = cont2 + 1	
		arrg_ver2.append(name)
		#sublimeText(name)		
	elif ver1 != -1:
		cont1 = cont1 + 1	
		arrg_ver1.append(name)	
		#sublimeText(name)	
		#replaceVersions('v1', name)				
	else:
		cont4 = cont4 + 1	
		arrg_ver4.append(name)
		#replaceVersions('nn', name)				


	#time.sleep(10)
print "Total de Archivos Totales: %s" % cont
print "Total de archivo con version 3: %s" % cont3 
print "Total de archivo con version 2: %s" % cont2 
print "Total de archivo con version 1: %s" % cont1 
print "Total de los que no tienen ni mergas: %s" % cont4