#!/usr/bin/env python
import sys
import glob, os
import MySQLdb

#Mysql connection
db = MySQLdb.connect(host="localhost", user="root", passwd="MetrodigiJP1234!", db="pearson")

# Delete Chapters auto Generates

def deleteChaptersAuto(part_id):
    cursor = db.cursor()    
    try:
        queryDelete = """DELETE from chapters WHERE part_id = %s""" % part_id
        # Uncomment 2 lines below to execute
        # cursor.execute(queryDelete) 
        # db.commit()
        cursor.close()
        print queryDelete
        print """Chapters from part [ %s ] was deleted""" % part_id
    except:
        db.rollback()
        print """No se guardo ni mergas"""

def copyChapters(part_from, part_to):
    cursor = db.cursor()
    try:
        query = """INSERT INTO chapters (`id`, `name`, `order`, `is_numerated`, `number`, `is_sample`, `pdf_url`, `pdf_images`, `state`, `part_id`)(SELECT NULL, name, `order`, is_numerated, number, is_sample, pdf_url, pdf_images, state, '%s'  FROM chapters WHERE part_id = %s)""" % (part_to,  part_from)
        # cursor.execute(query)
        # db.commit()
        # cursor.close()
        print query
        print """Se inserto con exito"""
    except:
        db.rollback()
        print """No se ejecuto nada"""        

part_from = sys.argv[1]
part_to = sys.argv[2]

deleteChapterInitial = raw_input("""Do you want delete chapters from part_id [%ss] ? (yes|no): """ % part_to)

if deleteChapterInitial == "yes":
    print """*****************VCK****************"""
    print """* DELETE CHAPTERS FROM NEW SETUP   *"""
    print """************************************"""
    deleteChaptersAuto(part_to)
    print "\n"
    copyChapters(part_from, part_to)
else:
    print "No hay nada que eliminar"
