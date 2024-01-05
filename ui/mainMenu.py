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
    c.cf.checkFile(c.clientes)
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
                    title="""
                    ++++++++++++++++++++++++++++++++
                    +   CREACION DE NUEVO CLIENTE  +
                    ++++++++++++++++++++++++++++++++
                    """
                    print(title)
                    cliente={
                        'cc': "00",
                        'nombre':'',
                        'apellidos':'',
                        'emailpersonal':'',
                        'emailcorporativo':'',
                        'edad':0
                        }
                    for key, item in cliente.items():
                        if(key!= 'edad'):
                            cliente[key]=input(f"Ingrese{key.capitalize()} del cliente: ")
                        else:
                            validateAge= True
                            while(validateAge):
                                try:
                                    cliente["edad"] = int(input(f"Ingrese{key.capitalize()}"))
                                except ValueError:
                                    print ("El valor ingresado es invalido")
                                else:
                                    validateAge= False
                    isAddPhone=True
                    telefono={
                        'telefono':[]                    
                        }
                    phone={
                        "Titulo" :'xx',
                        "valor" : '000'
                    }
                    while(isAddPhone):
                        phone["Titulo"] = input("Ingrese ubicacion (Casa, Oficina, Movil)")
                        phone["valor"] = input(f'Ingrese el Nro {phone["Titulo"]} del ciente {cliente["nombre"]}')
                        telefono["telefono"].append(phone)
                        isAddPhone=bool(input("Para terminar presione Enter.... O cualquier letra para continuar"))
                        cliente.update(telefono)
                        os.system("cls")
                        print (cliente)
                        os.system("pause")
                elif(op == 2):
                    c.delCustomer(c.clientes)
                elif(op == 3):
                    pass
                elif (op == 4):
                    pass
                elif(op == 5):
                    isActiveCustomer=False