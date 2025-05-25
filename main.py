# Sistema de Gestión de Pasajes SkyRoute

#Aca definimos las opciones en los menus con una tupla
menu_principal = ("Gestionar Clientes", "Gestionar Destinos", "Gestionar Ventas", 
                 "Consultar Ventas", "Botón de Arrepentimiento", "Ver Reporte General", 
                 "Acerca del Sistema", "Salir")
submenu_gestion = ("Ver", "Agregar", "Modificar", "Eliminar", "Volver al Menú Principal")
submenu_consulta = ("Ventas del día", "Ventas de la última semana", 
                   "Ventas por cliente", "Volver al Menú Principal")


# Definimos los vectores que vamos a utilizar para almacenar datos, ya que estos son los que se pueden modificar luego
clientes = []
destinos = []
ventas = []


# Ciclo para poder navergar en el menu principal
while True:
    # Mostrar mensaje de bienvenida y menú principal
    print("\nBienvenidos a SkyRoute - Sistema de Gestión de Pasajes")
    print("\nMenú Principal:")
    i = 1 #Definimos un indice que va a recorrer el vector menu_principal
    for opcion in menu_principal:
        print(f"{i}. {opcion}") #la f nos permite usar variables dentro de las comillas nos permite detallar menos
        i += 1
    
    # Captura y validación de la opción del menú principal
    while True: #Utilizar el While true nos permite definir que solo una condicion para salir del bucle, de esta forma ahorramos espacio en codigo
        opcion = input("\nSeleccione una opción (1-8): ")
        if opcion.isdigit() and 1 <= int(opcion) <= 8: #Isdigit es un metodo que analiza si el string es un numero, y el int es para convertir el string a un numero
            opcion = int(opcion)
            break #Si el usuario ingresa un numero valido, se sale del bucle
        print("Entrada no válida, intente nuevamente")
    
    # Procesamiento de la opción seleccionada
    if opcion == 1:  # Gestionar Clientes
        while True:
            print("\n--- Gestionar Clientes ---")
            i = 1
            for subopcion in submenu_gestion:
                print(f"{i}. {subopcion}")
                i += 1
            
            # Captura y validación de la subopción
            while True:
                subopcion = input("\nSeleccione una opción (1-5): ")
                if subopcion.isdigit() and 1 <= int(subopcion) <= 5:
                    subopcion = int(subopcion)
                    break
                print("Entrada no válida, intente nuevamente")
            
            if subopcion == 1:  # Ver
                ver_clientes()
            elif subopcion == 2:  # Agregar
                agregar_cliente()
            elif subopcion == 3:  # Modificar
                modificar_cliente()
            elif subopcion == 4:  # Eliminar
                print("Eliminando cliente...")
            elif subopcion == 5:  # Volver al Menú Principal
                break
            
            input("\nPresione Enter para continuar...")
    
    elif opcion == 2:  # Gestionar Destinos
        while True:
            print("\n--- Gestionar Destinos ---")
            i = 1
            for subopcion in submenu_gestion:
                print(f"{i}. {subopcion}")
                i += 1
            
            # Captura y validación de la subopción
            while True:
                subopcion = input("\nSeleccione una opción (1-5): ")
                if subopcion.isdigit() and 1 <= int(subopcion) <= 5:
                    subopcion = int(subopcion)
                    break
                print("Entrada no válida, intente nuevamente")
            
            if subopcion == 1:  # Ver
                ver_destinos()
            elif subopcion == 2:  # Agregar
                agregar_destino()
            elif subopcion == 3:  # Modificar
                modificar_destino()
            elif subopcion == 4:  # Eliminar
                print("Eliminando destino...")
            elif subopcion == 5:  # Volver al Menú Principal
                break
            
            input("\nPresione Enter para continuar...")
    
    elif opcion == 3:  # Gestionar Ventas
        while True:
            print("\n--- Gestionar Ventas ---")
            i = 1
            for subopcion in submenu_gestion:
                print(f"{i}. {subopcion}")
                i += 1
            
            # Captura y validación de la subopción
            while True:
                subopcion = input("\nSeleccione una opción (1-5): ")
                if subopcion.isdigit() and 1 <= int(subopcion) <= 5:
                    subopcion = int(subopcion)
                    break
                print("Entrada no válida, intente nuevamente")
            
            if subopcion == 1:  # Ver
                ver_ventas()
            elif subopcion == 2:  # Agregar
                agregar_venta()
            elif subopcion == 3:  # Modificar
                modificar_venta()
            elif subopcion == 4:  # Eliminar
                print("Eliminando venta...")
            elif subopcion == 5:  # Volver al Menú Principal
                break
            
            input("\nPresione Enter para continuar...")
    
    elif opcion == 4:  # Consultar Ventas
        while True:
            print("\n--- Consultar Ventas ---")
            i = 1
            for subopcion in submenu_consulta:
                print(f"{i}. {subopcion}")
                i += 1
            
            # Captura y validación de la subopción
            while True:
                subopcion = input("\nSeleccione una opción (1-4): ")
                if subopcion.isdigit() and 1 <= int(subopcion) <= 4:
                    subopcion = int(subopcion)
                    break
                print("Entrada no válida, intente nuevamente")
            
            if subopcion == 1:
                print("Mostrando ventas del día...")
            elif subopcion == 2:
                print("Mostrando ventas de la última semana...")
            elif subopcion == 3:
                print("Mostrando ventas por cliente...")
            elif subopcion == 4:
                break
            
            input("\nPresione Enter para continuar...")
    
    elif opcion == 5:  # Botón de Arrepentimiento
        print("Se ha iniciado proceso de arrepentimiento...")
        input("\nPresione Enter para continuar...")
    
    elif opcion == 6:  # Ver Reporte General
        print("Generando reporte general...")
        input("\nPresione Enter para continuar...")
    
    elif opcion == 7:  # Acerca del Sistema
        print("SkyRoute v1.0 – Prototipo de consola en Python básico")
        input("\nPresione Enter para continuar...")
    
    elif opcion == 8:  # Salir
        print("Gracias por usar SkyRoute. ¡Hasta luego!")
        break


