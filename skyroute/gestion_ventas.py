# gestion_ventas.py
# Funciones para registrar ventas y botón de arrepentimiento

from datetime import datetime, timedelta

# Se espera que clientes y destinos sean importados o pasados como argumentos en una integración futura

def ver_ventas(conexion):
    cursor = conexion.cursor()
    query = '''
        SELECT v.id_venta, v.fecha, v.estado, v.monto, v.fecha_anulacion,
               c.razon_social, c.cuit, c.email,
               d.id_destino, ciu.nombre, p.nombre
        FROM ventas v
        JOIN clientes c ON v.id_cliente = c.id_cliente
        JOIN destinos d ON v.id_destino = d.id_destino
        JOIN ciudades ciu ON d.id_ciudad = ciu.id_ciudad
        JOIN paises p ON ciu.id_pais = p.id_pais
        ORDER BY v.id_venta
    '''
    cursor.execute(query)
    ventas = cursor.fetchall()
    if not ventas:
        print("\nNo hay ventas registradas.")
    else:
        print("\nLista de Ventas:")
        for venta in ventas:
            print(f"\nVenta ID: {venta[0]}")
            print(f"Fecha: {venta[1]}")
            print(f"Estado: {venta[2]}")
            print(f"Monto: ${venta[3]}")
            if venta[4]:
                print(f"Fecha de anulación: {venta[4]}")
            print("\nDatos del Cliente:")
            print(f"Razón Social: {venta[5]}")
            print(f"CUIT: {venta[6]}")
            print(f"Email: {venta[7]}")
            print("\nDatos del Destino:")
            print(f"Ciudad: {venta[9]}")
            print(f"País: {venta[10]}")
            print("-" * 50)
    cursor.close()

def agregar_venta(conexion):
    print("\n--- Agregar Venta ---\n")
    cursor = conexion.cursor()
    # Mostrar clientes
    cursor.execute("SELECT id_cliente, razon_social, cuit FROM clientes")
    clientes = cursor.fetchall()
    if not clientes:
        print("No hay clientes registrados.\n")
        cursor.close()
        return
    print("Clientes disponibles:\n")
    for c in clientes:
        print(f"ID: {c[0]} | Razón Social: {c[1]} | CUIT: {c[2]}")
    print()
    while True:
        try:
            cliente_id = int(input("Ingrese el ID del cliente: "))
            if any(c[0] == cliente_id for c in clientes):
                break
            print("ID de cliente no válido.\n")
        except ValueError:
            print("Por favor, ingrese un número válido.\n")
    print()
    # Mostrar destinos
    cursor.execute('''
        SELECT d.id_destino, ciu.nombre, p.nombre, d.costo_base
        FROM destinos d
        JOIN ciudades ciu ON d.id_ciudad = ciu.id_ciudad
        JOIN paises p ON ciu.id_pais = p.id_pais
    ''')
    destinos = cursor.fetchall()
    if not destinos:
        print("No hay destinos registrados.\n")
        cursor.close()
        return
    print("Destinos disponibles:\n")
    for d in destinos:
        print(f"ID: {d[0]} | Ciudad: {d[1]} | País: {d[2]} | Costo Base: ${d[3]:.2f}")
    print()
    while True:
        try:
            destino_id = int(input("Ingrese el ID del destino: "))
            destino = next((d for d in destinos if d[0] == destino_id), None)
            if destino:
                break
            print("ID de destino no válido.\n")
        except ValueError:
            print("Por favor, ingrese un número válido.\n")
    print()
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO ventas (id_cliente, id_destino, fecha, estado, monto) VALUES (%s, %s, %s, 'Activa', %s)",
        (cliente_id, destino_id, fecha_actual, destino[3])
    )
    conexion.commit()
    print("\nVenta agregada exitosamente.\n")
    cursor.close()

def boton_arrepentimiento(conexion):
    cursor = conexion.cursor()
    ahora = datetime.now()
    # Solo ventas activas de los últimos 5 minutos
    cursor.execute('''
        SELECT v.id_venta, v.fecha, v.estado, v.monto, c.razon_social, ciu.nombre, p.nombre
        FROM ventas v
        JOIN clientes c ON v.id_cliente = c.id_cliente
        JOIN destinos d ON v.id_destino = d.id_destino
        JOIN ciudades ciu ON d.id_ciudad = ciu.id_ciudad
        JOIN paises p ON ciu.id_pais = p.id_pais
        WHERE v.estado = 'Activa'
    ''')
    ventas_activas = cursor.fetchall()
    ventas_recientes = []
    for v in ventas_activas:
        fecha_venta = datetime.strptime(str(v[1]), "%Y-%m-%d %H:%M:%S")
        if ahora - fecha_venta <= timedelta(minutes=5):
            ventas_recientes.append(v)
    if not ventas_recientes:
        print("\nNo hay ventas recientes para anular.\n")
        cursor.close()
        return
    print("\nVentas recientes (últimos 5 minutos):\n")
    for v in ventas_recientes:
        print(f"ID Venta: {v[0]} | Fecha: {v[1]} | Cliente: {v[4]} | Ciudad: {v[5]} | País: {v[6]} | Monto: ${v[3]}")
    while True:
        try:
            venta_id = int(input("\nIngrese el ID de la venta a anular (0 para cancelar): "))
            if venta_id == 0:
                print("\nOperación cancelada.\n")
                cursor.close()
                return
            venta = next((v for v in ventas_recientes if v[0] == venta_id), None)
            if not venta:
                print("ID de venta no válido o no reciente.")
                continue
            confirmacion = input("\nIngrese 'SI' para confirmar la anulación: ")
            if confirmacion.upper() == 'SI':
                fecha_anulacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute("UPDATE ventas SET estado = 'Anulada', fecha_anulacion = %s WHERE id_venta = %s", (fecha_anulacion, venta_id))
                conexion.commit()
                print("\nVenta anulada exitosamente.")
                print(f"Fecha y hora de anulación: {fecha_anulacion}")
            else:
                print("\nOperación cancelada.")
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    cursor.close()
