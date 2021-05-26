import config, polish
import os, sys

if __name__ == '__main__':
   
    #load arguments
    args = sys.argv[1:]
 
    #load config and setup variables
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
    rss = int(settings['rss'])

    main_path = os.getcwd()
    head_path = main_path + os.sep.join(('','templates',headfile))
    foot_path = main_path + os.sep.join(('','templates',footfile))
    entry_path = main_path + os.sep.join(('','templates',entryfile))
    index_path = main_path + os.sep.join(('',indexfile))
   
    if args[0] == 'add-polish':
        try:
            polish.polishFile(args[1])
        except IndexError:
            print('ERROR! No filename given!')
    
    elif args[0] == 'add-entry':
        try:  
            title = input('Title: ')
            desc = input('Description: ')  
            polish.addEntry(title,args[1],desc)
        except IndexError:
            print('ERROR! One or more arguments missing!') 

    elif args[0] == 'update-polish':
        try:
            polish.updatePolish(args[1])
        except IndexError:
            print('ERROR! No filename given!')

else:
    print('ERROR: not able to find script path! Please directly execute!')
    quit()
