# SkyRoute - Sistema de Gestión de Pasajes

## Descripción

SkyRoute es un sistema desarrollado para gestionar clientes, destinos y ventas de pasajes de manera eficiente, ofreciendo funcionalidades para ingresar, modificar, visualizar y eliminar datos a través de una interfaz de consola amigable. El sistema está orientado a facilitar el manejo de información en entornos donde se requiere un control sencillo pero funcional de registros relacionados con servicios o viajes.

## Integrantes del grupo

- Enrico Munighini, Antonella | 44.194.338 | [github.com/MunighiniAnto](https://github.com/MunighiniAnto)
- Marovich, Mikael | 41.625.321 | [github.com/MikiMarovich](https://github.com/MikiMarovich)
- Montiel, Matías | 42.474.994 | [github.com/MatyMontiel](https://github.com/MatyMontiel)
- Sánchez, Romina | 45.348.881 | [github.com/rominasanchez12](https://github.com/rominasanchez12)
- Villarruel, Tomás | 44.896.222 | [github.com/tomivillarruelDev](https://github.com/tomivillarruelDev)

## Instrucciones de ejecución

1. Requisitos previos:
   - Python 3.10 o superior
   - Sistema operativo: Windows, Linux o macOS
   - Instalar el conector de MySQL para Python:
     ```bash
     pip install mysql-connector-python
     ```
3. Navegar a la carpeta `skyroute`.
4. Ejecutar el sistema con:
   ```bash
   python main.py
   ```

## Estructura del repositorio

```
skyroute/
├── init/
   ├──init.sql                # Script SQL para crear la base de datos y tablas
├── config.py                # Configuración de conexión a la base de datos
├── conexion_base_datos.py   # Conexión y operaciones con MySQL
├── gestion_clientes.py      # Alta, baja, modificación, listado de clientes
├── gestion_destinos.py      # Alta, baja, modificación, listado de destinos
├── gestion_ventas.py        # Registrar ventas y botón de arrepentimiento
├── main.py                  # Archivo principal con menú de opciones
├── README.md                # Documentación del proyecto

```

- **config.py**: Configuración de la base de datos (host, usuario, contraseña, nombre de la base).
- **conexion_base_datos.py**: Funciones para conectar y operar con MySQL.
- **gestion_clientes.py**: Funciones para gestionar clientes (alta, baja, modificación, listado).
- **gestion_destinos.py**: Funciones para gestionar destinos (alta, baja, modificación, listado).
- **gestion_ventas.py**: Funciones para registrar ventas y anular ventas (botón de arrepentimiento).
- **main.py**: Menú principal del sistema modular.
- **README.md**: Documentación general del proyecto.
