#!/usr/bin/env python
import sys
import glob, os
import MySQLdb
import json

#Mysql connection
db = MySQLdb.connect(host="localhost", user="root", passwd="MetrodigiJP1234!", db="pearson")
path = "/var/www/pearson/pearson-books/"
# Delete Chapters auto Generates

def getProjectInfo(projectId, field):

    cursor = db.cursor()

    sql = "select p.*, (select id from parts where project_id = p.id ) as part_id from projects p where id = %s" % projectId    
    cursor.execute(sql)
    res = cursor.fetchall()
    row_headers=[x[0] for x in cursor.description]
    json_data=[]
    for result in res:
        json_data.append(dict(zip(row_headers,result)))
    cursor.close()
    if field == 'all':
        return json_data
    else:
        return json_data[0][field]

def getChaptersInfo(partId):

    cursor = db.cursor()

    sql = "select * from chapters where part_id = %s" % partId    
    cursor.execute(sql)
    res = cursor.fetchall()    
    cursor.close()
    return res

def getModuleInfo(chapterId):

    cursor = db.cursor()

    sql = "select * from modules where chapter_id = %s" % chapterId    
    cursor.execute(sql)
    res = cursor.fetchall()    
    cursor.close()
    return res

def updateProjectClone(projectId, newProjectId):
    cursor = db.cursor()

    try:
        projectTitle = getProjectInfo(projectId, 'title')
        short_code = getProjectInfo(projectId, 'short_code')
        sql = "UPDATE projects SET title = '%s PD', short_code= '%s-cm' WHERE id = %s" % (projectTitle, short_code, newProjectId)        
        cursor.execute(sql)
        db.commit()        
        cursor.close()
        return cursor.rowcount
    except:
        db.rollback()
        print """Error actualizando project"""
    

# Copiar proyecto
def copyProject(projectId):
    cursor = db.cursor()
    try:
        query = """INSERT INTO projects (`id`,`title`,`short_code`,`isbn`,`status`,`statement`,`created_date`,`discipline_id`,`client_id`,`private`,`git`,`uname`,`init_chapter_number`,`folder_type`,`disabled`,`jira_key`)(SELECT NULL, 'copy-%s',`short_code`,`isbn`,`status`,`statement`,`created_date`,65,1,`private`,NULL,`uname`,`init_chapter_number`,`folder_type`,`disabled`,NULL  FROM projects WHERE id = %s)""" % (projectId,  projectId)        
        cursor.execute(query)
        db.commit()
        cursor.close()        
        print """Se copio con exito el proyecto"""
        return cursor.lastrowid
    except:
        db.rollback()
        print """No se ejecuto nada del proyecto"""

# INSERT PART
def insertPart(newProjectId):
    cursor = db.cursor()
    try:
        query = """INSERT INTO parts VALUES(NULL, 'Introduction', 1, %s)""" % newProjectId        
        cursor.execute(query)
        db.commit()
        cursor.close()        
        print """Se copio con exito el proyecto"""
        return cursor.lastrowid
    except:
        db.rollback()
        print """No se ejecuto nada del proyecto"""

# Insert Widget
def inserWidget(moduleFrom, moduleTo):
    cursor = db.cursor()
    try:
        query = """INSERT INTO widgets (`id`, `interactive_number`, `interactive_title`, `name`, `caption`, `source`, `order`, `learning_outcomes`, `prompts_to_students`, `time_on_task`, `concept`, `instructions_to_developers`, `special_responsive_request`, `url`, `wireframe_url`, `accessiblity`, `responsive_devices`, `responsive_browsers`, `code`, `created_date`, `widget_type_id`, `module_id`, `inclusion_status_id`, `wireframe_status_id`, `development_status_id`, `design_status_id`, `qa_status_id`, `widget_workflow_id`, `widget_code_id`, `imported`, `height`, `accesibility`, `mobile`)(SELECT NULL, `interactive_number`, `interactive_title`, `name`, `caption`, `source`, `order`, `learning_outcomes`, `prompts_to_students`, `time_on_task`, `concept`, `instructions_to_developers`, `special_responsive_request`, `url`, `wireframe_url`, `accessiblity`, `responsive_devices`, `responsive_browsers`, `code`, `created_date`, `widget_type_id`, %s, `inclusion_status_id`, `wireframe_status_id`, `development_status_id`, `design_status_id`, `qa_status_id`, `widget_workflow_id`, `widget_code_id`, `imported`, `height`, `accesibility`, `mobile` FROM widgets WHERE module_id =  %s);""" % (moduleTo, moduleFrom)
        cursor.execute(query)
        db.commit()
        cursor.close()                
        return True
    except:
        db.rollback()
        print """No se ejecuto nada del proyecto"""

