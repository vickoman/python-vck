#!/usr/bin/env python
import sys
import glob, os
#Mackbook MAMP
#path = "/Applications/MAMP/htdocs/Pearson3/pearson-books/"
#IMAC VAGRANT
path = "/Users/vickoman/Enviroments/Vagrant/vickoman-box/public/Pearson3/pearson-books/"
path_two = "/OPS/components/metrodigi/ch*-advanced_flashcards_v3-*/index.html"
#SERVER PEARSON
# path = "/var/www/Pearson/pearson-books/"
# path_two = "/OPS/components/metrodigi/ch*-table_drag_and_drop-*/javascript/script.js"

flag = False
relative_path = "%s%s/%s%s" % (path, sys.argv[1], sys.argv[2], path_two)

def sublimeText(file):
	command = "%s %s" % ("subl", file)
	return os.system(command)

    
    
for name in glob.glob(relative_path):
    
    f = open(name, 'r')
    lines = f.read()
    
    button = """<button tabindex="0" class="right got-it-v3">Got it!</button>
            <button tabindex="0" class="next right">Next</button>
            <button tabindex="0" class="prev right">Previous</button>"""

    new_order =  """<button tabindex="0" class="prev right">Previous</button>
            <button tabindex="0" class="next right">Next</button>
            <button tabindex="0" class="right got-it-v3">Got it!</button>"""
    
    result = lines.find(button)
    
    if (result):
        new_data = lines.replace(button, new_order)
        f.close()
        nf = open(name, 'w')
        nf.write(new_data)
        nf.close()
        print "%s : %s " % ("Encontramos la linea ", name) 