import funciones.clientes as c

if __name__ == '__main__':
    if(c.cf.checkFiles(c.MY_DATABASE)):
        print ('ok')
    else:
        print('errrorr')
