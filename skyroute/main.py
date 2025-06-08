# main.py
# Archivo principal con menú de opciones para SkyRoute (versión modular)

from gestion_clientes import ver_clientes, agregar_cliente, modificar_cliente, eliminar_cliente
from gestion_destinos import menu_gestion_destinos
from gestion_ventas import ver_ventas, agregar_venta, boton_arrepentimiento
from conexion_base_datos import obtener_conexion, cerrar_conexion

menu_principal = (
    "Gestionar Clientes",
    "Gestionar Destinos",
    "Gestionar Ventas",
    "Botón de Arrepentimiento",
    "Salir"
)

submenu_gestion = ("Ver", "Agregar", "Modificar", "Eliminar", "Volver al Menú Principal")

def menu_principal_loop():
    conexion = obtener_conexion()
        
    while True:
        print("\n-------------------------------")
        print("Bienvenidos a SkyRoute")
        print("-------------------------------")
        print("\n| Menú Principal |\n")
        for i in range(len(menu_principal)):
            print(f"{i + 1}. {menu_principal[i]}")
        while True:
            opcion = input("\nSeleccione una opción (1-5): ")
            if opcion.isdigit() and 1 <= int(opcion) <= 5:
                opcion = int(opcion)
                break
            print("Entrada no válida, intente nuevamente")
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
                    ver_clientes(conexion)
                elif subopcion == 2:
                    agregar_cliente(conexion)
                elif subopcion == 3:
                    modificar_cliente(conexion)
                elif subopcion == 4:
                    eliminar_cliente(conexion)
                elif subopcion == 5:
                    break
                input("\nPresione Enter para continuar...")
        elif opcion == 2:
            menu_gestion_destinos(conexion)
        elif opcion == 3:
            while True:
                print("\n--- Gestionar Ventas ---")
                print("1. Ver Ventas\n2. Agregar Venta\n3. Volver al Menú Principal")
                subopcion = input("\nSeleccione una opción (1-3): ")
                if subopcion == '1':
                    ver_ventas(conexion)
                elif subopcion == '2':
                    agregar_venta(conexion)
                elif subopcion == '3':
                    break
                else:
                    print("Entrada no válida, intente nuevamente")
                input("\nPresione Enter para continuar...")
        elif opcion == 4:
            boton_arrepentimiento(conexion)
            input("\nPresione Enter para continuar...")
        elif opcion == 5:
            print("\n¡Gracias por usar SkyRoute!")
            break
    cerrar_conexion(conexion)

if __name__ == "__main__":
    menu_principal_loop()
