# Sistema de Gestión de Pasajes SkyRoute

#Aca definimos las opciones en los menus con una tupla
menu_principal = ("Gestionar Clientes", "Gestionar Destinos", "Gestionar Ventas", 
                 "Consultar Ventas", "Botón de Arrepentimiento", "Ver Reporte General", 
                 "Acerca del Sistema", "Salir")
submenu_gestion = ("Ver", "Agregar", "Modificar", "Eliminar", "Volver al Menú Principal")
submenu_consulta = ("Ventas activas del día", "Ventas activas de la última semana", 
                   "Ventas activas por cliente", "Ver ventas anuladas", "Volver al Menú Principal")


# Definimos los vectores que vamos a utilizar para almacenar datos, ya que estos son los que se pueden modificar luego
clientes = []
destinos = []
ventas = []

#---------------------------------------- Funciones para Gestionar Clientes ----------------------------------------
def ver_clientes():
    if not clientes:
        print("\nNo hay clientes registrados.")
    else:
        print("\nLista de Clientes:")
        for i in range(len(clientes)):
            print(f"\nCliente {i + 1}:")
            print(f"Razón Social: {clientes[i]['razon_social']}")
            print(f"CUIT: {clientes[i]['cuit']}")
            print(f"Correo: {clientes[i]['correo']}")
            print("-" * 30)

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
        for i in range(len(clientes)):
            print(f"\nCliente {i + 1}:")
            print(f"Razón Social: {clientes[i]['razon_social']}")
            print(f"CUIT: {clientes[i]['cuit']}")
            print(f"Correo: {clientes[i]['correo']}")
            print("-" * 30)

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
        for i in range(len(destinos)):
            print(f"\nDestino {i + 1}:")
            print(f"Ciudad: {destinos[i]['ciudad']}")
            print(f"País: {destinos[i]['pais']}")
            print(f"Costo Base: ${destinos[i]['costo_base']}")
            print("-" * 30)

def agregar_destino():
    print("\n--- Agregar Destino ---")
    ciudad = input("Ingrese ciudad: ")
    pais = input("Ingrese país: ")
    
    # Verificar si el destino ya existe
    if any(destino['ciudad'] == ciudad and destino['pais'] == pais for destino in destinos):
        print("Este destino ya está registrado.")
    else:
        # Validación del costo base
        while True:
            try:
                costo_base = float(input("Ingrese costo base del viaje: $"))
                if costo_base > 0:
                    break
                print("El costo base debe ser mayor a 0")
            except ValueError:
                print("Por favor, ingrese un número válido")
        
        # Agregar destino a la lista
        destinos.append({
            'ciudad': ciudad,
            'pais': pais,
            'costo_base': costo_base
        })
        
        print(f"\nDestino agregado exitosamente:")
        print(f"Ciudad: {ciudad}")
        print(f"País: {pais}")
        print(f"Costo Base: ${costo_base}")

