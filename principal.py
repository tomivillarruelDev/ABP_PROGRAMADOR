
def main():
    print("*" * 48, chr(27) + "[3;4m" + "Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes" + chr(27) + "[1;0m" + "*" * 40)

    opcion = -1
    clientes = []

#-------------------------------------------------------------Ingresar cliente----------------------------------------------------------------

    def Ingresar_clientes(cant_clientes):
    
        for i in range(cant_clientes):
            print(f"\nCargando datos de la empresa #{i + 1}:")

            #Valudación de CUIT
            while True:
                cuit = input("Ingresar CUIT de la empresa: ")
                if cuit.isdigit() and len(cuit) == 11:
                    break
                print("\nDebe ser CUIT y contener 11 digitos.")

            razon_social = input("Ingresar razon social de la empresa: ")

            #Validación de correo
            while True:
                correo = input("Ingresar correo de la empresa: ")
                if '@' in correo and '.' in correo:
                    break
                print("\nIngresó un correo invalido. Intente nuevamente.")
            
           #Se genera la lista para agregar al vector
            empresa = [razon_social, cuit, correo]
        
            #Se agregan los datos a la tupla
            clientes.append(empresa)


#-------------------------------------------------------------Mostrar cliente----------------------------------------------------------------

    def Mostrar_clientes():
        print("_" * 30)
        print("Se ingresaron los siguientes datos:")

        for i in range(len(clientes)):
            print ("\nCliente N°: ", i+1)
            print("Razon social: ", clientes[i][0])
            print("CUIT: ", clientes[i][1])
            print("Correo de contacto: ", clientes[i][2])


#-------------------------------------------------------------Modificar cliente----------------------------------------------------------------
    def Modificar_cliente():
        for i in range(len(clientes)):
            print("\nCliente:", i+1)
            print("\nRazon social: ", clientes[i][0])
            print("CUIT: ", clientes[i][1])
            print("Correo de contacto: ", clientes[i][2])
            print("-" * 30)

        while True:
            try:
                modi = int(input("¿Que cliente desea modificar?: "))
                
                # Ajustar índice a base 0
                modi -=1

                #muestro los datos a modificar
                if 0 <= modi <  len(clientes):
                    print("\nCliente:", modi)
                    print("\nRazon social: ", clientes[modi][0])
                    print("CUIT: ", clientes[modi][1])
                    print("Correo de contacto: ", clientes[modi][2])

                    # Solicitar qué dato modificar
                    solicitud_modificacion = input(
                    "Ingrese qué dato quiere modificar:\n"
                    "1 - Razón social\n"
                    "2 - CUIT\n"
                    "3 - Correo de contacto\n"
                    "4 - Ninguno\n"
                    "Opción: ")

                    if solicitud_modificacion:
                        if not solicitud_modificacion.isdigit() or not (1 <= int(solicitud_modificacion) <= 4):
                            print("Número incorrecto.")
                            continue
                        else:
                            if int(solicitud_modificacion) == 1:
                                nuevo_rs = input("Ingrese la nueva razón social:")
                                clientes[modi][int(solicitud_modificacion)-1] = nuevo_rs

                            if int(solicitud_modificacion) == 2:
                                nuevo_cuit = input("Ingrese el nuevo CUIT: ")
                                clientes[modi][int(solicitud_modificacion)-1] = nuevo_cuit

                            if int(solicitud_modificacion) == 3: 
                                nuevo_correo = input("Ingrese el nuevo correo: ")
                                clientes[modi][int(solicitud_modificacion)-1] = nuevo_correo
                            if int(solicitud_modificacion) == 4:
                                print("\nNo se modificaron datos del cliente n°: ", clientes[i][0])
                                break

                    print("\nCliente modificado exitosamente:")
                    print("\nCliente:", modi+1)
                    print("\nRazon social: ", clientes[modi][0])
                    print("CUIT: ", clientes[modi][1])
                    print("Correo de contacto: ", clientes[modi][2])
                    break
                
                else:
                    print("Número de cliente invalido.")

            except ValueError:
                print("Ingrese un numero valido correspondiente a cliente.")

#-------------------------------------------------------------Eliminar cliente-------------------------------------------------------------
    def Eliminar_cliente():
        #muestro los clientes que tiene disponible
        for i in range(len(clientes)):
            print("\nCliente:", i+1)
            print("\nRazon social: ", clientes[i][0])
            print("CUIT: ", clientes[i][1])
            print("Correo de contacto: ", clientes[i][2])
            print("-" * 30)
        
        while True:
            try:
                eliminar = int(input("¿Que cliente desea eliminar?: "))
                
                # Ajustar índice a base 0 por que la lista se maneja desde el 0
                eliminar -=1

                if 0 <= eliminar <  len(clientes):
                    clientes.remove(clientes[eliminar])
                    print("\nClientes", eliminar, "eliminado exitosamente")

                    #muestro como queda conformada la lista de clientes
                    print("\nAsí queda la lista de clientes:")
                    if not clientes:
                        print("No quedaron datos de clientes")
                    else:
                        for n in range(len(clientes)):
                            print("Cliente:", n+1)
                            print("\nRazon social: ", clientes[n][0])
                            print("CUIT: ", clientes[n][1])
                            print("Correo de contacto: ", clientes[n][2])
                            print("-" * 30)
                        break
                else:
                    print("Número de cliente invalido.")
                break



            except ValueError:
                print("Ingrese un numero valido correspondiente a cliente.")

