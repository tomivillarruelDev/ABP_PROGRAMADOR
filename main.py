def mostrar_menu_principal():
    print("\nBienvenidos a SkyRoute - Sistema de Gestión de Pasajes")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Ventas")
    print("4. Consultar Ventas")
    print("5. Botón de Arrepentimiento")
    print("6. Ver Reporte General")
    print("7. Acerca del Sistema")
    print("8. Salir")

# Lista de usuarios en memoria
usuarios = [
    {"id": 1, "nombre": "Juan Pérez", "dni": "12345678", "email": "juan@mail.com"},
    {"id": 2, "nombre": "Ana Gómez", "dni": "87654321", "email": "ana@mail.com"},
    {"id": 3, "nombre": "Carlos Ruiz", "dni": "11223344", "email": "carlos@mail.com"}
]

# Lista de destinos en memoria)
destinos = [
    {"id": 1, "nombre": "Buenos Aires"},
    {"id": 2, "nombre": "Córdoba"},
    {"id": 3, "nombre": "Mendoza"},
    {"id": 4, "nombre": "Bariloche"}
]

# Lista de ventas en memoria
ventas = [
    {"id": 1, "usuario_id": 1, "destino_id": 2},
    {"id": 2, "usuario_id": 2, "destino_id": 1},
    {"id": 3, "usuario_id": 1, "destino_id": 3},
    {"id": 4, "usuario_id": 3, "destino_id": 4},
    {"id": 5, "usuario_id": 2, "destino_id": 3}
]

def generar_id(lista):
    if not lista:
        return 1
    return max(item["id"] for item in lista) + 1

def ver_clientes():
    print("\nLista de clientes:")
    for usuario in usuarios:
        print(f"ID: {usuario['id']} | Nombre: {usuario['nombre']} | DNI: {usuario['dni']} | Email: {usuario['email']}")
    print()

def agregar_cliente():
    nombre = input("Ingrese nombre: ")
    dni = input("Ingrese DNI: ")
    email = input("Ingrese email: ")
    nuevo_id = generar_id(usuarios)
    usuarios.append({"id": nuevo_id, "nombre": nombre, "dni": dni, "email": email})
    print(f"Cliente agregado exitosamente: ID {nuevo_id} | Nombre: {nombre} | DNI: {dni} | Email: {email}\n")

def modificar_cliente():
    id_mod = int(input("Ingrese el ID del cliente a modificar: "))
    usuario = next((u for u in usuarios if u["id"] == id_mod), None)
    if usuario:
        nombre_anterior = usuario["nombre"]
        dni_anterior = usuario["dni"]
        email_anterior = usuario["email"]
        usuario["nombre"] = input(f"Nuevo nombre ({usuario['nombre']}): ") or usuario["nombre"]
        usuario["dni"] = input(f"Nuevo DNI ({usuario['dni']}): ") or usuario["dni"]
        usuario["email"] = input(f"Nuevo email ({usuario['email']}): ") or usuario["email"]
        print(f"Cliente modificado exitosamente: ID {id_mod} | Nombre: {nombre_anterior} -> {usuario['nombre']} | DNI: {dni_anterior} -> {usuario['dni']} | Email: {email_anterior} -> {usuario['email']}\n")
    else:
        print("ID no encontrado.\n")

def eliminar_cliente():
    id_del = int(input("Ingrese el ID del cliente a eliminar: "))
    for i, usuario in enumerate(usuarios):
        if usuario["id"] == id_del:
            usuarios.pop(i)
            print("Cliente eliminado exitosamente.\n")
            return
    print("ID no encontrado.\n")

def ver_destinos():
    print("\nLista de destinos:")
    for destino in destinos:
        print(f"ID: {destino['id']} | Nombre: {destino['nombre']}")
    print()

def agregar_destino():
    nombre = input("Ingrese nombre del destino: ")
    nuevo_id = generar_id(destinos)
    destinos.append({"id": nuevo_id, "nombre": nombre})
    print(f"Destino agregado exitosamente: ID {nuevo_id} | Nombre: {nombre}\n")

def modificar_destino():
    id_mod = int(input("Ingrese el ID del destino a modificar: "))
    destino = next((d for d in destinos if d["id"] == id_mod), None)
    if destino:
        nombre_anterior = destino["nombre"]
        destino["nombre"] = input(f"Nuevo nombre ({destino['nombre']}): ") or destino["nombre"]
        print(f"Destino modificado exitosamente: ID {id_mod} | Nombre: {nombre_anterior} -> {destino['nombre']}\n")
    else:
        print("ID no encontrado.\n")

