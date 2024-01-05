import json
import os
MY_DATABASE = ''

def NewFile(*param):
    with open(MY_DATABASE, "w") as wf:
        json.dump(param[0],wf,indemt = 4)

def AssData(*param):
    with open(MY_DATABASE, "r+") as rwf:
        data_file=json.load(rwf)
        if(len(param)> 1):
            data_file.update({param[0]: param[1]})
        else:
            data_file.update({param[0]})
        #data_file[llavePrincipal].update((codigo:info))
        rwf.seek(0)
        json.dump(data_file,rwf, indent=4)
        rwf.close()

def Elimiar(*param):
    id=input("ingrese el Nro Nit a Borrar")
    param[id].pop(id)
    print(param)
    os.system('pause')
    

def checkFile(*param):
    if(os.path.isfile(MY_DATABASE)):
        print("Lo encontre")
    else:
        if(len(param)>0):
            NewFile(param[0])