#--------------------------------------------------------------sub menú de destinos--------------------------------------------------------------
    def mostrar_submenu_destinos():
        print(chr(27) + "[1;31m" + "\nSubmenu de opciones:" + chr(27) + "[1;0m")
        print("=" * 20 + " Gestión de Destinos " + "=" * 20)
        print(chr(27) + "[1;30m" + "1)" + chr(27) + "[1;0m" + "Ver Destinos.")
        print(chr(27) + "[1;30m" + "2)" + chr(27) + "[1;0m" + "Agregar Destinos.")
        print(chr(27) + "[1;30m" + "3)" + chr(27) + "[1;0m" + "Modificar Destinos.")
        print(chr(27) + "[1;30m" + "4)" + chr(27) + "[1;0m" + "Eliminar Destinos.")
        print(chr(27) + "[1;30m" + "5)" + chr(27) + "[1;0m" + "Volver menu principal.")
        print("=" * 43)


#--------------------------------------------------------------sub menú de clientes--------------------------------------------------------------
    def mostrar_submenu_clientes():
        print(chr(27) + "[1;31m" + "\nSubmenu de opciones:" + chr(27) + "[1;0m")
        print("=" * 20 + " Gestión de Clientes " + "=" * 20)
        print(chr(27) + "[1;30m" + "1)" + chr(27) + "[1;0m" + "Ver clientes.")
        print(chr(27) + "[1;30m" + "2)" + chr(27) + "[1;0m" + "Agregar cliente.")
        print(chr(27) + "[1;30m" + "3)" + chr(27) + "[1;0m" + "Modificar clientes.")
        print(chr(27) + "[1;30m" + "4)" + chr(27) + "[1;0m" + "Eliminar cliente.")
        print(chr(27) + "[1;30m" + "5)" + chr(27) + "[1;0m" + "Volver menu principal.")
        print("=" * 43)

#--------------------------------------------------------------------menú------------------------------------------------------------------
    def Mostrar_Menu():
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

#--------------------------------------------------------------------------------------------------------------------------------------
    while opcion != 0:
        Mostrar_Menu()
        try:
            opcion = int(input("Ingrese la opciones del menu que desea realizar: "))
        except ValueError:
            print("Debe ingresar un número")

        if opcion != 0:
            if opcion == 1:
                while True:
                    mostrar_submenu_clientes()
                    sub_opcion = input("Ingrese la opciones del menu que desea realizar: ")

                    if sub_opcion.isdigit() and 1 <= int(sub_opcion) <= 5:
                        sub_opcion = int(sub_opcion)
                
                        if sub_opcion == 1:
                        #hacer una validación de que si está la tupla vacia mostrar msj de que no hay datos y deben registrarse
                        # aca tiene que haber un for que itere en las posiciones 
                            if not clientes:
                                print("\nNo hay datos de clientes")

                            else:
                                Mostrar_clientes()


                        if sub_opcion == 2:
                        #razon social
                        #CUIT
                        #CORREO DE CONTACTO
                        #agregar una función DEF que sea ingresar datos, otra puede ser modificar, y 
                        # otra eliminar, así los if quedan limpios y las funciones lado


                        #agregar validacion de lenght de cuit
                        #validación como es una razon social, alfanumerico , etc
                        #validar en correo el arroba y el .com
                            try:
                                cant_clientes = int(input("Cuantos clientes desea ingresar: "))
                                Ingresar_clientes(cant_clientes)
                            except ValueError:
                                print("Debe ingresar un número valido")

                        if sub_opcion == 3:
                            #hacer una validación de que si está la tupla vacia mostrar msj de que no hay datos y deben registrarse
                            if not clientes:
                                print("\nNo hay clientes registrados.")
                            else:
                               Modificar_cliente()

                        if sub_opcion == 4:
                            #hacer una validación de que si está la tupla vacia mostrar msj de que no hay datos y deben registrarse
                            if not clientes:
                                print("\nNo hay clientes registrados")
                            else:
                                Eliminar_cliente()
                               
                        #sale del submenú
                        if sub_opcion == 5:
                            break

                    else:
                        #acá no se está cumpliendo la condición
                        print("\nIncorrecto. Ingrese una opción del menú.")
        if opcion == 2:
            mostrar_submenu_destinos()


if __name__ == '__main__':
    main()