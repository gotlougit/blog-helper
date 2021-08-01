#module full of relevant functions for polishing webpages
import os
import config
import time

settings = config.loadData()
 
headfile = settings['headfile']
footfile = settings['footfile']
entryfile = settings['entryfile']
indexfile = settings['indexfile']

indexhead = settings['indexhead']
indexfoot = settings['indexfoot']

head_end = settings['head_end']
foot_start = settings['foot_start']
title_temp = settings['title_temp']
link_temp = settings['link_temp']
desc_temp = settings['desc_temp']
pagelink = settings['pagelink']

rss = int(settings['rss'])
rss_headfile = settings['rss_headfile']
rss_footfile = settings['rss_footfile']
rss_entryfile = settings['rss_entryfile']
rss_indexfile = settings['rss_indexfile']

datestamp = int(settings['datestamp'])
timestamp = int(settings['timestamp'])

entry_add_temp = settings['entry_add_temp']
entry_update_temp = settings['entry_update_temp']
update_flag = settings['updateflag']
date_temp = settings['date_temp']
time_temp = settings['time_temp']
date_str = settings['date_str']
time_str = settings['time_str']

def readFile(filename):

    with open(filename) as f:
        return f.read()

def getTemplatePath(filename):

    return os.getcwd() + os.sep.join(('','templates',filename))

def getTitle(content):
    
    lines = content.split('\n')
    for i in lines:
        if "<h1" in i:
            titleWithTag = i
            break
    else:
        return ''
    title = titleWithTag.partition('>')[2].partition('<')[0]
    return title

def addDateTime(content):
    
    if datestamp:
        date_out = time.strftime(date_str,time.localtime())
        content = content.replace(date_temp, date_out)

    if timestamp:
        time_out = time.strftime(time_str,time.localtime()) 
        content = content.replace(time_temp, time_out)
   
    return content
 
def addPolish(content,rss=False,findex=False):

    if rss:
        head = readFile(rss_head_path)
        foot = readFile(rss_foot_path)
    elif findex:
        head = readFile(indexhead_path)
        foot = readFile(indexfoot_path)
    else:
        head = readFile(head_path)
        foot = readFile(foot_path)
    
    content = addDateTime(content)
    title = getTitle(content)
    head = head.replace(title_temp, title)
    head = addDateTime(head)
    new_content = head + content + foot
    return new_content

def removePolish(content):
    
    raw_content = content.partition(head_end)[-1].partition(foot_start)[0]
    return raw_content

def polishFile(filename,rss=False,findex=False):
    
    if not rss:
        f = readFile(filename)
    else:
        f = ''
    newfile_content = addPolish(f,rss=rss,findex=findex)

    with open(filename,'w') as nf: 
        nf.write(newfile_content)

def updatePolish(filename,rss=False,findex=False):
    
    old_content = readFile(filename)
    raw_content = removePolish(old_content)
    new_content = addPolish(raw_content,rss=rss,findex=findex)
    
    with open(filename,'w') as nf: 
        nf.write(new_content)

def addEntry(rel_filename,desc,rss=False):
    
    if not rss: 
        new_entry = readFile(entry_path)
        ipath = index_path
    else:
        new_entry = readFile(rss_entry_path)
        ipath = rss_index_path
        rel_filename = pagelink + '/' + rel_filename
    
    heading = getTitle(removePolish(readFile(rel_filename)))
    new_entry = new_entry.replace(title_temp,heading)
    new_entry = new_entry.replace(link_temp,rel_filename)
    new_entry = new_entry.replace(desc_temp,desc)
    new_entry = addDateTime(new_entry)

    index_content = readFile(ipath)
    raw_index = removePolish(index_content)
    new_content = addPolish(new_entry + raw_index,rss=rss,findex=True)

    with open(ipath,'w') as nf:
        nf.write(new_content)

head_path = getTemplatePath(headfile)
foot_path = getTemplatePath(footfile)
entry_path= getTemplatePath(entryfile)

index_path = os.getcwd() + os.sep.join(('',indexfile))

indexhead_path = getTemplatePath(indexhead)
indexfoot_path = getTemplatePath(indexfoot)

rss_head_path = getTemplatePath(rss_headfile)
rss_foot_path = getTemplatePath(rss_footfile)
rss_entry_path= getTemplatePath(rss_entryfile)
rss_index_path = os.getcwd() + os.sep.join(('',rss_indexfile))
