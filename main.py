import polish
import os, sys

if __name__ == '__main__':
   
    #load arguments
    args = sys.argv[1:]

    #interpret arguments 
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
            if polish.rss_enable:
                polish.addEntry(title,args[1],desc,rss=True)
        except IndexError:
            print('ERROR! One or more arguments missing!') 

    elif args[0] == 'update-polish':
        try:
            polish.updatePolish(args[1])
        except IndexError:
            print('ERROR! No filename given!')

    elif args[0] == 'init':
        print('Make sure to have a templates/ folder here before starting!')
        print('Also make sure to configure web_config.json for your purposes!')
        if polish.rss_enable:
            polish.polishFile(polish.rss_index_path, rss=True)

    elif args[0] == 'add-rss': #just in case someone messes up
        polish.polishFile(polish.rss_index_path, rss=True)

else:
    print('ERROR: not able to find script path! Please directly execute!')
    quit()