def eliminar_destino():
    id_del = int(input("Ingrese el ID del destino a eliminar: "))
    for i, destino in enumerate(destinos):
        if destino["id"] == id_del:
            destinos.pop(i)
            print("Destino eliminado exitosamente.\n")
            return
    print("ID no encontrado.\n")

def ver_ventas():
    print("\nLista de ventas:")
    for venta in ventas:
        usuario = buscar_usuario_por_id(venta["usuario_id"])
        destino = buscar_destino_por_id(venta["destino_id"])
        print(f"ID Venta: {venta['id']} | Cliente: {usuario['nombre'] if usuario else 'Desconocido'} | Destino: {destino['nombre'] if destino else 'Desconocido'}")
    print()

def agregar_venta():
    print("Seleccione el cliente por ID:")
    for usuario in usuarios:
        print(f"ID: {usuario['id']} | Nombre: {usuario['nombre']}")
    usuario_id = int(input("ID de cliente: "))
    print("Seleccione el destino por ID:")
    for destino in destinos:
        print(f"ID: {destino['id']} | Nombre: {destino['nombre']}")
    destino_id = int(input("ID de destino: "))
    nuevo_id = generar_id(ventas)
    ventas.append({"id": nuevo_id, "usuario_id": usuario_id, "destino_id": destino_id})
    print(f"Venta registrada exitosamente: ID {nuevo_id} | Cliente ID: {usuario_id} | Destino ID: {destino_id}\n")

def modificar_venta():
    id_mod = int(input("Ingrese el ID de la venta a modificar: "))
    venta = next((v for v in ventas if v["id"] == id_mod), None)
    if venta:
        usuario_id_anterior = venta["usuario_id"]
        destino_id_anterior = venta["destino_id"]
        print("Seleccione el nuevo cliente por ID:")
        for usuario in usuarios:
            print(f"ID: {usuario['id']} | Nombre: {usuario['nombre']}")
        usuario_id = input(f"ID de cliente actual ({venta['usuario_id']}): ")
        if usuario_id:
            venta['usuario_id'] = int(usuario_id)
        print("Seleccione el nuevo destino por ID:")
        for destino in destinos:
            print(f"ID: {destino['id']} | Nombre: {destino['nombre']}")
        destino_id = input(f"ID de destino actual ({venta['destino_id']}): ")
        if destino_id:
            venta['destino_id'] = int(destino_id)
        print(f"Venta modificada exitosamente: ID {id_mod} | Cliente ID: {usuario_id_anterior} -> {venta['usuario_id']} | Destino ID: {destino_id_anterior} -> {venta['destino_id']}\n")
    else:
        print("ID no encontrado.\n")

def eliminar_venta():
    id_del = int(input("Ingrese el ID de la venta a eliminar: "))
    for i, venta in enumerate(ventas):
        if venta["id"] == id_del:
            ventas.pop(i)
            print(f"Venta eliminada exitosamente: ID {id_del}\n")
            return
    print("ID no encontrado.\n")

def menu_gestionar_clientes():
    while True:
        print("\n-- GESTIONAR CLIENTES --")
        print("1. Ver Clientes")
        print("2. Agregar Cliente")
        print("3. Modificar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción y presione Enter: ")
        if opcion == "1":
            ver_clientes()
        elif opcion == "2":
            agregar_cliente()
        elif opcion == "3":
            modificar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            print()  # Espacio antes de volver al menú principal
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")

def menu_gestionar_destinos():
    while True:
        print("\n-- GESTIONAR DESTINOS --")
        print("1. Ver Destinos")
        print("2. Agregar Destino")
        print("3. Modificar Destino")
        print("4. Eliminar Destino")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción y presione Enter: ")
        if opcion == "1":
            ver_destinos()
        elif opcion == "2":
            agregar_destino()
        elif opcion == "3":
            modificar_destino()
        elif opcion == "4":
            eliminar_destino()
        elif opcion == "5":
            print()
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")

def menu_gestionar_ventas():
    while True:
        print("\n-- GESTIONAR VENTAS --")
        print("1. Ver Ventas")
        print("2. Agregar Venta")
        print("3. Modificar Venta")
        print("4. Eliminar Venta")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción y presione Enter: ")
        if opcion == "1":
            ver_ventas()
        elif opcion == "2":
            agregar_venta()
        elif opcion == "3":
            modificar_venta()
        elif opcion == "4":
            eliminar_venta()
        elif opcion == "5":
            print()
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")