#---------------------------------------- Funciones para Gestionar Clientes ----------------------------------------
def ver_clientes():
    if not clientes:
        print("\nNo hay clientes registrados.")
    else:
        print("\nLista de Clientes:")
        i = 1
        for cliente in clientes:
            print(f"\nCliente {i}:")
            print(f"Razón Social: {cliente['razon_social']}")
            print(f"CUIT: {cliente['cuit']}")
            print(f"Correo: {cliente['correo']}")
            print("-" * 30)
            i += 1
            

def agregar_cliente():
    print("\n--- Agregar Cliente ---")
    # Validación de CUIT
    while True:
        cuit = input("Ingrese CUIT (solo números): ")
        if cuit.isdigit() and len(cuit) == 11:
            # Verificar si el CUIT ya existe
            if any(cliente['cuit'] == cuit for cliente in clientes):
                print("Este CUIT ya está registrado.")
                continue
            break
        print("El CUIT debe contener 11 números")
    
    razon_social = input("Ingrese Razón Social: ")
    
    # Validación de correo
    while True:
        correo = input("Ingrese correo electrónico: ")
        if '@' in correo and '.' in correo:
            break
        print("Ingrese un correo electrónico válido")
    
    # Agregar cliente a la lista
    clientes.append({
        'cuit': cuit,
        'razon_social': razon_social,
        'correo': correo
    })
    
    print(f"\nCliente agregado exitosamente:")
    print(f"CUIT: {cuit}")
    print(f"Razón Social: {razon_social}")
    print(f"Correo: {correo}")

