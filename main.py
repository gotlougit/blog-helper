import config, polish
import os, sys

if __name__ == '__main__':
   
    #load arguments
    args = sys.argv[1:]
 
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

    elif args[0] == 'init': #this is just to create the config file
        print('Make sure to have a templates/ folder here before starting!')
        pass

else:
    print('ERROR: not able to find script path! Please directly execute!')
    quit()
