
# File Renamer v0.0.1
# Takes Directory, and Recursively moves through and renames media files to Plex Standards

import os
import re
from pathlib import Path


#########################Functions############################
def RecursiveEdit(dir):
    # get all media files
    if (dir.name == "Movies"):

        g = dir.glob('**/*')
        files = [x for x in g if x.is_file()]
        for f in files:

            print(f)
            # split the file name into words 
            oldname = re.sub('^[\(\[].*?[\)\]]', '', f.stem)
            print(oldname)
            oldname = re.findall(r'\w+', oldname)
            print(oldname)

            # make new name out of tuple element up to year
            yr = [index for index, element in enumerate(oldname) if re.search(r'(20\d{2})|(19\d{2})', element)]
            # redo this part for brackets for the year
            print(oldname)
            newname = str(f.parent) + '\\' + ' '.join(oldname[:yr[0]]) + r' (' + str(oldname[yr[0]]) + r')' + str(f.suffix)
            print(str(f))
            print(newname)
            f.rename(newname)

    elif (dir.name == "TV Shows"):

        g = dir.glob('**/*')
        files = [x for x in g if x.is_file()]
        for f in files:

                chk = re.search(r'Season', str(f.parent), re.IGNORECASE) #check if the parent folder does not contain the word season

                if (bool(chk)):
                    show = str(f.parent.parent.stem) # get the parent parent folder as show name
                else:
                    show = str(f.parent.stem) # get parent folder as show name
                print("Show Name " + show)

                m = re.search(r's(\d+)e((\w+)-(\w+)|(\w+))', f.name, re.IGNORECASE) # this gets the season and episode number in format
                #seperate into season and episode
                try:
                    episode = m.group()
                    episode = re.split('\D', episode, flags=re.IGNORECASE)
                    newfilename = str(f.parent) + '\\' + show + ' ' + 'S' + episode[1] + 'E' + episode[2] + str(f.suffix) # set the new file name
                    print("old file name: " + str(f))
                    print("new file name: " + newfilename)
                    try:
                        f.rename(newfilename)
                    except:
                        continue;
                except:
                    continue;


##################################Main Loop##################################


while True:
    val = input(f'''Please Enter and Option
    (1) Movies
    (2) TV Shows
    (3) Exit
''')
    try:
        opt = int(val)
        if ((opt != 3) & (opt > 0)):
            break;
        else:
            os._exit(1)
    except ValueError:
        print("Not an option!\n")

# Depending on option, parse through directory and rename files
if (opt == 1):
    #dir = Path(input(f'Enter the Root Directory')+"Movies/")       debug line
    dir = Path(str(Path.cwd())+"Movies/")
    if (dir.exists()):
        RecursiveEdit(dir)
    else:
        print("No Movie Directory Exists!")
        input()
        os._exit(1)
elif (opt == 2):    
    #dir = Path(input(f'Enter the Root Directory')+"TV Shows/")     debug line
    dir = Path(str(Path.cwd())+"TV Shows/")
    if (dir.exists()):
        RecursiveEdit(dir)
    else:
        print("No TV Show Directory Exists!")
        input()
        os._exit(1)



    





