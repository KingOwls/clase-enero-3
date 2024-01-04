import os
import funciones.corefile as cf
clientes = {
}
clientes ={
    'Cc': '00',
    'Nombre': '',
    'Apellido': '',
    'Telefono' : [],
    'EmailPersonal': '',
    'EmailCorprotativo': '',
    'Edad': 0,
}

Telefono= {    
    "Descripción":'',
    "Numerico": '000'
}


cf.MY_DATABASE ='data/clientes.json'
def NewCustomer():
    pass

def validarArchivoClientes():
    if(cf.checkFile()):
        print("ok")
        os.system("pause")
    else:
        cf.NewFile(clientes)