def modificar_cliente():
    if not clientes:
        print("\nNo hay clientes registrados para modificar.")
    else:
        print("\nLista de Clientes:")
        i = 1
        for cliente in clientes:
            print(f"\nCliente {i}:")
            print(f"Razón Social: {cliente['razon_social']}")
            print(f"CUIT: {cliente['cuit']}")
            print(f"Correo: {cliente['correo']}")
            print("-" * 30)
            i += 1

        while True:
            try:
                indice = int(input("\nIngrese el número del cliente a modificar: ")) - 1
                if 0 <= indice < len(clientes):
                    cliente = clientes[indice]
                    print(f"\nModificando cliente {indice + 1}:")
                    print(f"CUIT actual: {cliente['cuit']}")
                    print(f"Razón Social actual: {cliente['razon_social']}")
                    print(f"Correo actual: {cliente['correo']}")
                    
                    # Modificar datos
                    nuevo_cuit = input("\nIngrese nuevo CUIT (Enter para mantener el actual): ")
                    if nuevo_cuit:
                        # Validar que el nuevo CUIT tenga 11 dígitos
                        if not nuevo_cuit.isdigit() or len(nuevo_cuit) != 11:
                            print("El CUIT debe contener 11 números")
                        else:
                            # Verificar si el nuevo CUIT ya existe en otro cliente
                            if any(c['cuit'] == nuevo_cuit for c in clientes if c != cliente):
                                print("Este CUIT ya está registrado para otro cliente")
                            else:
                                cliente['cuit'] = nuevo_cuit
                    
                    nueva_razon_social = input("Ingrese nueva Razón Social (Enter para mantener la actual): ")
                    if nueva_razon_social:
                        cliente['razon_social'] = nueva_razon_social
                    
                    nuevo_correo = input("Ingrese nuevo correo (Enter para mantener el actual): ")
                    if nuevo_correo:
                        if '@' in nuevo_correo and '.' in nuevo_correo:
                            cliente['correo'] = nuevo_correo
                        else:
                            print("Correo no válido, se mantiene el actual")
                    
                    print("\nCliente modificado exitosamente:")
                    print(f"CUIT: {cliente['cuit']}")
                    print(f"Razón Social: {cliente['razon_social']}")
                    print(f"Correo: {cliente['correo']}")
                    break
                else:
                    print("Número de cliente no válido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")



#---------------------------------------- Funciones para Gestionar Destinos ----------------------------------------
def ver_destinos():
    if not destinos:
        print("\nNo hay destinos registrados.")
    else:
        print("\nLista de Destinos:")
        for i, destino in enumerate(destinos, 1):
            print(f"\nDestino {i}:")
            print(f"Código: {destino['codigo']}")
            print(f"Ciudad: {destino['ciudad']}")
            print(f"País: {destino['pais']}")
            print("-" * 30)

def agregar_destino():
    print("\n--- Agregar Destino ---")
    codigo = input("Ingrese código del destino: ")
    # Verificar si el código ya existe
    if any(destino['codigo'] == codigo for destino in destinos):
        print("Este código de destino ya está registrado.")
    else:
        ciudad = input("Ingrese ciudad: ")
        pais = input("Ingrese país: ")
        
        # Agregar destino a la lista
        destinos.append({
            'codigo': codigo,
            'ciudad': ciudad,
            'pais': pais
        })
        
        print(f"\nDestino agregado exitosamente:")
        print(f"Código: {codigo}")
        print(f"Ciudad: {ciudad}")
        print(f"País: {pais}")

def modificar_destino():
    if not destinos:
        print("\nNo hay destinos registrados para modificar.")
    else:
        print("\nLista de Destinos:")
        for i, destino in enumerate(destinos, 1):
            print(f"\nDestino {i}:")
            print(f"Código: {destino['codigo']}")
            print(f"Ciudad: {destino['ciudad']}")
            print(f"País: {destino['pais']}")
            print("-" * 30)
        
        while True:
            try:
                indice = int(input("\nIngrese el número del destino a modificar: ")) - 1
                if 0 <= indice < len(destinos):
                    destino = destinos[indice]
                    print(f"\nModificando destino {indice + 1}:")
                    print(f"Código actual: {destino['codigo']}")
                    print(f"Ciudad actual: {destino['ciudad']}")
                    print(f"País actual: {destino['pais']}")
                    
                    # Modificar datos
                    nueva_ciudad = input("\nIngrese nueva ciudad (Enter para mantener la actual): ")
                    nuevo_pais = input("Ingrese nuevo país (Enter para mantener el actual): ")
                    
                    if nueva_ciudad:
                        destino['ciudad'] = nueva_ciudad
                    if nuevo_pais:
                        destino['pais'] = nuevo_pais
                    
                    print("\nDestino modificado exitosamente:")
                    print(f"Código: {destino['codigo']}")
                    print(f"Ciudad: {destino['ciudad']}")
                    print(f"País: {destino['pais']}")
                    break
                else:
                    print("Número de destino no válido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")



