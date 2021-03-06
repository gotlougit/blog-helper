import polish
import os, sys

def start():

    #load arguments
    args = sys.argv[1:]
    
    #interpret arguments 
    if args[0] == 'add-polish':
        try:
            polish.polishFile(args[1])
        except IndexError:
            print('ERROR! No filename given!')
    
    elif args[0] == 'remove-polish':
        try:
            content = polish.readFile(args[1])
            print(polish.removePolish(content))
        except IndexError:
            print('ERROR! No filename given!')
    
    elif args[0] == 'add-index':
        try:
            polish.polishFile(args[1],rss=False,findex=True)
        except IndexError:
            print('ERROR! No filename given!')
    
    elif args[0] == 'update-index':
        try:
            polish.updatePolish(args[1],rss=False,findex=True)
        except IndexError:
            print('ERROR! No filename given!')
    
    elif args[0] == 'add-entry':
        try:  
            #title = input('Title: ')
            desc = input('Description: ')  
            polish.addEntry(args[1],desc)
            if polish.rss:
                polish.addEntry(title,args[1],desc,rss=True)
        except IndexError:
            print('ERROR! One or more arguments missing!') 
    
    elif args[0] == 'update-polish':
        try:
            polish.updatePolish(args[1])
        except IndexError:
            print('ERROR! No filename given!')
    
    elif args[0] == 'init':
        try:
            os.chdir('templates/')
        except FileNotFoundError:
            print('WARNING: templates/ folder not found!') 
    
    elif args[0] == 'add-rss': #just in case someone messes up
        polish.polishFile(polish.rss_index_path, rss=True)

if __name__ == "__main__":
    start()
