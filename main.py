import funciones.clientes as c
import ui.mainMenu as menu
import os

if __name__ == '__main__':
    isActiveApp = True
    opMainMenu = 0
    while(isActiveApp):
        os.system('cls')
        menu.generarMainMenu()
        try:
            opMainMenu =int(input(":)_"))
        except ValueError:
            print("error en el dato ingresado")
        else:
            if(opMainMenu == 1):
                menu.generarClientesMenu()
                
            elif(opMainMenu ==2):
                pass
            elif(opMainMenu ==3):
                pass
            elif(opMainMenu ==4):
                isActiveApp = False
            else:
                print("opcion no esta disponible.....")
                os.pause()