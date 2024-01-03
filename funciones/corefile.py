import json
MY_DATABASE = ''

def NewFile(data:dict):
    with open(MY_DATABASE, "w") as wf:
        json.dump(data,wf,indemt = 3)
        wf.close()

def checkFile(archivo:str) -> bool:
    try:
        with open(MY_DATABASE, "r") as f:
            retun True
    except FileNotFoundError as e:
        retun False
    except IOError as e:
        retun False
