# gestion_clientes.py
# Funciones para alta, baja, modificación y listado de clientes

def generar_id(lista):
    if not lista:
        return 1
    return max(item["id"] for item in lista) + 1

def ver_clientes(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT id, razon_social, cuit, email FROM clientes")
    clientes = cursor.fetchall()
    if not clientes:
        print("\nNo hay clientes registrados.")
    else:
        print("\nLista de Clientes:")
        for idx, cliente in enumerate(clientes, start=1):
            print(f"\nCliente {idx}:")
            print(f"ID: {cliente[0]}")
            print(f"Razón Social: {cliente[1]}")
            print(f"CUIT: {cliente[2]}")
            print(f"Email: {cliente[3]}")
            print("-" * 30)
    cursor.close()

def agregar_cliente(conexion):
    print("\n--- Agregar Cliente ---")
    while True:
        cuit = input("Ingrese CUIT (solo números): ")
        if cuit.isdigit() and len(cuit) == 11:
            cursor = conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM clientes WHERE cuit = %s", (cuit,))
            if cursor.fetchone()[0] > 0:
                print("Este CUIT ya está registrado.")
                cursor.close()
                continue
            cursor.close()
            break
        print("El CUIT debe contener 11 números")
    razon_social = input("Ingrese Razón Social: ")
    while True:
        email = input("Ingrese correo electrónico: ")
        if '@' in email and '.' in email:
            break
        print("Ingrese un correo electrónico válido")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO clientes (razon_social, cuit, email) VALUES (%s, %s, %s)", (razon_social, cuit, email))
    conexion.commit()
    print("\nCliente agregado exitosamente.")
    cursor.close()

def modificar_cliente(conexion):
    ver_clientes(conexion)
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM clientes")
    ids = [row[0] for row in cursor.fetchall()]
    if not ids:
        print("\nNo hay clientes para modificar.")
        cursor.close()
        return
    while True:
        try:
            id_sel = int(input("\nIngrese el ID del cliente a modificar (0 para cancelar): "))
            if id_sel == 0:
                print("\nOperación cancelada.")
                cursor.close()
                return
            if id_sel in ids:
                break
            print("ID de cliente no válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    cursor.execute("SELECT razon_social, cuit, email FROM clientes WHERE id = %s", (id_sel,))
    actual = cursor.fetchone()
    print(f"\nModificando cliente con ID {id_sel}: ")
    print(f"CUIT actual: {actual[1]}")
    print(f"Razón Social actual: {actual[0]}")
    print(f"Email actual: {actual[2]}")
    nuevo_cuit = input("Ingrese nuevo CUIT (Enter para mantener el actual): ")
    if nuevo_cuit:
        if not nuevo_cuit.isdigit() or len(nuevo_cuit) != 11:
            print("El CUIT debe contener 11 números")
        else:
            cursor.execute("SELECT COUNT(*) FROM clientes WHERE cuit = %s AND id != %s", (nuevo_cuit, id_sel))
            if cursor.fetchone()[0] > 0:
                print("Este CUIT ya está registrado para otro cliente")
            else:
                cursor.execute("UPDATE clientes SET cuit = %s WHERE id = %s", (nuevo_cuit, id_sel))
                conexion.commit()
    nueva_razon_social = input("Ingrese nueva Razón Social (Enter para mantener la actual): ")
    if nueva_razon_social:
        cursor.execute("UPDATE clientes SET razon_social = %s WHERE id = %s", (nueva_razon_social, id_sel))
        conexion.commit()
    nuevo_email = input("Ingrese nuevo email (Enter para mantener el actual): ")
    if nuevo_email:
        if '@' in nuevo_email and '.' in nuevo_email:
            cursor.execute("UPDATE clientes SET email = %s WHERE id = %s", (nuevo_email, id_sel))
            conexion.commit()
        else:
            print("Email no válido, se mantiene el actual")
    print("\nCliente modificado exitosamente.")
    cursor.close()

def eliminar_cliente(conexion):
    ver_clientes(conexion)
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM clientes")
    ids = [row[0] for row in cursor.fetchall()]
    if not ids:
        print("\nNo hay clientes para eliminar.")
        cursor.close()
        return
    while True:
        try:
            id_sel = int(input("\nIngrese el ID del cliente a eliminar (0 para cancelar): "))
            if id_sel == 0:
                print("\nOperación cancelada.")
                cursor.close()
                return
            if id_sel in ids:
                break
            print("ID de cliente no válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    # Verificar si el cliente tiene ventas asociadas
    cursor.execute("SELECT COUNT(*) FROM ventas WHERE cliente_id = %s", (id_sel,))
    if cursor.fetchone()[0] > 0:
        print("\nNo se puede eliminar el cliente porque tiene ventas asociadas.\nPrimero debe eliminar o anular todas las ventas del cliente.")
        cursor.close()
        return
    confirmacion = input("\nIngrese 'SI' para confirmar la eliminación: ")
    if confirmacion.upper() == 'SI':
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id_sel,))
        conexion.commit()
        print("\nCliente eliminado exitosamente.")
    else:
        print("\nOperación cancelada.")
    cursor.close()
