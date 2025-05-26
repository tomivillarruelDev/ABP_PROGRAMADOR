def validar_cuit():
    while True:
        cuit = input("Ingresar CUIT de la empresa: ")
        if cuit.isdigit() and len(cuit) == 11:
            return cuit
        print("Debe ingresar un CUIT válido de 11 dígitos.")


def validar_correo():
    while True:
        correo = input("Ingresar correo de la empresa: ")
        if '@' in correo and '.' in correo:
            return correo
        print("Correo inválido. Intente nuevamente.")


def ingresar_clientes(clientes, cantidad):
    for i in range(cantidad):
        print(f"\nCargando datos de la empresa #{i + 1}:")
        razon_social = input("Ingresar razón social: ")
        cuit = validar_cuit()
        correo = validar_correo()

        cliente = {
            "razon_social": razon_social,
            "cuit": cuit,
            "correo": correo
        }
        clientes.append(cliente)


def mostrar_clientes(clientes):
    if not clientes:
        print("No hay datos de clientes.")
        return
    print("\nListado de Clientes:")
    for i, cliente in enumerate(clientes, start=1):
        print(f"\nCliente #{i}")
        print(f"Razón social: {cliente['razon_social']}")
        print(f"CUIT: {cliente['cuit']}")
        print(f"Correo: {cliente['correo']}")
        print("-" * 30)


def modificar_cliente(clientes):
    mostrar_clientes(clientes)
    if not clientes:
        return

    try:
        index = int(input("¿Qué cliente desea modificar? (Número): ")) - 1
        if not (0 <= index < len(clientes)):
            print("Número de cliente inválido.")
            return

        cliente = clientes[index]
        print("\nSeleccione qué desea modificar:")
        print("1 - Razón social")
        print("2 - CUIT")
        print("3 - Correo")
        print("4 - Cancelar")
        opcion = input("Opción: ")

        if opcion == "1":
            cliente["razon_social"] = input("Nueva razón social: ")
        elif opcion == "2":
            cliente["cuit"] = validar_cuit()
        elif opcion == "3":
            cliente["correo"] = validar_correo()
        elif opcion == "4":
            print("Modificación cancelada.")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Debe ingresar un número válido.")


def eliminar_cliente(clientes):
    mostrar_clientes(clientes)
    if not clientes:
        return

    try:
        index = int(input("¿Qué cliente desea eliminar? (Número): ")) - 1
        if not (0 <= index < len(clientes)):
            print("Número de cliente inválido.")
            return

        eliminado = clientes.pop(index)
        print(f"Cliente '{eliminado['razon_social']}' eliminado correctamente.")
    except ValueError:
        print("Debe ingresar un número válido.")


def menu_clientes(clientes):
    while True:
        print("\n=== Gestión de Clientes ===")
        print("1. Ver clientes")
        print("2. Agregar cliente")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_clientes(clientes)
        elif opcion == "2":
            try:
                cantidad = int(input("¿Cuántos clientes desea ingresar?: "))
                ingresar_clientes(clientes, cantidad)
            except ValueError:
                print("Debe ingresar un número.")
        elif opcion == "3":
            modificar_cliente(clientes)
        elif opcion == "4":
            eliminar_cliente(clientes)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")


def mostrar_menu_principal():
    print("\n=== Menú Principal ===")
    print("1. Gestión de Clientes")
    print("2. Gestión de Destinos (en desarrollo)")
    print("3. Salir")


def main():
    clientes = []
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_clientes(clientes)
        elif opcion == "2":
            print("Funcionalidad de destinos aún no implementada.")
        elif opcion == "3":
            print("¡Gracias por usar SkyRoute!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
