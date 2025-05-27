# Sistema de Gestión de Pasajes SkyRoute

#ENCABEZADO
#Propósito del sistema:
#El sistema fue desarrollado con el objetivo de gestionar clientes y destinos de manera eficiente, ofreciendo funcionalidades para 
# ingresar, modificar, visualizar y eliminar datos a través de una interfaz de consola amigable. Está orientado a facilitar el manejo de información 
# en entornos donde se requiere un control sencillo pero funcional de registros relacionados con servicios o viajes.


#Instalación y ejecución:
#Requisitos previos:
#Python 3.10 o superior
#Sistema operativo: Windows, Linux o macOS


#Ejecturar programa:
#python main.py


#Integrantes del grupo:
#Nombre y Apellido	               DNI
#Enrico Munighini, Antonella	   44.194.338
#Marovich, Mikael	               41.625.321
#Montiel, Matías	               42.474.994
#Sánchez, Romina	               45.348.881
#Villarruel, Tomás	               44.896.222

#Fecha de entrega: 26/05/2025
#Versión del sistema: 1.0.0

#------------------------------------------------------------------------------------------------------------------------

#Aca definimos las opciones en los menus con una tupla
menu_principal = ("Gestionar Clientes", "Gestionar Destinos", "Gestionar Ventas", 
                 "Consultar Ventas", "Botón de Arrepentimiento", "Ver Reporte General", 
                 "Acerca del Sistema", "Salir")
submenu_gestion = ("Ver", "Agregar", "Modificar", "Eliminar", "Volver al Menú Principal")
submenu_consulta = ("Ventas activas del día", "Ventas activas de la última semana", 
                   "Ventas activas por cliente", "Ver ventas anuladas", "Volver al Menú Principal")
submenu_reporte = ("Ver resumen de ventas", "Ver destinos más vendidos", "Ver clientes frecuentes", "Volver al Menú Principal")



# Definimos los vectores que vamos a utilizar para almacenar datos, ya que estos son los que se pueden modificar luego
clientes = [
  {"id": 1, "razon_social": "Ferreteria S.A", "cuit": "12345678", "email": "ferreteria@mail.com"},
  {"id": 2, "razon_social": "Materiales de Construcción", "cuit": "87654321", "email": "materiales@mail.com"},
  {"id": 3, "razon_social": "Textil S.A", "cuit": "11223344", "email": "textil@mail.com"}
]
destinos = [
    {"id": 1, "nombre": "Buenos Aires", "costo_base": 1000},
    {"id": 2, "nombre": "Córdoba", "costo_base": 800},
    {"id": 3, "nombre": "Mendoza", "costo_base": 1200},
    {"id": 4, "nombre": "Bariloche", "costo_base": 1500}
]

ventas = [
    {"id": 1, "cliente_id": 1, "destino_id": 2, "fecha": "01/10/2023 10:00", "estado": "Activa", "monto": 800},
    {"id": 2, "cliente_id": 2, "destino_id": 1, "fecha": "01/10/2023 11:00", "estado": "Activa", "monto": 1000},
    {"id": 3, "cliente_id": 1, "destino_id": 3, "fecha": "01/10/2023 12:00", "estado": "Activa", "monto": 1200},
    {"id": 4, "cliente_id": 3, "destino_id": 4, "fecha": "01/10/2023 13:00", "estado": "Activa", "monto": 1500},
    {"id": 5, "cliente_id": 2, "destino_id": 3, "fecha": "01/10/2023 14:00", "estado": "Activa", "monto": 1200}
]


# ------------------------------------------ Función para Generar ID Único ----------------------------------------
def generar_id(lista):
    if not lista:
        return 1
    return max(item["id"] for item in lista) + 1

#---------------------------------------- Funciones para Gestionar Clientes ----------------------------------------
def ver_clientes():
    if not clientes:
        print("\nNo hay clientes registrados.")
    else:
        print("\nLista de Clientes:")
        for idx, cliente in enumerate(clientes, start=1):
            print(f"\nCliente {idx}:")
            print(f"ID: {cliente['id']}")
            print(f"Razón Social: {cliente['razon_social']}")
            print(f"CUIT: {cliente['cuit']}")
            print(f"Email: {cliente['email']}")
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
        email = input("Ingrese correo electrónico: ")
        if '@' in email and '.' in email:
            break
        print("Ingrese un correo electrónico válido")
    
    # Generar ID único
    cliente_id = generar_id(clientes)

    # Agregar cliente a la lista
    clientes.append({
        'id': cliente_id,
        'cuit': cuit,
        'razon_social': razon_social,
        'email': email
    })
    
    print(f"\nCliente agregado exitosamente:")
    print(f"ID: {cliente_id}")
    print(f"CUIT: {cuit}")
    print(f"Razón Social: {razon_social}")
    print(f"Email: {email}")

