# gestion_destinos.py
# Funciones para alta, baja, modificación y listado de destinos, países y ciudades
import sys
sys.stdout.reconfigure(encoding='utf-8')

def ver_destinos(conexion):
    cursor = conexion.cursor()
    query = '''
        SELECT d.id_destino, c.nombre, p.nombre, d.costo_base
        FROM destinos d
        JOIN ciudades c ON d.id_ciudad = c.id_ciudad
        JOIN paises p ON c.id_pais = p.id_pais
    '''
    cursor.execute(query)
    destinos = cursor.fetchall()
    if not destinos:
        print("\nNo hay destinos registrados.")
    else:
        print("\nLista de Destinos:")
        for idx, destino in enumerate(destinos, start=1):
            print(f"\nDestino {idx}:")
            print(f"ID: {destino[0]}")
            print(f"Ciudad: {destino[1]}")
            print(f"País: {destino[2]}")
            print(f"Costo Base: ${destino[3]}")
            print("-" * 30)
    cursor.close()

def agregar_destino(conexion):
    print("\n--- Agregar Destino ---\n")
    cursor = conexion.cursor()
    # Mostrar países disponibles
    cursor.execute("SELECT id_pais, nombre FROM paises")
    paises = cursor.fetchall()
    if not paises:
        print("No hay países registrados. Agregue países primero.\n")
        cursor.close()
        return
    print("Países disponibles:")
    print("="*40)
    for p in paises:
        print(f"{p[0]}. {p[1]}")
    print("="*40 + "\n")
    while True:
        try:
            id_pais = int(input("Seleccione el ID del país: "))
            if any(p[0] == id_pais for p in paises):
                break
            print("ID de país no válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    # Mostrar ciudades del país seleccionado
    cursor.execute("SELECT id_ciudad, nombre FROM ciudades WHERE id_pais = %s", (id_pais,))
    ciudades = cursor.fetchall()
    if not ciudades:
        print("No hay ciudades registradas para este país. Agregue ciudades primero.\n")
        cursor.close()
        return
    print("Ciudades disponibles:")
    print("-"*40)
    for c in ciudades:
        print(f"{c[0]}. {c[1]}")
    print("-"*40 + "\n")
    while True:
        try:
            id_ciudad = int(input("Seleccione el ID de la ciudad: "))
            if any(c[0] == id_ciudad for c in ciudades):
                break
            print("ID de ciudad no válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    while True:
        try:
            costo_base = float(input("Ingrese costo base del viaje: $"))
            if costo_base > 0:
                break
            print("El costo base debe ser mayor a 0")
        except ValueError:
            print("Por favor, ingrese un número válido")
    cursor.execute("INSERT INTO destinos (id_ciudad, costo_base) VALUES (%s, %s)", (id_ciudad, costo_base))
    conexion.commit()
    print("\nDestino agregado exitosamente.\n")
    cursor.close()

def modificar_destino(conexion):
    ver_destinos(conexion)
    cursor = conexion.cursor()
    cursor.execute("SELECT id_destino FROM destinos")
    ids = [row[0] for row in cursor.fetchall()]
    if not ids:
        print("\nNo hay destinos para modificar.")
        cursor.close()
        return
    while True:
        try:
            id_sel = int(input("\nIngrese el ID del destino a modificar (0 para cancelar): "))
            if id_sel == 0:
                print("\nOperación cancelada.")
                cursor.close()
                return
            if id_sel in ids:
                break
            print("ID de destino no válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    # Permitir cambiar ciudad y costo base
    cursor.execute("SELECT c.id_pais, d.id_ciudad, d.costo_base FROM destinos d JOIN ciudades c ON d.id_ciudad = c.id_ciudad WHERE d.id_destino = %s", (id_sel,))
    actual = cursor.fetchone()
    id_pais_actual, id_ciudad_actual, costo_base_actual = actual
    # Selección de país
    cursor.execute("SELECT id_pais, nombre FROM paises")
    paises = cursor.fetchall()
    print("Países disponibles:")
    for p in paises:
        print(f"{p[0]}. {p[1]}")
    id_pais = input(f"Seleccione nuevo ID de país (actual {id_pais_actual}, Enter para mantener): ")
    if not id_pais:
        id_pais = id_pais_actual
    else:
        id_pais = int(id_pais)
    # Selección de ciudad
    cursor.execute("SELECT id_ciudad, nombre FROM ciudades WHERE id_pais = %s", (id_pais,))
    ciudades = cursor.fetchall()
    print("Ciudades disponibles:")
    for c in ciudades:
        print(f"{c[0]}. {c[1]}")
    id_ciudad = input(f"Seleccione nuevo ID de ciudad (actual {id_ciudad_actual}, Enter para mantener): ")
    if not id_ciudad:
        id_ciudad = id_ciudad_actual
    else:
        id_ciudad = int(id_ciudad)
    # Costo base
    nuevo_costo = input(f"Ingrese nuevo costo base (actual ${costo_base_actual}, Enter para mantener): $")
    if not nuevo_costo:
        nuevo_costo = costo_base_actual
    else:
        nuevo_costo = float(nuevo_costo)
    cursor.execute("UPDATE destinos SET id_ciudad = %s, costo_base = %s WHERE id_destino = %s", (id_ciudad, nuevo_costo, id_sel))
    conexion.commit()
    print("\nDestino modificado exitosamente.")
    cursor.close()

def eliminar_destino(conexion):
    ver_destinos(conexion)
    cursor = conexion.cursor()
    cursor.execute("SELECT id_destino FROM destinos")
    ids = [row[0] for row in cursor.fetchall()]
    if not ids:
        print("\nNo hay destinos para eliminar.")
        cursor.close()
        return
    while True:
        try:
            id_sel = int(input("\nIngrese el ID del destino a eliminar (0 para cancelar): "))
            if id_sel == 0:
                print("\nOperación cancelada.")
                cursor.close()
                return
            if id_sel in ids:
                break
            print("ID de destino no válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    # Verificar si el destino tiene ventas asociadas
    cursor.execute("SELECT COUNT(*) FROM ventas WHERE id_destino = %s", (id_sel,))
    if cursor.fetchone()[0] > 0:
        print("\nNo se puede eliminar el destino porque tiene ventas asociadas.\nPrimero debe eliminar o anular todas las ventas de ese destino.")
        cursor.close()
        return
    confirmacion = input("\nIngrese 'SI' para confirmar la eliminación: ")
    if confirmacion.upper() == 'SI':
        cursor.execute("DELETE FROM destinos WHERE id_destino = %s", (id_sel,))
        conexion.commit()
        print("\nDestino eliminado exitosamente.")
    else:
        print("\nOperación cancelada.")
    cursor.close()

def agregar_pais(conexion):
    print("\n--- Agregar País ---\n")
    while True:
        nombre = input("Ingrese el nombre del país: ").strip()
        if not nombre:
            print("El nombre del país no puede estar vacío.")
            continue
        break
    while True:
        codigo = input("Ingrese el código del país (ej: AR): ").strip()
        if not codigo:
            print("El código del país no puede estar vacío.")
            continue
        break
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO paises (nombre, codigo) VALUES (%s, %s)", (nombre, codigo))
        conexion.commit()
        print("\nPaís agregado exitosamente.\n")
    except Exception as e:
        print(f"\nError al agregar país: {e}\n")
    cursor.close()

def listar_paises(conexion):
    print("\n--- Lista de Países ---\n")
    cursor = conexion.cursor()
    cursor.execute("SELECT id_pais, nombre, codigo FROM paises")
    paises = cursor.fetchall()
    if not paises:
        print("No hay países registrados.\n")
    else:
        print("="*40)
        for p in paises:
            print(f"ID: {p[0]} | Nombre: {p[1]} | Código: {p[2]}")
            print("-"*40)
        print("="*40)
    cursor.close()

def modificar_pais(conexion):
    listar_paises(conexion)
    cursor = conexion.cursor()
    cursor.execute("SELECT id_pais FROM paises")
    ids = [row[0] for row in cursor.fetchall()]
    if not ids:
        print("No hay países para modificar.\n")
        cursor.close()
        return
    try:
        id_sel = int(input("\nIngrese el ID del país a modificar (0 para cancelar): "))
        if id_sel == 0:
            print("\nOperación cancelada.\n")
            cursor.close()
            return
        if id_sel not in ids:
            print("ID de país no válido.\n")
            cursor.close()
            return
        nuevo_nombre = input("Ingrese nuevo nombre (Enter para mantener): ")
        nuevo_codigo = input("Ingrese nuevo código (Enter para mantener): ")
        if nuevo_nombre:
            cursor.execute("UPDATE paises SET nombre = %s WHERE id_pais = %s", (nuevo_nombre, id_sel))
        if nuevo_codigo:
            cursor.execute("UPDATE paises SET codigo = %s WHERE id_pais = %s", (nuevo_codigo, id_sel))
        conexion.commit()
        print("\nPaís modificado exitosamente.\n")
    except Exception as e:
        print(f"Error: {e}")
    cursor.close()

def eliminar_pais(conexion):
    listar_paises(conexion)
    cursor = conexion.cursor()
    cursor.execute("SELECT id_pais FROM paises")
    ids = [row[0] for row in cursor.fetchall()]
    if not ids:
        print("No hay países para eliminar.\n")
        cursor.close()
        return
    try:
        id_sel = int(input("\nIngrese el ID del país a eliminar (0 para cancelar): "))
        if id_sel == 0:
            print("\nOperación cancelada.\n")
            cursor.close()
            return
        # Verificar si tiene ciudades asociadas
        cursor.execute("SELECT COUNT(*) FROM ciudades WHERE id_pais = %s", (id_sel,))
        if cursor.fetchone()[0] > 0:
            print("\nNo se puede eliminar el país porque tiene ciudades asociadas.\n")
            cursor.close()
            return
        confirmacion = input("Ingrese 'SI' para confirmar la eliminación: ")
        if confirmacion.upper() == 'SI':
            cursor.execute("DELETE FROM paises WHERE id_pais = %s", (id_sel,))
            conexion.commit()
            print("\nPaís eliminado exitosamente.\n")
        else:
            print("\nOperación cancelada.\n")
    except Exception as e:
        print(f"Error: {e}")
    cursor.close()

def agregar_ciudad(conexion):
    print("\n--- Agregar Ciudad ---\n")
    listar_paises(conexion)
    try:
        id_pais = int(input("Ingrese el ID del país al que pertenece la ciudad: "))
    except ValueError:
        print("ID de país no válido.\n")
        return
    while True:
        nombre = input("Ingrese el nombre de la ciudad: ").strip()
        if not nombre:
            print("El nombre de la ciudad no puede estar vacío.")
            continue
        break
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO ciudades (nombre, id_pais) VALUES (%s, %s)", (nombre, id_pais))
        conexion.commit()
        print("\nCiudad agregada exitosamente.\n")
    except Exception as e:
        print(f"\nError al agregar ciudad: {e}\n")
    cursor.close()

def listar_ciudades(conexion):
    print("\n--- Lista de Ciudades ---\n")
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT ciu.id_ciudad, ciu.nombre, p.nombre 
        FROM ciudades ciu 
        JOIN paises p ON ciu.id_pais = p.id_pais
        ORDER BY p.nombre ASC, ciu.nombre ASC
    """)
    ciudades = cursor.fetchall()
    if not ciudades:
        print("No hay ciudades registradas.\n")
    else:
        pais_actual = None
        print("="*40)
        for c in ciudades:
            if c[2] != pais_actual:
                print(f"\n=== {c[2].upper()} ===")
                pais_actual = c[2]
            print(f"ID: {c[0]} | Ciudad: {c[1]}")
            print("-"*40)
        print("="*40)
        print()
    cursor.close()

def modificar_ciudad(conexion):
    listar_ciudades(conexion)
    cursor = conexion.cursor()
    cursor.execute("SELECT id_ciudad FROM ciudades")
    ids = [row[0] for row in cursor.fetchall()]
    if not ids:
        print("No hay ciudades para modificar.\n")
        cursor.close()
        return
    try:
        id_sel = int(input("\nIngrese el ID de la ciudad a modificar (0 para cancelar): "))
        if id_sel == 0:
            print("\nOperación cancelada.\n")
            cursor.close()
            return
        if id_sel not in ids:
            print("ID de ciudad no válido.\n")
            cursor.close()
            return
        nuevo_nombre = input("Ingrese nuevo nombre (Enter para mantener): ")
        listar_paises(conexion)
        nuevo_id_pais = input("Ingrese nuevo ID de país (Enter para mantener): ")
        if nuevo_nombre:
            cursor.execute("UPDATE ciudades SET nombre = %s WHERE id_ciudad = %s", (nuevo_nombre, id_sel))
        if nuevo_id_pais:
            cursor.execute("UPDATE ciudades SET id_pais = %s WHERE id_ciudad = %s", (int(nuevo_id_pais), id_sel))
        conexion.commit()
        print("\nCiudad modificada exitosamente.\n")
    except Exception as e:
        print(f"Error: {e}")
    cursor.close()

def eliminar_ciudad(conexion):
    listar_ciudades(conexion)
    cursor = conexion.cursor()
    cursor.execute("SELECT id_ciudad FROM ciudades")
    ids = [row[0] for row in cursor.fetchall()]
    if not ids:
        print("No hay ciudades para eliminar.\n")
        cursor.close()
        return
    try:
        id_sel = int(input("\nIngrese el ID de la ciudad a eliminar (0 para cancelar): "))
        if id_sel == 0:
            print("\nOperación cancelada.\n")
            cursor.close()
            return
        # Verificar si tiene destinos asociados
        cursor.execute("SELECT COUNT(*) FROM destinos WHERE id_ciudad = %s", (id_sel,))
        if cursor.fetchone()[0] > 0:
            print("\nNo se puede eliminar la ciudad porque tiene destinos asociados.\n")
            cursor.close()
            return
        confirmacion = input("Ingrese 'SI' para confirmar la eliminación: ")
        if confirmacion.upper() == 'SI':
            cursor.execute("DELETE FROM ciudades WHERE id_ciudad = %s", (id_sel,))
            conexion.commit()
            print("\nCiudad eliminada exitosamente.\n")
        else:
            print("\nOperación cancelada.\n")
    except Exception as e:
        print(f"Error: {e}")
    cursor.close()

def menu_gestion_destinos(conexion):
    while True:
        print("\n--- Gestión de Destinos y Geografía ---\n")
        print("1. Listar destinos")
        print("2. Agregar destino")
        print("3. Modificar destino")
        print("4. Eliminar destino")
        print("5. Gestión de países")
        print("6. Gestión de ciudades")
        print("7. Volver al menú principal\n")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            ver_destinos(conexion)
        elif opcion == '2':
            agregar_destino(conexion)
        elif opcion == '3':
            modificar_destino(conexion)
        elif opcion == '4':
            eliminar_destino(conexion)
        elif opcion == '5':
            menu_gestion_paises(conexion)
        elif opcion == '6':
            menu_gestion_ciudades(conexion)
        elif opcion == '7':
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")
        input("\nPresione Enter para continuar...")

def menu_gestion_paises(conexion):
    while True:
        print("\n--- Gestión de Países ---\n")
        print("1. Listar países")
        print("2. Agregar país")
        print("3. Modificar país")
        print("4. Eliminar país")
        print("5. Volver\n")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            listar_paises(conexion)
        elif opcion == '2':
            agregar_pais(conexion)
        elif opcion == '3':
            modificar_pais(conexion)
        elif opcion == '4':
            eliminar_pais(conexion)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")
        input("\nPresione Enter para continuar...")

def menu_gestion_ciudades(conexion):
    while True:
        print("\n--- Gestión de Ciudades ---\n")
        print("1. Listar ciudades")
        print("2. Agregar ciudad")
        print("3. Modificar ciudad")
        print("4. Eliminar ciudad")
        print("5. Volver\n")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            listar_ciudades(conexion)
        elif opcion == '2':
            agregar_ciudad(conexion)
        elif opcion == '3':
            modificar_ciudad(conexion)
        elif opcion == '4':
            eliminar_ciudad(conexion)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")
        input("\nPresione Enter para continuar...")
