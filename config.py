#script to manage configuration files

import os, json

#set both variables before using code!
#fname = '' 
#default_data = {} 

#set up variables here instead for easy access
fname = os.getcwd() + os.sep.join(('','web_config.json'))
default_data = { 
    'headfile':'head.html',
    'footfile':'foot.html',
    'entryfile':'entry.html',
    'indexfile':'index.html',
    'head_end':'<!-- HEAD END -->',
    'foot_start':'<!-- FOOT START -->',
    'title_temp':'this is a title',
    'link_temp':'this is a link',
    'desc_temp':'this is a desc',
    'rss_indexfile':'rss.xml',
    'rss_headfile':'rsshead.xml',
    'rss_entryfile':'rssentry.xml',
    'rss_footfile':'rssfoot.xml',
    'rss':0,
    'pagelink':'127.0.0.1'
}

def saveData(data):

    with open(fname,'w') as f:
        json.dump(data, f, indent = 1)

def loadData():
    
    try: 
        with open(fname) as f:
            out = json.load(f)
    except FileNotFoundError:
        saveData(default_data)
        out = default_data
        print('config file not found! creating one with default values..')
    return out
