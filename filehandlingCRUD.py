# -----___________F I L E-----H A N D L I N G___________----------)(CRUD OPERATION PROJECT)

from pathlib import Path #STRETCH OUT THE PATH LOCATION OF THE FILE
import os #FOR DELETING THE  FILE

# ----CREATING AND WRITING IN THE FILE---------

def createFile():
    try:
        name=input("enter the name of your file-->> ")
        path=Path(name)
        if not path.exists():
            with open(path,"w") as fc: 
                data=input("enter the data you want to write in the file-->> ")
                fc.write(data)
            print("file created successfully")
        else:
            print("ERROR!! FILE ALREADY OCCURED")
    except Exception as fcer:
        print(f"error occured as {fcer}")

# -------READING FROM THE FILE---------

def readFile():
    try:
        name=input("enter the name of the file-->> ")
        path=Path(name)
        if path.exists():
            with open(path,"r")as fr:
                content=fr.read()
                print(f"your content in the file are \n{content}")
        else:
            print("ERROR! File Not Exist")
    except Exception as frer:
        print(f"error occured as {frer}")

#  ------UPDATING INTO THE FILE------

def updateFile():
    try:
        name=input("enter the name of the file to be renamed-->> ")
        path=Path(name)

        print("Press 1 TO RENAME FILE")
        print("Press 2 TO APPENDING FILE")
        print("Press 3 TO OVERWRITE FILE")

        choice=input("enter your choice from above options-->> ")

        if choice==1:
            new_name=input("enter the file name-->> ")
            new_path=Path(new_name)

            if not new_path.exists:
                path.rename(new_path)
                print("file created succesfully")
            else:
                print(f"file aready exists with the name{new_name}")

        elif choice==2:
            with open(path,"a")as fua:
                data=input("enter the content you want to enter-->> ")
                fua.write("\n"+ data)
            print("successfully appended")

        elif choice==3:
            with open(path,"w")as fuw:
                data=input("enter the content to overwrte ito the file-->> ")
                fuw.write("\n"+data)
            print("data written succesfully")

    except Exception as fuerr:
        print(f"an occured during updating the file as{fuerr}")

# -------DELETING FROM THE FILE--------

def deleteFile():
    try:
        name=input("enter the name of the file-->> ")
        path=Path(name)
        if path.exists():
            path.unlink()
            print("file deleted succesfully")
        else:
            print("no such file exists")

    except Exception as fderr:
        print(f"error occured as {fderr}")

print("enter choices from following choices")
print("Press 1 TO CREATE FILE")
print("Press 2 TO READ FILE")
print("Press 3 TO UPDATE FILE")
print("Press 4 TO DELETE FILE")

choice=int(input("enter your choice-->> "))
if choice==1:
    createFile()

if choice==2:
    readFile()

if choice==3:
    updateFile()

if choice==4:
    deleteFile()