def modificar_destino():
    if not destinos:
        print("\nNo hay destinos registrados para modificar.")
    else:
        print("\nLista de Destinos:")
        for i in range(len(destinos)):
            print(f"\nDestino {i + 1}:")
            print(f"Ciudad: {destinos[i]['ciudad']}")
            print(f"País: {destinos[i]['pais']}")
            print(f"Costo Base: ${destinos[i]['costo_base']}")
            print("-" * 30)
        
        while True:
            try:
                indice = int(input("\nIngrese el número del destino a modificar: ")) - 1
                if 0 <= indice < len(destinos):
                    destino = destinos[indice]
                    print(f"\nModificando destino {indice + 1}:")
                    print(f"Ciudad actual: {destino['ciudad']}")
                    print(f"País actual: {destino['pais']}")
                    print(f"Costo Base actual: ${destino['costo_base']}")
                    
                    # Modificar datos
                    nueva_ciudad = input("\nIngrese nueva ciudad (Enter para mantener la actual): ")
                    nuevo_pais = input("Ingrese nuevo país (Enter para mantener el actual): ")
                    
                    # Verificar si el nuevo destino ya existe
                    if nueva_ciudad and nuevo_pais:
                        if any(d['ciudad'] == nueva_ciudad and d['pais'] == nuevo_pais and d != destino for d in destinos):
                            print("Este destino ya está registrado.")
                            continue
                    
                    # Modificar costo base
                    while True:
                        nuevo_costo = input("Ingrese nuevo costo base (Enter para mantener el actual): $")
                        if not nuevo_costo:
                            break
                        try:
                            nuevo_costo = float(nuevo_costo)
                            if nuevo_costo > 0:
                                destino['costo_base'] = nuevo_costo
                                break
                            print("El costo base debe ser mayor a 0")
                        except ValueError:
                            print("Por favor, ingrese un número válido")
                    
                    if nueva_ciudad:
                        destino['ciudad'] = nueva_ciudad
                    if nuevo_pais:
                        destino['pais'] = nuevo_pais
                    
                    print("\nDestino modificado exitosamente:")
                    print(f"Ciudad: {destino['ciudad']}")
                    print(f"País: {destino['pais']}")
                    print(f"Costo Base: ${destino['costo_base']}")
                    break
                else:
                    print("Número de destino no válido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

def eliminar_destino():
    if not destinos:
        print("\nNo hay destinos registrados para eliminar.")
    else:
        print("\nLista de Destinos:")
        for i in range(len(destinos)):
            print(f"\nDestino {i + 1}:")
            print(f"Ciudad: {destinos[i]['ciudad']}")
            print(f"País: {destinos[i]['pais']}")
            print(f"Costo Base: ${destinos[i]['costo_base']}")
            print("-" * 30)
        
        while True:
            try:
                indice = int(input("\nIngrese el número del destino a eliminar: ")) - 1
                if 0 <= indice < len(destinos):
                    destino = destinos[indice]
                    print(f"\n¿Está seguro que desea eliminar el siguiente destino?")
                    print(f"Ciudad: {destino['ciudad']}")
                    print(f"País: {destino['pais']}")
                    print(f"Costo Base: ${destino['costo_base']}")
                    
                    confirmacion = input("\nIngrese 'SI' para confirmar la eliminación: ")
                    if confirmacion.upper() == 'SI':
                        destinos.pop(indice)
                        print("\nDestino eliminado exitosamente.")
                    else:
                        print("\nOperación cancelada.")
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
        for i in range(len(ventas)):
            # Buscar datos del cliente
            cliente = next((c for c in clientes if c['cuit'] == ventas[i]['cuit_cliente']), None)
            
            print(f"\nVenta {i + 1}:")
            print("\nDatos del Cliente:")
            print(f"CUIT: {ventas[i]['cuit_cliente']}")
            print(f"Razón Social: {cliente['razon_social'] if cliente else 'Cliente no encontrado'}")
            print(f"Correo: {cliente['correo'] if cliente else 'Cliente no encontrado'}")
            
            print("\nDatos del Pasaje:")
            print(f"Ciudad: {ventas[i]['ciudad']}")
            print(f"País: {ventas[i]['pais']}")
            print(f"Fecha: {ventas[i]['fecha']}")
            print(f"Monto: ${ventas[i]['monto']}")
            print(f"Estado: {ventas[i]['estado']}")
            print("-" * 50)

def agregar_venta():
    print("\n--- Agregar Venta ---")
    # Validación de CUIT del cliente
    while True:
        cuit_cliente = input("Ingrese CUIT del cliente (solo números): ")
        if cuit_cliente.isdigit() and len(cuit_cliente) == 11:
            # Verificar si el cliente existe
            cliente = next((c for c in clientes if c['cuit'] == cuit_cliente), None)
            if not cliente:
                print("Este CUIT no está registrado como cliente.")
                continue
            break
        print("El CUIT debe contener 11 números")
    
    # Mostrar destinos disponibles
    if not destinos:
        print("\nNo hay destinos registrados. Debe registrar destinos antes de realizar una venta.")
        return
    
    print("\nDestinos disponibles:")
    for i in range(len(destinos)):
        print(f"\nDestino {i + 1}:")
        print(f"Ciudad: {destinos[i]['ciudad']}")
        print(f"País: {destinos[i]['pais']}")
        print(f"Costo Base: ${destinos[i]['costo_base']}")
        print("-" * 30)
    
    # Selección de destino
    while True:
        try:
            indice_destino = int(input("\nIngrese el número del destino: ")) - 1
            if 0 <= indice_destino < len(destinos):
                destino = destinos[indice_destino]
                break
            print("Número de destino no válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    # Obtener fecha actual
    from datetime import datetime
    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    # Agregar venta a la lista
    ventas.append({
        'cuit_cliente': cuit_cliente,
        'ciudad': destino['ciudad'],
        'pais': destino['pais'],
        'fecha': fecha_actual,
        'estado': 'Activa',
        'monto': destino['costo_base']
    })
    
    print(f"\nVenta agregada exitosamente:")
    print("\nDatos del Cliente:")
    print(f"CUIT: {cuit_cliente}")
    print(f"Razón Social: {cliente['razon_social']}")
    print(f"Correo: {cliente['correo']}")
    
    print("\nDatos del Pasaje:")
    print(f"Ciudad: {destino['ciudad']}")
    print(f"País: {destino['pais']}")
    print(f"Fecha: {fecha_actual}")
    print(f"Monto: ${destino['costo_base']}")
    print(f"Estado: Activa")

def modificar_venta():
    if not ventas:
        print("\nNo hay ventas registradas para modificar.")
    else:
        print("\nLista de Ventas:")
        for i in range(len(ventas)):
            # Buscar datos del cliente
            cliente = next((c for c in clientes if c['cuit'] == ventas[i]['cuit_cliente']), None)
            
            print(f"\nVenta {i + 1}:")
            print("\nDatos del Cliente:")
            print(f"CUIT: {ventas[i]['cuit_cliente']}")
            print(f"Razón Social: {cliente['razon_social'] if cliente else 'Cliente no encontrado'}")
            print(f"Correo: {cliente['correo'] if cliente else 'Cliente no encontrado'}")
            
            print("\nDatos del Pasaje:")
            print(f"Ciudad: {ventas[i]['ciudad']}")
            print(f"País: {ventas[i]['pais']}")
            print(f"Fecha: {ventas[i]['fecha']}")
            print(f"Monto: ${ventas[i]['monto']}")
            print(f"Estado: {ventas[i]['estado']}")
            print("-" * 50)
        
        while True:
            try:
                indice = int(input("\nIngrese el número de la venta a modificar: ")) - 1
                if 0 <= indice < len(ventas):
                    venta = ventas[indice]
                    # Buscar datos del cliente
                    cliente = next((c for c in clientes if c['cuit'] == venta['cuit_cliente']), None)
                    
                    print(f"\nModificando venta {indice + 1}:")
                    print("\nDatos del Cliente:")
                    print(f"CUIT: {venta['cuit_cliente']}")
                    print(f"Razón Social: {cliente['razon_social'] if cliente else 'Cliente no encontrado'}")
                    print(f"Correo: {cliente['correo'] if cliente else 'Cliente no encontrado'}")
                    
                    print("\nDatos del Pasaje:")
                    print(f"Ciudad: {venta['ciudad']}")
                    print(f"País: {venta['pais']}")
                    print(f"Fecha: {venta['fecha']}")
                    print(f"Monto: ${venta['monto']}")
                    print(f"Estado: {venta['estado']}")
                    
                    print("\nNo se puede modificar el estado de la venta desde aquí.")
                    print("Use el Botón de Arrepentimiento para anular una venta.")
                    break
                else:
                    print("Número de venta no válido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

def eliminar_venta():
    if not ventas:
        print("\nNo hay ventas registradas para eliminar.")
    else:
        print("\nLista de Ventas:")
        for i in range(len(ventas)):
            # Buscar datos del cliente
            cliente = next((c for c in clientes if c['cuit'] == ventas[i]['cuit_cliente']), None)
            
            print(f"\nVenta {i + 1}:")
            print("\nDatos del Cliente:")
            print(f"CUIT: {ventas[i]['cuit_cliente']}")
            print(f"Razón Social: {cliente['razon_social'] if cliente else 'Cliente no encontrado'}")
            print(f"Correo: {cliente['correo'] if cliente else 'Cliente no encontrado'}")
            
            print("\nDatos del Pasaje:")
            print(f"Ciudad: {ventas[i]['ciudad']}")
            print(f"País: {ventas[i]['pais']}")
            print(f"Fecha: {ventas[i]['fecha']}")
            print(f"Monto: ${ventas[i]['monto']}")
            print(f"Estado: {ventas[i]['estado']}")
            print("-" * 50)
        
        while True:
            try:
                indice = int(input("\nIngrese el número de la venta a eliminar: ")) - 1
                if 0 <= indice < len(ventas):
                    venta = ventas[indice]
                    # Buscar datos del cliente
                    cliente = next((c for c in clientes if c['cuit'] == venta['cuit_cliente']), None)
                    
                    print(f"\n¿Está seguro que desea eliminar la siguiente venta?")
                    print("\nDatos del Cliente:")
                    print(f"CUIT: {venta['cuit_cliente']}")
                    print(f"Razón Social: {cliente['razon_social'] if cliente else 'Cliente no encontrado'}")
                    print(f"Correo: {cliente['correo'] if cliente else 'Cliente no encontrado'}")
                    
                    print("\nDatos del Pasaje:")
                    print(f"Ciudad: {venta['ciudad']}")
                    print(f"País: {venta['pais']}")
                    print(f"Fecha: {venta['fecha']}")
                    print(f"Monto: ${venta['monto']}")
                    print(f"Estado: {venta['estado']}")
                    
                    confirmacion = input("\nIngrese 'SI' para confirmar la eliminación: ")
                    if confirmacion.upper() == 'SI':
                        ventas.pop(indice)
                        print("\nVenta eliminada exitosamente.")
                    else:
                        print("\nOperación cancelada.")
                    break
                else:
                    print("Número de venta no válido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

def boton_arrepentimiento():
    if not ventas:
        print("\nNo hay ventas registradas.")
    else:
        print("\nVentas Activas:")
        ventas_activas = [v for v in ventas if v['estado'] == 'Activa']
        if not ventas_activas:
            print("No hay ventas activas para anular.")
            return
        
        for i in range(len(ventas_activas)):
            # Buscar datos del cliente
            cliente = next((c for c in clientes if c['cuit'] == ventas_activas[i]['cuit_cliente']), None)
            
            print(f"\nVenta {i + 1}:")
            print("\nDatos del Cliente:")
            print(f"CUIT: {ventas_activas[i]['cuit_cliente']}")
            print(f"Razón Social: {cliente['razon_social'] if cliente else 'Cliente no encontrado'}")
            print(f"Correo: {cliente['correo'] if cliente else 'Cliente no encontrado'}")
            
            print("\nDatos del Pasaje:")
            print(f"Ciudad: {ventas_activas[i]['ciudad']}")
            print(f"País: {ventas_activas[i]['pais']}")
            print(f"Fecha: {ventas_activas[i]['fecha']}")
            print(f"Monto: ${ventas_activas[i]['monto']}")
            print(f"Estado: {ventas_activas[i]['estado']}")
            print("-" * 50)
        
        while True:
            try: #Try es una estructura que se utiliza para manejar errores, de esta forma mostramos un mensaje de error en vez de que se detenga el sistema
                indice = int(input("\nIngrese el número de la venta a anular: ")) - 1
                if 0 <= indice < len(ventas_activas):
                    venta = ventas_activas[indice]
                    # Buscar datos del cliente
                    cliente = next((c for c in clientes if c['cuit'] == venta['cuit_cliente']), None)
                    
                    print(f"\n¿Está seguro que desea anular la siguiente venta?")
                    print("\nDatos del Cliente:")
                    print(f"CUIT: {venta['cuit_cliente']}")
                    print(f"Razón Social: {cliente['razon_social'] if cliente else 'Cliente no encontrado'}")
                    print(f"Correo: {cliente['correo'] if cliente else 'Cliente no encontrado'}")
                    
                    print("\nDatos del Pasaje:")
                    print(f"Ciudad: {venta['ciudad']}")
                    print(f"País: {venta['pais']}")
                    print(f"Fecha: {venta['fecha']}")
                    print(f"Monto: ${venta['monto']}")
                    print(f"Estado: {venta['estado']}")
                    
                    confirmacion = input("\nIngrese 'SI' para confirmar la anulación: ")
                    if confirmacion.upper() == 'SI':
                        # Encontrar la venta en la lista original y actualizar su estado
                        for v in ventas:
                            if (v['cuit_cliente'] == venta['cuit_cliente'] and 
                                v['ciudad'] == venta['ciudad'] and 
                                v['pais'] == venta['pais'] and 
                                v['fecha'] == venta['fecha']):
                                v['estado'] = 'Anulada'
                                break
                        print("\nVenta anulada exitosamente.")
                    else:
                        print("\nOperación cancelada.")
                    break
                else:
                    print("Número de venta no válido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

# Agregar las nuevas funciones de consulta
def ventas_del_dia():
    from datetime import datetime
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    
    # Filtrar ventas activas del día
    ventas_dia = [v for v in ventas if v['fecha'].startswith(fecha_actual) and v['estado'] == 'Activa']
    
    if not ventas_dia:
        print(f"\nNo hay ventas activas registradas para el día {fecha_actual}")
    else:
        print(f"\nVentas activas del día {fecha_actual}:")
        for i in range(len(ventas_dia)):
            # Buscar datos del cliente
            cliente = next((c for c in clientes if c['cuit'] == ventas_dia[i]['cuit_cliente']), None) #Con next permite devolver el prmer resultado que coincida sino muestra None
            
            print(f"\nVenta {i + 1}:")
            print("\nDatos del Cliente:")
            print(f"CUIT: {ventas_dia[i]['cuit_cliente']}")
            print(f"Razón Social: {cliente['razon_social'] if cliente else 'Cliente no encontrado'}")
            print(f"Correo: {cliente['correo'] if cliente else 'Cliente no encontrado'}")
            
            print("\nDatos del Pasaje:")
            print(f"Ciudad: {ventas_dia[i]['ciudad']}")
            print(f"País: {ventas_dia[i]['pais']}")
            print(f"Fecha: {ventas_dia[i]['fecha']}")
            print(f"Monto: ${ventas_dia[i]['monto']}")
            print(f"Estado: {ventas_dia[i]['estado']}")
            print("-" * 50)

def ventas_ultima_semana():
    from datetime import datetime, timedelta #Para trabajar con fechas primero debemos importarlas
    fecha_actual = datetime.now() #Datetime nos permite saber la fecha y la hora
    fecha_inicio = (fecha_actual - timedelta(days=7)).strftime("%d/%m/%Y") #timedelta nos permite hacer operaciones con las fechas por ejemplo para saber las ventas de esta semana
    
    # Filtrar ventas activas de la última semana
    ventas_semana = [v for v in ventas if v['estado'] == 'Activa'] #Filtramos de la lista ventas las activas
    ventas_semana = [v for v in ventas_semana if datetime.strptime(v['fecha'], "%d/%m/%Y %H:%M") >= datetime.strptime(fecha_inicio, "%d/%m/%Y")] #datetime.strptime convierte strings de fecha a objetos datetime, para poder comparar fechas
    #Los "%d/%m/%Y %H:%M" son formatos de fecha que utiliza Python y la / para separar los items

    if not ventas_semana:
        print(f"\nNo hay ventas activas registradas desde {fecha_inicio}")
    else:
        print(f"\nVentas activas desde {fecha_inicio}:")
        for i in range(len(ventas_semana)):
            # Buscar datos del cliente
            cliente = next((c for c in clientes if c['cuit'] == ventas_semana[i]['cuit_cliente']), None)
            
            print(f"\nVenta {i + 1}:")
            print("\nDatos del Cliente:")
            print(f"CUIT: {ventas_semana[i]['cuit_cliente']}")
            print(f"Razón Social: {cliente['razon_social'] if cliente else 'Cliente no encontrado'}")
            print(f"Correo: {cliente['correo'] if cliente else 'Cliente no encontrado'}")
            
            print("\nDatos del Pasaje:")
            print(f"Ciudad: {ventas_semana[i]['ciudad']}")
            print(f"País: {ventas_semana[i]['pais']}")
            print(f"Fecha: {ventas_semana[i]['fecha']}")
            print(f"Monto: ${ventas_semana[i]['monto']}")
            print(f"Estado: {ventas_semana[i]['estado']}")
            print("-" * 50)

def ventas_por_cliente():
    if not ventas:
        print("\nNo hay ventas registradas.")
        return
    
    # Mostrar lista de clientes
    print("\nClientes disponibles:")
    for i in range(len(clientes)):
        print(f"\nCliente {i + 1}:")
        print(f"CUIT: {clientes[i]['cuit']}")
        print(f"Razón Social: {clientes[i]['razon_social']}")
        print(f"Correo: {clientes[i]['correo']}")
        print("-" * 30)
    
    # Selección de cliente
    while True:
        try:
            indice = int(input("\nIngrese el número del cliente para ver sus ventas: ")) - 1
            if 0 <= indice < len(clientes):
                cliente = clientes[indice]
                # Filtrar ventas activas del cliente
                ventas_cliente = [v for v in ventas if v['cuit_cliente'] == cliente['cuit'] and v['estado'] == 'Activa']
                
                if not ventas_cliente:
                    print(f"\nNo hay ventas activas registradas para el cliente {cliente['razon_social']}")
                else:
                    print(f"\nVentas activas del cliente {cliente['razon_social']}:")
                    for i in range(len(ventas_cliente)):
                        print(f"\nVenta {i + 1}:")
                        print("\nDatos del Cliente:")
                        print(f"CUIT: {cliente['cuit']}")
                        print(f"Razón Social: {cliente['razon_social']}")
                        print(f"Correo: {cliente['correo']}")
                        
                        print("\nDatos del Pasaje:")
                        print(f"Ciudad: {ventas_cliente[i]['ciudad']}")
                        print(f"País: {ventas_cliente[i]['pais']}")
                        print(f"Fecha: {ventas_cliente[i]['fecha']}")
                        print(f"Monto: ${ventas_cliente[i]['monto']}")
                        print(f"Estado: {ventas_cliente[i]['estado']}")
                        print("-" * 50)
                break
            else:
                print("Número de cliente no válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def ver_ventas_anuladas():
    # Filtrar ventas anuladas
    ventas_anuladas = [v for v in ventas if v['estado'] == 'Anulada']
    
    if not ventas_anuladas:
        print("\nNo hay ventas anuladas registradas.")
    else:
        print("\nVentas Anuladas:")
        for i in range(len(ventas_anuladas)):
            # Buscar datos del cliente
            cliente = next((c for c in clientes if c['cuit'] == ventas_anuladas[i]['cuit_cliente']), None)
            
            print(f"\nVenta {i + 1}:")
            print("\nDatos del Cliente:")
            print(f"CUIT: {ventas_anuladas[i]['cuit_cliente']}")
            print(f"Razón Social: {cliente['razon_social'] if cliente else 'Cliente no encontrado'}")
            print(f"Correo: {cliente['correo'] if cliente else 'Cliente no encontrado'}")
            
            print("\nDatos del Pasaje:")
            print(f"Ciudad: {ventas_anuladas[i]['ciudad']}")
            print(f"País: {ventas_anuladas[i]['pais']}")
            print(f"Fecha: {ventas_anuladas[i]['fecha']}")
            print(f"Monto: ${ventas_anuladas[i]['monto']}")
            print(f"Estado: {ventas_anuladas[i]['estado']}")
            print("-" * 50)

# Ciclo para poder navergar en el menu principal
while True:
    # Mostrar mensaje de bienvenida y menú principal
    print("\n-------------------------------------------------------")
    print("Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes")
    print("-------------------------------------------------------")
    print("\n| Menú Principal |\n")
    for i in range(len(menu_principal)):
        if i == 7:  # Antes de la última opción
            print()  # Salto de línea
        print(f"{i + 1}. {menu_principal[i]}")
    
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
            for i in range(len(submenu_gestion)):
                print(f"{i + 1}. {submenu_gestion[i]}")
            
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
            for i in range(len(submenu_gestion)):
                print(f"{i + 1}. {submenu_gestion[i]}")
            
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
                eliminar_destino()
            elif subopcion == 5:  # Volver al Menú Principal
                break
            
            input("\nPresione Enter para continuar...")
    
    elif opcion == 3:  # Gestionar Ventas
        while True:
            print("\n--- Gestionar Ventas ---")
            for i in range(len(submenu_gestion)):
                print(f"{i + 1}. {submenu_gestion[i]}")
            
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
                eliminar_venta()
            elif subopcion == 5:  # Volver al Menú Principal
                break
            
            input("\nPresione Enter para continuar...")
    
    elif opcion == 4:  # Consultar Ventas
        while True:
            print("\n--- Consultar Ventas ---")
            for i in range(len(submenu_consulta)):
                print(f"{i + 1}. {submenu_consulta[i]}")
            
            # Captura y validación de la subopción
            while True:
                subopcion = input("\nSeleccione una opción (1-5): ")
                if subopcion.isdigit() and 1 <= int(subopcion) <= 5:
                    subopcion = int(subopcion)
                    break
                print("Entrada no válida, intente nuevamente")
            
            if subopcion == 1:  # Ventas activas del día
                ventas_del_dia()
            elif subopcion == 2:  # Ventas activas de la última semana
                ventas_ultima_semana()
            elif subopcion == 3:  # Ventas activas por cliente
                ventas_por_cliente()
            elif subopcion == 4:  # Ver ventas anuladas
                ver_ventas_anuladas()
            elif subopcion == 5:  # Volver al Menú Principal
                break
            
            input("\nPresione Enter para continuar...")
    
    elif opcion == 5:  # Botón de Arrepentimiento
        boton_arrepentimiento()
        input("\nPresione Enter para continuar...")
    
    elif opcion == 6:  # Ver Reporte General
        print("\nProximamente...\n")
        input("\nPresione Enter para continuar...")
    
    elif opcion == 7:  # Acerca del Sistema
        print("\nSKYROUTE - Sistema de Gestion de Pasajes v1.0.\n")
        print("Proyecto ABP del modulo programador del ISPC\n")
        print("Integrantes:\n")
        print("Enrico Munighini, Antonella\t44.194.338")
        print("Marovich, Mikael\t\t41.625.321") #El \t es una tabulacion, asi quedan alineados los DNIs
        print("Montiel, Matias\t\t\t42.474.994")
        print("Sanchez, Romina\t\t\t45.348.881")
        print("Villarruel, Tomas\t\t44.896.222")
        input("\nPresione Enter para continuar...")
    
    elif opcion == 8:  # Salir
        print("\n¡Gracias por usar Skyroute!\n")
        print("Nos vemos.")
        break