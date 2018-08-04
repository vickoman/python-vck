#!/usr/bin/env python
import sys
import glob, os
#Mackbook MAMP
#path = "/Applications/MAMP/htdocs/Pearson3/pearson-books/"
#IMAC VAGRANT
path = "/Users/vickoman/Enviroments/Vagrant/vickoman-box/public/Pearson3/pearson-books/"
path_two = "/OPS/components/metrodigi/ch*-table_drag_and_drop-*/javascript/script.js"
#SERVER PEARSON
# path = "/var/www/Pearson/pearson-books/"
# path_two = "/OPS/components/metrodigi/ch*-table_drag_and_drop-*/javascript/script.js"

flag = False

relative_path = "%s%s/%s%s" % (path, sys.argv[1], sys.argv[2], path_two)

def comment_line(file, text):
	f = open(file, 'rw')
	lines = f.read()
	comment = "%s%s" % ("//", text)
	comment_exist = lines.find(comment)
	
	if comment_exist == -1:
		new_data = lines.replace(text, comment)
		f.close()

		nf = open(file, 'w')
		nf.write(new_data)
		nf.close()
		return True
	return False

def sublimeText(file):
	command = "%s %s" % ("subl", file)
	return os.system(command)

def comment_block(file, block):
	f = open(file, 'rw')
	lines = f.read()
	comment = '''} //else {
            	//_this.options.tablecontainerdraganddrop.getElements(".table-content-cell[data-cid] .column-dragtarget[tabindex]")[0].getParent().getElements(".column-dragtarget")[0].focus();
        		// }'''
	comment_exist =  lines.find(comment)
	if comment_exist == -1:
		new_data = lines.replace(block, comment)
		f.close()

		nf = open(file, 'w')
		nf.write(new_data)
		nf.close()
		return True
	return False


for name in glob.glob(relative_path):
	f = open(name, 'r')
	lines = f.read()
	f.close
	text = "this.resetEl.focus();"
	text_2 = '_this.options.tablecontainerdraganddrop.getElements(".table-content-cell[data-cid] .column-dragtarget[tabindex]")[0].getParent().getElements(".column-dragtarget")[0].focus();'
	block_text = '''} else {
            _this.options.tablecontainerdraganddrop.getElements(".table-content-cell[data-cid] .column-dragtarget[tabindex]")[0].getParent().getElements(".column-dragtarget")[0].focus();
        }'''
	line_1 = lines.find(text)
	line_2 = lines.find(text_2)
	
	if line_1:
		#print "%s: %s" % ("Encontramos la linea", text)
		if comment_line(name, text):
			flag = True
			print "%s %s" % ("Se cambio el archivo", name)			

	if line_2:
		# if comment_line(name, text_2):
		# 	print "%s %s" % ("Se cambio el archivo", name)
		if comment_line(name, text_2):
			flag = True
			print "%s %s" % ("Se cambio el archivo", name)	

	sublimeText(name)

if flag == False:
	print "Nada que hacer aqui!"	

	
