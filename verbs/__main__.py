import modes
from util import *
from verb import *


def welcome() -> None:
    print("\nWelcome:")
    print("\t1. Start")
    print("\t2. Settings")
    print("\t3. Create/Edit file")
    print("\t4. Quit\n")


welcome()

while True:
    
    k = input("")
    
    if k.lower() == "start":
        VERBS, func = create_VERBS()
        getattr(modes, func)(VERBS)
        break
    
    if k.lower() == "settings":
        print("")
        settings()
        welcome()
        continue
    
    if k.lower() == "create/edit file" or k.lower() == "create file" or k.lower() == "create file" :
        print("")
        create_edit_file()
        welcome()
        continue
    
    if k.lower() == "quit":
        break
    
    try:
        if int(k) == 1:
            VERBS, func = create_VERBS()
            getattr(modes, func)(VERBS)
            break
        if int(k) == 2:
            print("")
            settings()
            welcome()
            continue
        if int(k) == 3:
            print("")
            create_edit_file()
            welcome()
            continue
        if int(k) == 4:
            break
        if int(k) < 1 or int(k) > 3:
            raise IndexError()
    
    except ValueError:
        pass
    
    except IndexError:
        print(f"Not between 1 and {3}")
        continue
        
    print("Not a choice")