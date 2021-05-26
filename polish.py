#module full of relevant functions for polishing webpages
import os
import config

settings = config.loadData()
    
headfile = settings['headfile']
footfile = settings['footfile']
entryfile = settings['entryfile']
indexfile = settings['indexfile']

head_end = settings['head_end']
foot_start = settings['foot_start']
title_temp = settings['title_temp']
link_temp = settings['link_temp']
desc_temp = settings['desc_temp']
pagelink = settings['pagelink']

rss_enable = int(settings['rss'])
rss_headfile = settings['rss_headfile']
rss_footfile = settings['rss_footfile']
rss_entryfile = settings['rss_entryfile']
rss_indexfile = settings['rss_indexfile']

def readFile(filename):
    with open(filename) as f:
        return f.read()

def getTemplatePath(filename):
    return os.getcwd() + os.sep.join(('','templates',filename))

def addPolish(content,rss=False):
    if not rss:
        head = readFile(head_path)
        foot = readFile(foot_path)
    else:
        head = readFile(rss_head_path)
        foot = readFile(rss_foot_path)

    new_content = head + content + foot
    return new_content

def removePolish(content):
    
    raw_content = content.partition(head_end)[-1].partition(foot_start)[0]
    return raw_content

def polishFile(filename,rss=False):
    if not rss:
        f = readFile(filename)
    else:
        f = ''
    newfile_content = addPolish(f,rss=rss)

    with open(filename,'w') as nf: 
        nf.write(newfile_content)

def updatePolish(filename,rss=False):
    old_content = readFile(filename)
    raw_content = removePolish(old_content)
    new_content = addPolish(raw_content,rss=rss)
    
    with open(filename,'w') as nf: 
        nf.write(new_content)

def addEntry(heading,rel_filename,desc,rss=False):
    if not rss: 
        entry = open(entry_path).read()
        ipath = index_path
    elif rss_enable:
        entry = open(rss_entry_path).read()
        ipath = rss_index_path
 
    new_entry = entry.replace(title_temp,heading)
    if rss:
        rel_filename = pagelink + '/' + rel_filename
    new_entry = new_entry.replace(link_temp,rel_filename)
    new_entry = new_entry.replace(desc_temp,desc)

    index_content = readFile(ipath)
    raw_index = removePolish(index_content)
    new_content = addPolish(new_entry + raw_index,rss=rss)
    with open(ipath,'w') as nf:
        nf.write(new_content)

head_path = getTemplatePath(headfile)
foot_path = getTemplatePath(footfile)
entry_path= getTemplatePath(entryfile)
index_path = os.getcwd() + os.sep.join(('',indexfile))

rss_head_path = getTemplatePath(rss_headfile)
rss_foot_path = getTemplatePath(rss_footfile)
rss_entry_path= getTemplatePath(rss_entryfile)
rss_index_path = os.getcwd() + os.sep.join(('',rss_indexfile))
