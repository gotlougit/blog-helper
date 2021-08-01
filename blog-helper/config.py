#script to manage configuration files

import os, json

#set up variables here instead for easy access
fname = os.getcwd() + os.sep.join(('','web_config.json'))
default_data = { 
    'headfile':'head.html',
    'footfile':'foot.html',
    'entryfile':'entry.html',
    'indexfile':'index.html',
    'indexhead':'indexhead.html',
    'indexfoot':'indexfoot.html',
    'head_end':'<!-- HEAD END -->',
    'foot_start':'<!-- FOOT START -->',
    'title_temp':'this is a title',
    'link_temp':'this-is-a-link',
    'desc_temp':'this is desc',
    'rss_indexfile':'rss.xml',
    'rss_headfile':'rsshead.xml',
    'rss_entryfile':'rssentry.xml',
    'rss_footfile':'rssfoot.xml',
    'rss':0,
    'pagelink':'127.0.0.1',
    'datestamp':0,
    'timestamp':0,
    'updateflag':'<!-- UPDATE -->',
    'entry_add_temp':'Added on: ',
    'entry_update_temp':'Updated on: ',
    'date_temp':'this is date',
    'time_temp':'this is time',
    'date_str':'%A, %d %B, %Y',
    'time_str':'%I:%M %p'
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
