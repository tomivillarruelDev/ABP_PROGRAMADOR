
def main():
    print("*" * 48, chr(27) + "[3;4m" + "Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes" + chr(27) + "[1;0m" + "*" * 40)

    opcion = -1
    clientes = []

    def Ingresar_clientes(cant_clientes):
    
        for i in range(cant_clientes):
            print(f"\nCargando datos de la empresa #{i + 1}:")
            razon_social = input("Ingresar razon social de la empresa: ")
            cuit = int(input("Ingresar CUIT de la empresa: "))
            correo = input("Ingresar correo de la empresa: ")

            empresa = [razon_social, cuit, correo]
        

            clientes.append(empresa)

    def Mostrar_clientes():

        for i in range(len(clientes)):
            print("Se ingresaron los siguientes datos:")
            print("\nRazon socia: ", clientes[i][0])
            print("CUIT: ", clientes[i][1])
            print("Correo de contacto: ", clientes[i][2])

        
        opcion = 1

    while opcion != 0:

        print(chr(27) + "[1;31m" + "\nMenu de opciones:" + chr(27) + "[1;0m")
        print("=" * 85)
        print(chr(27) + "[1;30m" + "1)" + chr(27) + "[1;0m" + "Gestionar clientes.")
        print(chr(27) + "[1;30m" + "2)" + chr(27) + "[1;0m" + "Gestionar destinos.")
        print(chr(27) + "[1;30m" + "3)" + chr(27) + "[1;0m" + "Gestionar ventas.")
        print(chr(27) + "[1;30m" + "4)" + chr(27) + "[1;0m" + "Consultar ventas.")
        print(chr(27) + "[1;30m" + "5)" + chr(27) + "[1;0m" + "Boton de arrepentimiento.")
        print(chr(27) + "[1;30m" + "6)" + chr(27) + "[1;0m" + "Ver reporte general.")
        print(chr(27) + "[1;30m" + "7)" + chr(27) + "[1;0m" + "Acerca del sistema")
        print(chr(27) + "[1;30m" + "8)" + chr(27) + "[1;0m" + "Salir")
        print("=" * 85)
        
        opcion = int(input("Ingrese la opciones del menu que desea realizar: "))

        if opcion != 0:
            if opcion == 1:
                print(chr(27) + "[1;31m" + "\nSubmenu de opciones:" + chr(27) + "[1;0m")
                print("=" * 43)
                print(chr(27) + "[1;30m" + "1)" + chr(27) + "[1;0m" + "Ver clientes.")
                print(chr(27) + "[1;30m" + "2)" + chr(27) + "[1;0m" + "Agregar cliente.")
                print(chr(27) + "[1;30m" + "3)" + chr(27) + "[1;0m" + "Modificar clientes.")
                print(chr(27) + "[1;30m" + "4)" + chr(27) + "[1;0m" + "Eliminar cliente.")
                print(chr(27) + "[1;30m" + "0)" + chr(27) + "[1;0m" + "Volver menu principal.")
                print("=" * 43)
                opcion = int(input("Ingrese la opciones del menu que desea realizar: "))

                if opcion == 0:
                    opcion = -1
                
                if opcion == 1:
                    #hacer una validación de que si está la tupla vacia mostrar msj de que no hay datos y deben registrarse
                    # aca tiene que haber un for que itere en las posiciones 
                    if not clientes:
                        print("No hay datos de clientes")
                    else:
                        Mostrar_clientes()


                if opcion == 2:
                    #razon social
                    #CUIT
                    #CORREO DE CONTACTO
                    #agregar una función DEF que sea ingresar datos, otra puede ser modificar, y 
                    # otra eliminar, así los if quedan limpios y las funciones lado


                    #agregar validacion de lenght de cuit
                    #validación como es una razon social, alfanumerico , etc
                    #validar en correo el arroba y el .com

                    cant_clientes = int(input("Cuantos clientes desea ingresar: "))

                    Ingresar_clientes(cant_clientes)

                if opcion == 3:
                    print("sub menú 3")
                    #hacer una validación de que si está la tupla vacia mostrar msj de que no hay datos y deben registrarse

                if opcion == 4:
                    print("sub menú 4")
                    #hacer una validación de que si está la tupla vacia mostrar msj de que no hay datos y deben registrarse

            #if opcion == 2:
                #print("Opciones 2")


               
        



if __name__ == '__main__':
    main()