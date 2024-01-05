import os
import funciones.corefile as cf
clientes = {
}
cf.MY_DATABASE ='data/clientes.json'
def NewCustomer(customer : dict):
    clientes.update(customer)
    cf.AddData(customer['cc'], clientes)

def delCustomer(customers : dict):
    cf.Elimiar(customers)

def validarArchivoClientes():
    if(cf.checkFile()):
        print("ok")
        os.system("pause")
    else:
        cf.NewFile(clientes)