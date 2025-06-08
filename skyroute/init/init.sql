-- Tabla de países
CREATE TABLE IF NOT EXISTS paises (
    id_pais INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    codigo VARCHAR(10) NOT NULL UNIQUE
);

-- Tabla de ciudades
CREATE TABLE IF NOT EXISTS ciudades (
    id_ciudad INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    id_pais INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_pais) REFERENCES paises(id_pais) ON DELETE RESTRICT,
    UNIQUE(nombre, id_pais)
);

-- Tabla de destinos
CREATE TABLE IF NOT EXISTS destinos (
    id_destino INT AUTO_INCREMENT PRIMARY KEY,
    id_ciudad INT NOT NULL,
    costo_base DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_ciudad) REFERENCES ciudades(id_ciudad) ON DELETE RESTRICT
);

-- Tabla de clientes
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    razon_social VARCHAR(100) NOT NULL,
    cuit VARCHAR(11) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL
);

-- Tabla de ventas
CREATE TABLE IF NOT EXISTS ventas (
    id_venta INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    cliente_id INT NOT NULL,
    destino_id INT NOT NULL,
    fecha DATETIME NOT NULL,
    estado ENUM('Activa', 'Anulada') NOT NULL DEFAULT 'Activa',
    monto DECIMAL(10,2) NOT NULL,
    fecha_anulacion DATETIME NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id_cliente) ON DELETE RESTRICT,
    FOREIGN KEY (destino_id) REFERENCES destinos(id_destino) ON DELETE RESTRICT
);

-- Datos de ejemplo para países
INSERT INTO paises (nombre, codigo) VALUES
('Argentina', 'AR'),
('Brasil', 'BR');

-- Datos de ejemplo para ciudades
INSERT INTO ciudades (nombre, id_pais) VALUES
('Buenos Aires', 1),
('Córdoba', 1),
('Mendoza', 1),
('Bariloche', 1),
('Río de Janeiro', 2);

-- Datos de ejemplo para destinos
INSERT INTO destinos (id_ciudad, costo_base) VALUES
(1, 1000.00),
(2, 800.00),
(3, 1200.00),
(4, 1500.00),
(5, 2000.00); 

-- Datos de ejemplo para clientes
INSERT INTO clientes (razon_social, cuit, email) VALUES
('Ferreteria S.A', '12345678001', 'ferreteria@mail.com'),
('Materiales de Construcción', '87654321001', 'materiales@mail.com'),
('Textil S.A', '11223344001', 'textil@mail.com');

-- Datos de ejemplo para ventas
INSERT INTO ventas (cliente_id, destino_id, fecha, estado, monto)
VALUES
(1, 2, '2023-10-01 10:00:00', 'Activa', 800.00),
(2, 1, '2023-10-01 11:00:00', 'Activa', 1000.00),
(1, 3, '2023-10-01 12:00:00', 'Activa', 1200.00),
(3, 4, '2023-10-01 13:00:00', 'Activa', 1500.00),
(2, 3, '2023-10-01 14:00:00', 'Activa', 1200.00);
