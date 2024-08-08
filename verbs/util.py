import csv
import json
import os
from verb import Verb


def create_VERBS() -> [list, str]:
    
    SETTINGS = json.loads(open("_code/settings.json", "r").read())
    
    if SETTINGS.get("active").get("file_type") == "csv":
        with open(SETTINGS.get("active").get("path"), newline='') as f:
            reader = csv.reader(f)
            VERBS = [i for e, i in enumerate(reader) if e > 0]
            VERBS = [Verb(i[0].strip(), i[1].strip(), i[2].strip(), i[3].strip(), i[4].strip()) for i in VERBS]
            f.close()
        
    elif SETTINGS.get("active").get("file_type") == "txt":
        with open(SETTINGS.get("active").get("path"), "r") as f:
            VERBS = [i.strip().split(",") for e, i in enumerate(f.readlines()) if e > 0]
            VERBS = [Verb(i[0].strip(), i[1].strip(), i[2].strip(), i[3].strip(), i[4].strip()) for i in VERBS]
            f.close()
    
    else:
        raise Exception("HOW THE FUCK IS THE FILE TYPE WRONG?")
    
    return VERBS, SETTINGS.get("active").get("answer_with")
    

def settings() -> None:
    
    SETTINGS = json.loads(open("_code/settings.json", "r").read())
    
    keys = list(SETTINGS.get("active").keys())
    
    print("Current settings: ")
    for i, key in enumerate(keys):
        print(f"\t{i+1}. {key}: {' ' * (11 - len(key))}{SETTINGS.get('active').get(key)}")
        
    print(f"\nEnter which setting to change (1 - {len(keys)}): ")
    
    while True:
        try:
            choice = int(input(""))
            if not (choice >= 1 and choice <= len(keys)):
                raise IndexError()
            print()
            choice -= 1
            break
        
        except ValueError:
            print("Not a number.")
        
        except IndexError:
            print(f"Not between 1 and {len(keys)}")
    
    print(SETTINGS.get("choice").get(keys[choice]).get("prompt"))
    
    for i, elem in enumerate(SETTINGS.get("choice").get(keys[choice]).get("choices")):
        print(f"\t{i+1}. {elem}")
    
    print()
    
    while True:
        
        if SETTINGS.get("choice").get(keys[choice]).get("input") == "int":
            k = input("")
            
            if k in SETTINGS.get("choice").get(keys[choice]).get("choices"):
                break
            
            try:
                if int(k) >= 1 and int(k) <= len(SETTINGS.get("choice").get(keys[choice]).get("choices")):
                    k = SETTINGS.get("choice").get(keys[choice]).get("choices")[int(k) - 1]
                    break
                else:
                    raise IndexError()
            
            except IndexError:
                print(f"Not between 1 and {len(SETTINGS.get('choice').get(keys[choice]).get('choices'))}")
                continue
            
            except ValueError:
                pass
            
            print("Not a choice")
            continue
        
        if SETTINGS.get("choice").get(keys[choice]).get("input") == "string":
            k = input("")
            
            try: 
                f = open(k, "r")
            except FileNotFoundError:
                print("Path does not exist.")
                continue
            
            break
    
    SETTINGS["active"][keys[choice]] = k

    with open("_code/settings.json", "w") as f:
        f.write(json.dumps(SETTINGS, indent=4))
        f.close()


def create_edit_file() -> None:
    
    print("Enter a path.\nIf it exists, it will edit the file.\nIf it doesn't exist, it will create a file.")
    
    k = input("")
    
    try:
        with open(k, "w") as f:
            f.write(k)
            f.close()
    except FileNotFoundError:
        dirs = k[:k.rfind("/")]
        os.makedirs(dirs)
        with open(k, "w") as f:
            f.write(k)
            f.close()
            

    print("\nEnter the contents of the file.\nOnce all the contents are inputed, press enter twice (aka enter a empty line)\n")
    
    lines = []
    while True:
        l = input("")
        if l:
            lines.append(l)
        else:
            break
    print("\n".join(lines), file=open(k, "w"))