def copyChapters(part_from, part_to):
    cursor = db.cursor()
    try:
        query = """INSERT INTO chapters (`id`, `name`, `order`, `is_numerated`, `number`, `is_sample`, `pdf_url`, `pdf_images`, `state`, `part_id`)(SELECT NULL, name, `order`, is_numerated, number, is_sample, pdf_url, pdf_images, state, '%s'  FROM chapters WHERE part_id = %s)""" % (part_to,  part_from)
        cursor.execute(query)
        db.commit()
        cursor.close()        
        print """Se copiaron los chapters con exito"""
        return True
    except:
        db.rollback()
        print """No se ejecuto nada""" 

def copyModules(chapterFrom, chapterTo):
    cursor = db.cursor()
    try:
        query = """INSERT INTO modules (`id`, `name`, `order`, `chapter_id`)(SELECT NULL, name, `order`, '%s' FROM modules WHERE chapter_id = %s)""" % (chapterTo, chapterFrom)
        cursor.execute(query)
        db.commit()
        cursor.close()        
        return True
    except:
        db.rollback()
        print """No se ejecuto nada modulos""" 

def copyFolderProject(short_code, short_code_new):
    command = "%s %s %s%s %s%s" % ("cp", "-r", path, short_code, path, short_code_new)
    command_rm = "%s %s %s%s/.git" % ("rm", "-rf", path, short_code_new)
    if os.system(command) == 0 and os.system(command_rm) == 0:
        return True
	

projectId = sys.argv[1]


# COPY
newProjectId = copyProject(projectId)

if updateProjectClone(projectId, newProjectId) == 1:
    print "Se actualizo el project con el nombre deseado"
else:
    print "No se actualizo el project"

# CHAPERS
partNew = insertPart(newProjectId)
partOld = getProjectInfo(projectId, 'part_id')
if copyChapters(partOld, partNew):
    print "Se copiaron los chapters con exito"
else:
    print "No se copiaron los chapters"

# MODULOS
# Cambiar por las variables
chaptersFrom = list(getChaptersInfo(partOld))
chaptersTo = list(getChaptersInfo(partNew))



modules_copied = 0
widgets_copied = 0
folder_copied = ""
if len(chaptersFrom) > 0  and len(chaptersTo) > 0:    
    for index in range(len(chaptersFrom)):        
        if chaptersFrom[index][1] == chaptersTo[index][1]:            
            if copyModules(chaptersFrom[index][0], chaptersTo[index][0]):
                modules_copied = modules_copied + 1
                modulesFrom = getModuleInfo(chaptersFrom[index][0])
                modulesTo = getModuleInfo(chaptersTo[index][0])
                for inx in range(len(modulesFrom)):
                    if modulesFrom[inx][1] == modulesTo[inx][1]:
                        if inserWidget(modulesFrom[inx][0], modulesTo[inx][0]):
                            widgets_copied = widgets_copied + 1

short_code = getProjectInfo(projectId, 'short_code')
short_code_new = """%s-cm""" % short_code
if copyFolderProject(short_code, short_code_new):
    folder_copied = "Folder %s was created successfully" % short_code_new

print folder_copied
print """[%s] modules copied and [%s] widgets copied to new project""" % (modules_copied, widgets_copied) 