def modificar_cliente():
    ver_clientes()
    if not clientes:
        print("\nNo hay clientes para modificar.")
        return
    # Selección por ID
    while True:
        try:
            id_sel = int(input("\nIngrese el ID del cliente a modificar (0 para cancelar): "))
            if id_sel == 0:
                print("\nOperación cancelada.")
                return
            cliente = next((c for c in clientes if c['id'] == id_sel), None)
            if cliente:
                break
            print("ID de cliente no válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    # Mostrar datos actuales
    print(f"\nModificando cliente con ID {cliente['id']}: ")
    print(f"CUIT actual: {cliente['cuit']}")
    print(f"Razón Social actual: {cliente['razon_social']}")
    print(f"Email actual: {cliente['email']}")
    
    # Modificar datos
    nuevo_cuit = input("Ingrese nuevo CUIT (Enter para mantener el actual): ")
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
    
    nuevo_email = input("Ingrese nuevo email (Enter para mantener el actual): ")
    if nuevo_email:
        if '@' in nuevo_email and '.' in nuevo_email:
            cliente['email'] = nuevo_email
        else:
            print("Email no válido, se mantiene el actual")
    
    print("\nCliente modificado exitosamente:")
    print(f"ID: {cliente['id']}")
    print(f"CUIT: {cliente['cuit']}")
    print(f"Razón Social: {cliente['razon_social']}")
    print(f"Email: {cliente['email']}")

def eliminar_cliente():
    ver_clientes()
    if not clientes:
        print("\nNo hay clientes para modificar.")
        return
    # Selección por ID
    while True:
        try:
            id_sel = int(input("\nIngrese el ID del cliente a eliminar (0 para cancelar): "))
            if id_sel == 0:
                print("\nOperación cancelada.")
                return
            cliente = next((c for c in clientes if c['id'] == id_sel), None)
            if cliente:
                break
            print("ID de cliente no válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    # Confirmar eliminación
    print(f"\n¿Está seguro que desea eliminar el siguiente cliente?")
    print(f"ID: {cliente['id']}")
    print(f"Razón Social: {cliente['razon_social']}")
    print(f"CUIT: {cliente['cuit']}")
    print(f"Email: {cliente['email']}")
    
    # Verificar si el cliente tiene ventas asociadas
    ventas_cliente = [v for v in ventas if v.get('cliente_id') == cliente['id']]
    if ventas_cliente:
        print("\n¡ADVERTENCIA! Este cliente tiene ventas asociadas:")
        for v in ventas_cliente:
            destino = next((d for d in destinos if d['id'] == v['destino_id']), None)
            destino_nombre = destino['nombre'] if destino else 'Destino desconocido'
            print(f"- Venta del {v['fecha']} a {destino_nombre} (Estado: {v['estado']})")
        print("\nNo se puede eliminar el cliente porque tiene ventas asociadas.")
        print("Primero debe eliminar o anular todas las ventas del cliente.")
        return
    
    confirmacion = input("\nIngrese 'SI' para confirmar la eliminación: ")
    # Confirmar y eliminar
    if confirmacion.upper() == 'SI':
        clientes.remove(cliente)
        print("\nCliente eliminado exitosamente.")
    else:
        print("\nOperación cancelada.")

#---------------------------------------- Funciones para Gestionar Destinos ----------------------------------------
def ver_destinos():
    if not destinos:
        print("\nNo hay destinos registrados.")
    else:
        print("\nLista de Destinos:")
        for i in range(len(destinos)):
            print(f"\nDestino {i + 1}:")
            print(f"Nombre: {destinos[i]['nombre']}")
            print(f"Costo Base: ${destinos[i]['costo_base']}")
            print("-" * 30)

def agregar_destino():
    print("\n--- Agregar Destino ---")
    nombre = input("Ingrese el nombre del destino: ")
    costo_base = 0
    # Verificar si el destino ya existe
    if any(destino['nombre'] == nombre for destino in destinos):
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

        destino_id = generar_id(destinos)  # Generar ID único para el nuevo destino

        # Agregar destino a la lista
        destinos.append({
            'id': destino_id,
            'nombre': nombre,
            'costo_base': costo_base
        })
        
        print(f"\nDestino agregado exitosamente:")
        print(f"ID: {destino_id}")
        print(f"Nombre: {nombre}")
        print(f"Costo Base: ${costo_base}")

def modificar_destino():
        ver_destinos()
        if not destinos:
            print("\nNo hay destinos para modificar.")
            return
        # Selección por ID
        while True:
            try:
                id_sel = int(input("\nIngrese el ID del destino a modificar (0 para cancelar): "))
                if id_sel == 0:
                    print("\nOperación cancelada.")
                    return
                destino = next((d for d in destinos if d['id'] == id_sel), None)
                if destino:
                    break
                print("ID de destino no válido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        # Mostrar datos actuales
        print(f"\nModificando destino con ID {destino['id']}:")
        print(f"Nombre actual: {destino['nombre']}")
        print(f"Costo Base actual: ${destino['costo_base']}")
        
        # Modificar datos
        nuevo_nombre = input("Ingrese nuevo nombre (Enter para mantener el actual): ")
        if nuevo_nombre:
            # Verificar si el nuevo destino ya existe
            if any(d['nombre'] == nuevo_nombre and d != destino for d in destinos):
                print("Este destino ya está registrado.")
            else:
                destino['nombre'] = nuevo_nombre
        
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
        
        print("\nDestino modificado exitosamente:")
        print(f"Nombre: {destino['nombre']}")
        print(f"Costo Base: ${destino['costo_base']}")

def eliminar_destino():
        ver_destinos()
        if not destinos:
            print("\nNo hay destinos para eliminar.")
            return
        # Selección por ID
        while True:
            try:
                id_sel = int(input("\nIngrese el ID del destino a eliminar (0 para cancelar): "))
                if id_sel == 0:
                    print("\nOperación cancelada.")
                    return
                destino = next((d for d in destinos if d['id'] == id_sel), None)
                if destino:
                    break
                print("ID de destino no válido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        # Confirmar eliminación
        print(f"\n¿Está seguro que desea eliminar el siguiente destino?")
        print(f"ID: {destino['id']}")
        print(f"Nombre: {destino['nombre']}")
        print(f"Costo Base: ${destino['costo_base']}")
        
        confirmacion = input("\nIngrese 'SI' para confirmar la eliminación: ")
        if confirmacion.upper() == 'SI':
            destinos.remove(destino)
            print("\nDestino eliminado exitosamente.")
        else:
            print("\nOperación cancelada.")

#---------------------------------------- Funciones para Gestionar Ventas ----------------------------------------
def ver_ventas():
    if not ventas:
        print("\nNo hay ventas registradas.")
    else:
        print("\nLista de Ventas:")
        for venta in ventas:
            # Obtener cliente y destino por sus IDs
            cliente = next((c for c in clientes if c['id'] == venta.get('cliente_id')), None)
            destino = next((d for d in destinos if d['id'] == venta.get('destino_id')), None)
            print(f"\nVenta ID: {venta.get('id')}")
            print(f"Fecha: {venta['fecha']}")
            print(f"Estado: {venta['estado']}")
            
            print("\nDatos del Cliente:")
            if cliente:
                print(f"ID: {cliente['id']}")
                print(f"Razón Social: {cliente['razon_social']}")
                print(f"CUIT: {cliente['cuit']}")
                print(f"Email: {cliente['email']}")
            else:
                print("Cliente no encontrado")
            print("\nDatos del Destino:")
            if destino:
                print(f"Nombre: {destino['nombre']}")
                print(f"Costo Base: ${destino['costo_base']}")
            else:
                print("Destino no encontrado")
            print("-" * 50)

def agregar_venta():
    print("\n--- Agregar Venta ---")
    # Mostrar todos los clientes disponibles solo una vez
    print("\nClientes disponibles:")
    for cliente in clientes:
        print(f"ID: {cliente['id']} | Razón Social: {cliente['razon_social']} | CUIT: {cliente['cuit']}")
        print("-" * 30)

    # Selección de cliente por ID
    while True:
        cliente_id = input("Ingrese el ID del cliente (solo números): ")
        if cliente_id.isdigit():
            cliente_id = int(cliente_id)
            cliente = next((c for c in clientes if c['id'] == cliente_id), None)
            if not cliente:
                print("Este ID no está registrado como cliente.")
                continue
            break
        print("El ID debe ser un número válido.")
        
    # Mostrar destinos disponibles solo una vez
    print("\nDestinos disponibles:")
    for destino in destinos:
        print(f"ID: {destino['id']} | Nombre: {destino['nombre']} | Costo Base: ${destino['costo_base']}")
        print("-" * 30)

    # Selección de destino por ID
    while True:
        destino_id = input("Ingrese el ID del destino: ")
        if destino_id.isdigit():
            destino_id = int(destino_id)
            destino = next((d for d in destinos if d['id'] == destino_id), None)
            if not destino:
                print("Este ID no está registrado como destino.")
                continue
            break
        print("El ID debe ser un número válido.")

    # Obtener fecha actual
    from datetime import datetime
    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
    venta_id = generar_id(ventas)
    
    # Agregar venta a la lista
    ventas.append({
        'id': venta_id,
        'cliente_id': cliente_id,
        'destino_id': destino_id,
        'fecha': fecha_actual,
        'estado': 'Activa',
        'monto': destino['costo_base']
    })
    print("-" * 10)
    print(f"\nVenta agregada exitosamente:")
    print(f"ID: {venta_id}")
    print("-" * 10)
    print("\nDatos del Cliente:")
    print(f"ID: {cliente['id']}")
    print(f"Razón Social: {cliente['razon_social']}")
    print(f"Email: {cliente['email']}")
    print("\nDatos del Pasaje:")
    print(f"Fecha: {fecha_actual}")
    print(f"Destino: {destino['nombre']}")
    print(f"Monto: ${destino['costo_base']}")
    print(f"Estado: Activa")

def modificar_venta():
    ver_ventas()
    if not ventas:
        print("\nNo hay ventas registradas para modificar.")
        return
    
    print("\nLista de Ventas:")
    for venta in ventas:
        cliente = next((c for c in clientes if c['id'] == venta.get('cliente_id')), None)
        destino = next((d for d in destinos if d['id'] == venta.get('destino_id')), None)
        print(f"ID Venta: {venta['id']}")
        print("Datos del Cliente:")
        if cliente:
            print(f"Cuit: {cliente['cuit']}")
            print(f"Razón Social: {cliente['razon_social']}")
            print(f"Email: {cliente['email']}")
        else:
            print("Cliente no encontrado")
        print("Datos del Destino:")
        if destino:
            print(f"Nombre: {destino['nombre']}")
            print(f"Costo Base: ${destino['costo_base']}")
        else:
            print("Destino no encontrado")
        print("-" * 50)
    while True:
        try:
            venta_id = int(input("\nIngrese el ID de la venta a modificar (0 para cancelar): "))
            if venta_id == 0:
                print("\nOperación cancelada.")
                return
            venta = next((v for v in ventas if v['id'] == venta_id), None)
            if venta:
                break
            print("ID de venta no válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
            
    # Modificar cliente
    print("\nClientes disponibles:")
    for cliente in clientes:
        print(f"ID: {cliente['id']} | Razón Social: {cliente['razon_social']} | CUIT: {cliente['cuit']}")
    while True:
        nuevo_cliente_id = input(f"Ingrese nuevo ID de cliente (actual {venta['cliente_id']}, Enter para mantener): ")
        if not nuevo_cliente_id:
            break
        if nuevo_cliente_id.isdigit():
            nuevo_cliente_id = int(nuevo_cliente_id)
            if any(c['id'] == nuevo_cliente_id for c in clientes):
                venta['cliente_id'] = nuevo_cliente_id
                break
            else:
                print("ID de cliente no válido.")
        else:
            print("El ID debe ser un número válido.")
            
    # Modificar destino
    print("\nDestinos disponibles:")
    for destino in destinos:
        print(f"ID: {destino['id']} | Nombre: {destino['nombre']} | Costo Base: ${destino['costo_base']}")
    while True:
        nuevo_destino_id = input(f"Ingrese nuevo ID de destino (actual {venta['destino_id']}, Enter para mantener): ")
        if not nuevo_destino_id:
            break
        if nuevo_destino_id.isdigit():
            nuevo_destino_id = int(nuevo_destino_id)
            destino = next((d for d in destinos if d['id'] == nuevo_destino_id), None)
            if destino:
                venta['destino_id'] = nuevo_destino_id
                venta['monto'] = destino['costo_base']
                break
            else:
                print("ID de destino no válido.")
        else:
            print("El ID debe ser un número válido.")
            
    print("\nVenta modificada exitosamente.")
    print(f"ID Venta: {venta['id']}")
    print(f"Cliente ID: {venta['cliente_id']}")
    print(f"Destino ID: {venta['destino_id']}")
    print(f"Monto: ${venta['monto']}")
    print(f"Estado: {venta['estado']}")

def eliminar_venta():
    if not ventas:
        print("\nNo hay ventas registradas para eliminar.")
        return
    
    print("\nLista de Ventas:")
    for venta in ventas:
        cliente = next((c for c in clientes if c['id'] == venta.get('cliente_id')), None)
        destino = next((d for d in destinos if d['id'] == venta.get('destino_id')), None)
        print(f"ID Venta: {venta['id']}")
        print("Datos del Cliente:")
        if cliente:
            print(f"ID: {cliente['id']}")
            print(f"Razón Social: {cliente['razon_social']}")
            print(f"Email: {cliente['email']}")
        else:
            print("Cliente no encontrado")
        print("Datos del Destino:")
        if destino:
            print(f"Nombre: {destino['nombre']}")
            print(f"Costo Base: ${destino['costo_base']}")
        else:
            print("Destino no encontrado")
        print("-" * 50)
    while True:
        try:
            venta_id = int(input("\nIngrese el ID de la venta a eliminar (0 para cancelar): "))
            if venta_id == 0:
                print("\nOperación cancelada.")
                return
            venta = next((v for v in ventas if v['id'] == venta_id), None)
            if venta:
                break
            print("ID de venta no válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    confirmacion = input("\nIngrese 'SI' para confirmar la eliminación: ")
    if confirmacion.upper() == 'SI':
        ventas.remove(venta)
        print("\nVenta eliminada exitosamente.")
    else:
        print("\nOperación cancelada.")

def boton_arrepentimiento():
    if not ventas:
        print("\nNo hay ventas registradas.")
        return
    
    ventas_activas = [v for v in ventas if v.get('estado', 'Activa') == 'Activa']
    if not ventas_activas:
        print("No hay ventas activas para anular.")
        return
    print("\nVentas Activas:")
    for venta in ventas_activas:
        cliente = next((c for c in clientes if c['id'] == venta.get('cliente_id')), None)
        destino = next((d for d in destinos if d['id'] == venta.get('destino_id')), None)
        print(f"ID Venta: {venta['id']}")
        print(f"Fecha: {venta.get('fecha', 'N/A')}")
        print(f"Monto: ${venta.get('monto', 'N/A')}")
        print(f"Estado: {venta.get('estado', 'N/A')}")
        print("Datos del Cliente:")
        if cliente:
            print(f"ID: {cliente['id']}")
            print(f"Razón Social: {cliente['razon_social']}")
            print(f"Email: {cliente['email']}")
        else:
            print("Cliente no encontrado")
        print("Datos del Destino:")
        if destino:
            print(f"Nombre: {destino['nombre']}")
            print(f"Costo Base: ${destino['costo_base']}")
        else:
            print("Destino no encontrado")
        print("-" * 50)
    while True:
        try:
            venta_id = int(input("\nIngrese el ID de la venta que desea anular (0 para cancelar): "))
            if venta_id == 0:
                print("\nOperación cancelada.")
                return
            venta = next((v for v in ventas_activas if v['id'] == venta_id), None)
            if not venta:
                print("ID de venta no válido o no activa.")
                continue
           
            confirmacion = input("\nIngrese 'SI' para confirmar la anulación: ")
            if confirmacion.upper() == 'SI':
                venta['estado'] = 'Anulada'
                print("\nVenta anulada exitosamente.")
            else:
                print("\nOperación cancelada.")
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

#---------------------------------------- Funciones para Consultar Ventas ----------------------------------------
def ventas_del_dia():
    from datetime import datetime
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    ventas_dia = [v for v in ventas if v.get('fecha', '').startswith(fecha_actual) and v.get('estado', 'Activa') == 'Activa']
    if not ventas_dia:
        print(f"\nNo hay ventas activas registradas para el día {fecha_actual}")
    else:
        print(f"\nVentas activas del día {fecha_actual}:")
        for venta in ventas_dia:
            cliente = next((c for c in clientes if c['id'] == venta.get('cliente_id')), None)
            destino = next((d for d in destinos if d['id'] == venta.get('destino_id')), None)
            print(f"ID Venta: {venta['id']}")
            print("Datos del Cliente:")
            if cliente:
                print(f"ID: {cliente['id']}")
                print(f"Razón Social: {cliente['razon_social']}")
                print(f"Email: {cliente['email']}")
            else:
                print("Cliente no encontrado")
            print("Datos del Destino:")
            if destino:
                print(f"Nombre: {destino['nombre']}")
                print(f"Costo Base: ${destino['costo_base']}")
            else:
                print("Destino no encontrado")
            print(f"Fecha: {venta.get('fecha', 'N/A')}")
            print(f"Monto: ${venta.get('monto', 'N/A')}")
            print(f"Estado: {venta.get('estado', 'N/A')}")
            print("-" * 50)

def ventas_ultima_semana():
    from datetime import datetime, timedelta
    fecha_actual = datetime.now()
    fecha_inicio = fecha_actual - timedelta(days=7)
    ventas_semana = [v for v in ventas if v.get('estado', 'Activa') == 'Activa']
    ventas_semana = [v for v in ventas_semana if 'fecha' in v and datetime.strptime(v['fecha'], "%d/%m/%Y %H:%M") >= fecha_inicio]
    if not ventas_semana:
        print(f"\nNo hay ventas activas registradas desde {fecha_inicio.strftime('%d/%m/%Y')}")
    else:
        print(f"\nVentas activas desde {fecha_inicio.strftime('%d/%m/%Y')}:")
        for venta in ventas_semana:
            cliente = next((c for c in clientes if c['id'] == venta.get('cliente_id')), None)
            destino = next((d for d in destinos if d['id'] == venta.get('destino_id')), None)
            print(f"ID Venta: {venta['id']}")
            print("Datos del Cliente:")
            if cliente:
                print(f"ID: {cliente['id']}")
                print(f"Razón Social: {cliente['razon_social']}")
                print(f"Email: {cliente['email']}")
            else:
                print("Cliente no encontrado")
            print("Datos del Destino:")
            if destino:
                print(f"Nombre: {destino['nombre']}")
                print(f"Costo Base: ${destino['costo_base']}")
            else:
                print("Destino no encontrado")
            print(f"Fecha: {venta.get('fecha', 'N/A')}")
            print(f"Monto: ${venta.get('monto', 'N/A')}")
            print(f"Estado: {venta.get('estado', 'N/A')}")
            print("-" * 50)

def ventas_por_cliente():
    if not ventas:
        print("\nNo hay ventas registradas.")
        return
    
    print("\nClientes disponibles:")
    for cliente in clientes:
        print(f"ID: {cliente['id']} | Razón Social: {cliente['razon_social']} | CUIT: {cliente['cuit']}")
    while True:
        try:
            cliente_id = int(input("\nIngrese el ID del cliente para ver sus ventas: "))
            cliente = next((c for c in clientes if c['id'] == cliente_id), None)
            if cliente:
                ventas_cliente = [v for v in ventas if v.get('cliente_id') == cliente_id and v.get('estado', 'Activa') == 'Activa']
                if not ventas_cliente:
                    print(f"\nNo hay ventas activas registradas para el cliente {cliente['razon_social']}")
                else:
                    print(f"\nVentas activas del cliente {cliente['razon_social']}:")
                    for venta in ventas_cliente:
                        destino = next((d for d in destinos if d['id'] == venta.get('destino_id')), None)
                        print(f"\nVenta ID: {venta['id']}")
                        print("Datos del Cliente:")
                        print(f"ID: {cliente['id']}")
                        print(f"Razón Social: {cliente['razon_social']}")
                        print(f"Email: {cliente['email']}")
                        print("Datos del Pasaje:")
                        print(f"Fecha: {venta.get('fecha', 'N/A')}")
                        if destino:
                            print(f"Destino: {destino['nombre']}")
                            print(f"Monto: ${destino['costo_base']}")
                        else:
                            print("Destino no encontrado")
                        print(f"Estado: {venta.get('estado', 'Activa')}")
                        print("-" * 50)
                break
            else:
                print("ID de cliente no válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def ver_ventas_anuladas():
    ventas_anuladas = [v for v in ventas if v.get('estado') == 'Anulada']
    if not ventas_anuladas:
        print("\nNo hay ventas anuladas registradas.")
    else:
        print("\nVentas Anuladas:")
        for venta in ventas_anuladas:
            cliente = next((c for c in clientes if c['id'] == venta.get('cliente_id')), None)
            destino = next((d for d in destinos if d['id'] == venta.get('destino_id')), None)
            print(f"ID Venta: {venta['id']}")
            print("Datos del Cliente:")
            if cliente:
                print(f"ID: {cliente['id']}")
                print(f"Razón Social: {cliente['razon_social']}")
                print(f"Email: {cliente['email']}")
            else:
                print("Cliente no encontrado")
            print("Datos del Destino:")
            if destino:
                print(f"Nombre: {destino['nombre']}")
                print(f"Costo Base: ${destino['costo_base']}")
            else:
                print("Destino no encontrado")
            print(f"Fecha: {venta.get('fecha', 'N/A')}")
            print(f"Monto: ${venta.get('monto', 'N/A')}")
            print(f"Estado: {venta.get('estado', 'N/A')}")
            print("-" * 50)

#---------------------------------------- Funciones para Reporte General ----------------------------------------
def resumen_ventas():
    total_ventas = sum(1 for v in ventas if v.get('estado', 'Activa') == 'Activa')
    total_monto = sum(v.get('monto', 0) for v in ventas if v.get('estado', 'Activa') == 'Activa')
    print("\n--- Resumen de Ventas ---")
    print(f"Total de ventas activas: {total_ventas}")
    print(f"Monto total vendido: ${total_monto}")
    fechas = []
    for v in ventas:
        if 'fecha' in v:
            fecha = v['fecha'][:10]
            if fecha not in fechas:
                fechas.append(fecha)
    if fechas:
        fechas.sort()
        print(f"Fechas de ventas registradas: {', '.join(fechas)}")
    print()

def destinos_mas_vendidos():
    ventas_activas = [v for v in ventas if v.get('estado', 'Activa') == 'Activa']
    if not ventas_activas:
        print("\nNo hay ventas activas registradas.")
        return
    conteo = {}
    for v in ventas_activas:
        destino_id = v['destino_id']
        conteo[destino_id] = conteo.get(destino_id, 0) + 1
    print("\n--- Destinos más vendidos ---")
    # Ordenar manualmente por cantidad descendente
    for destino_id, cantidad in sorted(conteo.items(), key=lambda x: x[1], reverse=True):
        destino = next((d for d in destinos if d['id'] == destino_id), None)
        nombre = destino['nombre'] if destino else 'Desconocido'
        print(f"{nombre}: {cantidad} ventas")
    print()

def clientes_frecuentes():
    ventas_activas = [v for v in ventas if v.get('estado', 'Activa') == 'Activa']
    if not ventas_activas:
        print("\nNo hay ventas activas registradas.")
        return
    conteo = {}
    for v in ventas_activas:
        cliente_id = v['cliente_id']
        conteo[cliente_id] = conteo.get(cliente_id, 0) + 1
    print("\n--- Clientes frecuentes ---")
    # Ordenar manualmente por cantidad descendente
    for cliente_id, cantidad in sorted(conteo.items(), key=lambda x: x[1], reverse=True):
        cliente = next((c for c in clientes if c['id'] == cliente_id), None)
        nombre = cliente['razon_social'] if cliente else 'Desconocido'
        print(f"{nombre}: {cantidad} compras")
    print()

def menu_principal_loop():
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
        while True:
            opcion = input("\nSeleccione una opción (1-8): ")
            if opcion.isdigit() and 1 <= int(opcion) <= 8:
                opcion = int(opcion)
                break
            print("Entrada no válida, intente nuevamente")
        # Procesamiento de la opción seleccionada
        if opcion == 1:
            while True:
                print("\n--- Gestionar Clientes ---")
                for i in range(len(submenu_gestion)):
                    print(f"{i + 1}. {submenu_gestion[i]}")
                while True:
                    subopcion = input("\nSeleccione una opción (1-5): ")
                    if subopcion.isdigit() and 1 <= int(subopcion) <= 5:
                        subopcion = int(subopcion)
                        break
                    print("Entrada no válida, intente nuevamente")
                if subopcion == 1:
                    ver_clientes()
                elif subopcion == 2:
                    agregar_cliente()
                elif subopcion == 3:
                    modificar_cliente()
                elif subopcion == 4:
                    eliminar_cliente()
                elif subopcion == 5:
                    break
                input("\nPresione Enter para continuar...")
        elif opcion == 2:
            while True:
                print("\n--- Gestionar Destinos ---")
                for i in range(len(submenu_gestion)):
                    print(f"{i + 1}. {submenu_gestion[i]}")
                while True:
                    subopcion = input("\nSeleccione una opción (1-5): ")
                    if subopcion.isdigit() and 1 <= int(subopcion) <= 5:
                        subopcion = int(subopcion)
                        break
                    print("Entrada no válida, intente nuevamente")
                if subopcion == 1:
                    ver_destinos()
                elif subopcion == 2:
                    agregar_destino()
                elif subopcion == 3:
                    modificar_destino()
                elif subopcion == 4:
                    eliminar_destino()
                elif subopcion == 5:
                    break
                input("\nPresione Enter para continuar...")
        elif opcion == 3:
            while True:
                print("\n--- Gestionar Ventas ---")
                for i in range(len(submenu_gestion)):
                    print(f"{i + 1}. {submenu_gestion[i]}")
                while True:
                    subopcion = input("\nSeleccione una opción (1-5): ")
                    if subopcion.isdigit() and 1 <= int(subopcion) <= 5:
                        subopcion = int(subopcion)
                        break
                    print("Entrada no válida, intente nuevamente")
                if subopcion == 1:
                    ver_ventas()
                elif subopcion == 2:
                    agregar_venta()
                elif subopcion == 3:
                    modificar_venta()
                elif subopcion == 4:
                    eliminar_venta()
                elif subopcion == 5:
                    break
                input("\nPresione Enter para continuar...")
        elif opcion == 4:
            while True:
                print("\n--- Consultar Ventas ---")
                for i in range(len(submenu_consulta)):
                    print(f"{i + 1}. {submenu_consulta[i]}")
                while True:
                    subopcion = input("\nSeleccione una opción (1-5): ")
                    if subopcion.isdigit() and 1 <= int(subopcion) <= 5:
                        subopcion = int(subopcion)
                        break
                    print("Entrada no válida, intente nuevamente")
                if subopcion == 1:
                    ventas_del_dia()
                elif subopcion == 2:
                    ventas_ultima_semana()
                elif subopcion == 3:
                    ventas_por_cliente()
                elif subopcion == 4:
                    ver_ventas_anuladas()
                elif subopcion == 5:
                    break
                input("\nPresione Enter para continuar...")
        elif opcion == 5:
            boton_arrepentimiento()
            input("\nPresione Enter para continuar...")
        elif opcion == 6:
            while True:
                print("\n--- Reporte General ---")
                for i in range(len(submenu_reporte)):
                    print(f"{i + 1}. {submenu_reporte[i]}")
                while True:
                    subopcion = input("\nSeleccione una opción (1-4): ")
                    if subopcion.isdigit() and 1 <= int(subopcion) <= 4:
                        subopcion = int(subopcion)
                        break
                    print("Entrada no válida, intente nuevamente")
                if subopcion == 1:
                    resumen_ventas()
                elif subopcion == 2:
                    destinos_mas_vendidos()
                elif subopcion == 3:
                    clientes_frecuentes()
                elif subopcion == 4:
                    break
                input("\nPresione Enter para continuar...")
        elif opcion == 7:
            print("-" * 20)
            print("\n-- ACERCA DEL SISTEMA --")
            print("\nSKYROUTE - Sistema de Gestion de Pasajes v1.0.\n")
            print("Proyecto ABP del modulo programador del ISPC\n")
            print("Integrantes:\n")
            print("Enrico Munighini, Antonella\t44.194.338")
            print("Marovich, Mikael\t\t41.625.321")
            print("Montiel, Matias\t\t\t42.474.994")
            print("Sanchez, Romina\t\t\t45.348.881")
            print("Villarruel, Tomas\t\t44.896.222")
            print("Año: 2025")
            print("-" * 20)
            input("\nPresione Enter para continuar...")
        elif opcion == 8:
            print("\n¡Gracias por usar Skyroute!\n")
            print("Nos vemos.")
            break

if __name__ == "__main__":
    menu_principal_loop()