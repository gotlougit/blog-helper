import os, config, sys

def readFile(filename):
    with open(filename) as f:
        return f.read()

def addPolish(content):
    head = readFile(head_path)
    foot = readFile(foot_path)

    new_content = head + content + foot
    return new_content

def removePolish(content):
    
    raw_content = content.partition(head_end)[-1].partition(foot_start)[0]
    return raw_content

def polishFile(filename):
    f = readFile(filename)
    newfile_content = addPolish(f)

    with open(filename,'w') as nf:
        nf.write(newfile_content)

def updatePolish(filename):
    old_content = readFile(filename)
    raw_content = removePolish(old_content)
    new_content = addPolish(raw_content)
    
    with open(filename,'w') as nf:
        nf.write(new_content)

def addEntry(heading,rel_filename,desc):
   
    entry = open(entry_path).read()

    new_entry = entry.replace(title_temp,heading)
    new_entry = new_entry.replace(link_temp,rel_filename)
    new_entry = new_entry.replace(desc_temp,desc)

    index_content = readFile(index_path)
    raw_index = removePolish(index_content)
    new_content = addPolish(new_entry + raw_index)

    with open(index_path,'w') as nf:
        nf.write(new_content) 

if __name__ == '__main__':
   
    #load arguments
    args = sys.argv[1:]
 
    #load config and setup variables
    config.fname = os.getcwd() + os.sep.join(('','web_config.json'))
    config.default_data = {
    'headfile':'head.html',
    'footfile':'foot.html',
    'entryfile':'entry.html',
    'indexfile':'index.html',
    'head_end':'<!-- HEAD END -->',
    'foot_start':'<!-- FOOT START -->',
    'title_temp':'this is a title',
    'link_temp':'link',
    'desc_temp':'this is desc' 
}
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

    main_path = os.getcwd()
    head_path = main_path + os.sep.join(('','templates',headfile))
    foot_path = main_path + os.sep.join(('','templates',footfile))
    entry_path = main_path + os.sep.join(('','templates',entryfile))
    index_path = main_path + os.sep.join(('',indexfile))
   
    if args[0] == 'add-polish':
        try:
            polishFile(args[1])
        except IndexError:
            print('ERROR! No filename given!')
    
    elif args[0] == 'add-entry':
        try:  
            title = input('Title: ')
            desc = input('Description: ')  
            addEntry(title,args[1],desc)
        except IndexError:
            print('ERROR! One or more arguments missing!') 

    elif args[0] == 'update-polish':
        try:
            updatePolish(args[1])
        except IndexError:
            print('ERROR! No filename given!')

else:
    print('ERROR: not able to find script path! Please directly execute!')
    quit()
