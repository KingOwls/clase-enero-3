import json
import os
MY_DATABASE = ''

def NewFile(*param):
    with open(MY_DATABASE, "w") as wf:
        json.dump(param[0],wf,indemt = 4)

def checkFile(*param):
    if(os.path.isfile(MY_DATABASE)):
        print("Lo encontre")
    else:
        if(len(param)>0):
            NewFile(param[0])