#---------------------------------------- Funciones para Gestionar Ventas ----------------------------------------
def ver_ventas():
    if not ventas:
        print("\nNo hay ventas registradas.")
    else:
        print("\nLista de Ventas:")
        for i, venta in enumerate(ventas, 1):
            print(f"\nVenta {i}:")
            print(f"CUIT Cliente: {venta['cuit_cliente']}")
            print(f"Código Destino: {venta['codigo_destino']}")
            print(f"Monto: ${venta['monto']}")
            print("-" * 30)

def agregar_venta():
    print("\n--- Agregar Venta ---")
    # Validación de CUIT del cliente
    while True:
        cuit_cliente = input("Ingrese CUIT del cliente (solo números): ")
        if cuit_cliente.isdigit() and len(cuit_cliente) == 11:
            # Verificar si el cliente existe
            if not any(cliente['cuit'] == cuit_cliente for cliente in clientes):
                print("Este CUIT no está registrado como cliente.")
                continue
            break
        print("El CUIT debe contener 11 números")
    
    # Validación del código de destino
    while True:
        codigo_destino = input("Ingrese código del destino: ")
        if any(destino['codigo'] == codigo_destino for destino in destinos):
            break
        print("Este código de destino no está registrado.")
    
    # Validación del monto
    while True:
        monto = input("Ingrese monto (solo números): ")
        if monto.isdigit():
            break
        print("El monto debe contener solo números")
    
    # Agregar venta a la lista
    ventas.append({
        'cuit_cliente': cuit_cliente,
        'codigo_destino': codigo_destino,
        'monto': monto
    })
    
    print(f"\nVenta agregada exitosamente:")
    print(f"CUIT Cliente: {cuit_cliente}")
    print(f"Código Destino: {codigo_destino}")
    print(f"Monto: ${monto}")

def modificar_venta():
    if not ventas:
        print("\nNo hay ventas registradas para modificar.")
    else:
        print("\nLista de Ventas:")
        for i, venta in enumerate(ventas, 1):
            print(f"\nVenta {i}:")
            print(f"CUIT Cliente: {venta['cuit_cliente']}")
            print(f"Código Destino: {venta['codigo_destino']}")
            print(f"Monto: ${venta['monto']}")
            print("-" * 30)
        
        while True:
            try:
                indice = int(input("\nIngrese el número de la venta a modificar: ")) - 1
                if 0 <= indice < len(ventas):
                    venta = ventas[indice]
                    print(f"\nModificando venta {indice + 1}:")
                    print(f"CUIT Cliente actual: {venta['cuit_cliente']}")
                    print(f"Código Destino actual: {venta['codigo_destino']}")
                    print(f"Monto actual: ${venta['monto']}")
                    
                    # Modificar monto
                    while True:
                        nuevo_monto = input("\nIngrese nuevo monto (Enter para mantener el actual): ")
                        if not nuevo_monto:
                            break
                        if nuevo_monto.isdigit():
                            venta['monto'] = nuevo_monto
                            break
                        print("El monto debe contener solo números")
                    
                    print("\nVenta modificada exitosamente:")
                    print(f"CUIT Cliente: {venta['cuit_cliente']}")
                    print(f"Código Destino: {venta['codigo_destino']}")
                    print(f"Monto: ${venta['monto']}")
                    break
                else:
                    print("Número de venta no válido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