def consultar_ventas_por_cliente():
    ver_clientes()
    id_cliente = int(input("Ingrese el ID del cliente para ver sus ventas: "))
    ventas_cliente = [v for v in ventas if v["usuario_id"] == id_cliente]
    if ventas_cliente:
        print(f"\nVentas del cliente ID {id_cliente}:")
        for venta in ventas_cliente:
            destino = buscar_destino_por_id(venta["destino_id"])
            print(f"ID Venta: {venta['id']} | Destino: {destino['nombre'] if destino else 'Desconocido'}")
    else:
        print("No hay ventas registradas para este cliente.\n")
    print()

def consultar_ventas_por_destino():
    ver_destinos()
    id_destino = int(input("Ingrese el ID del destino para ver sus ventas: "))
    ventas_destino = [v for v in ventas if v["destino_id"] == id_destino]
    if ventas_destino:
        print(f"\nVentas para el destino ID {id_destino}:")
        for venta in ventas_destino:
            usuario = buscar_usuario_por_id(venta["usuario_id"])
            print(f"ID Venta: {venta['id']} | Cliente: {usuario['nombre'] if usuario else 'Desconocido'}")
    else:
        print("No hay ventas registradas para este destino.\n")
    print()

def buscar_usuario_por_id(usuario_id):
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            return usuario
    return None

def buscar_destino_por_id(destino_id):
    for destino in destinos:
        if destino["id"] == destino_id:
            return destino
    return None

def menu_consultar_ventas():
    while True:
        print("\n-- CONSULTAR VENTAS --")
        print("1. Consultar por Cliente")
        print("2. Consultar por Destino")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción y presione Enter: ")
        if opcion == "1":
            consultar_ventas_por_cliente()
        elif opcion == "2":
            consultar_ventas_por_destino()
        elif opcion == "3":
            print()
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_boton_arrepentimiento():
    while True:
        print("\n-- BOTÓN DE ARREPENTIMIENTO --")
        print("1. Cancelar última compra")
        print("2. Consultar estado de cancelación")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción y presione Enter: ")
        if opcion == "3":
            print()
            break
        elif opcion in ["1", "2"]:
            print("Funcionalidad no implementada aún.")
        else:
            print("Opción inválida. Intente nuevamente.")

def resumen_ventas():
    print(f"\nTotal de ventas registradas: {len(ventas)}")
    if ventas:
        fechas = [venta.get('fecha', 'Sin fecha') for venta in ventas]
        print(f"Fechas de ventas registradas: {', '.join(sorted(set(fechas)))}")
    print()

def destinos_mas_vendidos():
    from collections import Counter
    if not ventas:
        print("No hay ventas registradas.\n")
        return
    conteo = Counter([venta['destino_id'] for venta in ventas])
    mas_vendidos = conteo.most_common()
    print("\nDestinos más vendidos:")
    for destino_id, cantidad in mas_vendidos:
        destino = buscar_destino_por_id(destino_id)
        print(f"{destino['nombre'] if destino else 'Desconocido'}: {cantidad} ventas")
    print()

def clientes_frecuentes():
    from collections import Counter
    if not ventas:
        print("No hay ventas registradas.\n")
        return
    conteo = Counter([venta['usuario_id'] for venta in ventas])
    mas_frecuentes = conteo.most_common()
    print("\nClientes frecuentes:")
    for usuario_id, cantidad in mas_frecuentes:
        usuario = buscar_usuario_por_id(usuario_id)
        print(f"{usuario['nombre'] if usuario else 'Desconocido'}: {cantidad} compras")
    print()

def menu_reporte_general():
    while True:
        print("\n-- REPORTE GENERAL --")
        print("1. Ver resumen de ventas")
        print("2. Ver destinos más vendidos")
        print("3. Ver clientes frecuentes")
        print("4. Volver al Menú Principal")
        opcion = input("Seleccione una opción y presione Enter: ")
        if opcion == "1":
            resumen_ventas()
        elif opcion == "2":
            destinos_mas_vendidos()
        elif opcion == "3":
            clientes_frecuentes()
        elif opcion == "4":
            print()
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_acerca_del_sistema():
    print("\n-- ACERCA DEL SISTEMA --")
    print("SkyRoute v1.0 - Sistema de Gestión de Pasajes")
    print("Desarrollado por el equipo de ABP-PROG")
    print("Año: 2025")
    input("Presione Enter para volver al menú principal: ")

def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción y presione Enter: ")
        if opcion == "1":
            menu_gestionar_clientes()
        elif opcion == "2":
            menu_gestionar_destinos()
        elif opcion == "3":
            menu_gestionar_ventas()
        elif opcion == "4":
            menu_consultar_ventas()
        elif opcion == "5":
            menu_boton_arrepentimiento()
        elif opcion == "6":
            menu_reporte_general()
        elif opcion == "7":
            menu_acerca_del_sistema()
        elif opcion == "8":
            print("¡Gracias por usar SkyRoute!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()