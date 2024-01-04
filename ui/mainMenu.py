import funciones.clientes as c
import os

opciones = ['Gestor clientes', 'Gestor Proveedores', 'Gestor Productos']
opcionClientes =['Nuevo clientes', 'Borrar Clientes', 'Editar Cliente', 'Buscar','Menu principal']

def generarMainMenu():
    header= """
    ++++++++++++++++++++++++++++++++
    +SISTEMA GESTOR DE INVENTARIOS +
    ++++++++++++++++++++++++++++++++
    """
    print (header)
    for i,item in enumerate(opciones):
        print(f'{(i+1) - (item)}')

def generarClientesMenu():
    c.validarArchivoClientes()
    isActiveCustomer = True
    header= """
    ++++++++++++++++++++++++++++++++
    +  ADMINISTRACION DE CLIENTES  +
    ++++++++++++++++++++++++++++++++
    """
    while (isActiveCustomer):
        os.system('cls')
        print (header)
        for i,item in enumerate(opcionClientes):
            print(f'{(i+1) - (item)}')
            try:
                op = int(input(":)_"))
            except ValueError:
                print("Error en el tipo de dato")
            else:
                if(op == 1):
                    pass
                elif(op == 2):
                    pass
                elif(op == 3):
                    pass
                elif (op == 4):
                    pass
                elif(op == 5):
                    isActiveCustomer=False