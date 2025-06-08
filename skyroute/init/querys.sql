
    -- CONSULTAS --
    
-- Esta consulta lista todos los clientes

SELECT * FROM clientes;

-- Esta consulta muestra las compras realizadas en una fecha específica

SELECT c.razon_social, 
v.estado,  
ciu.nombre AS ciudad, 
p.nombre AS pais, 
v.monto, 
v.fecha 
FROM ventas v
JOIN clientes c ON v.id_cliente = c.id_cliente
JOIN destinos d ON v.id_destino = d.id_destino
JOIN ciudades ciu ON d.id_ciudad = ciu.id_ciudad 
JOIN paises p ON ciu.id_pais = p.id_pais
WHERE fecha = '2025-03-01 14:00:00';

-- Esta consulta obteniene la última compra de cada cliente y su fecha

SELECT c.razon_social, v.id_cliente, v.estado, v.fecha AS ultima_fecha, v.monto 
FROM  ventas v
JOIN (
   SELECT  MAX(fecha) AS ultima_fecha
   FROM ventas v
   GROUP BY v.id_cliente
   ) ultimas ON v.fecha = ultimas.ultima_fecha
JOIN clientes c ON v.id_cliente = c.id_cliente;
 
-- Esta consulta realiza el ingreso de una ciudad con S y lista todos los destinos que empiezan con 'S', 
 
 INSERT INTO ciudades(nombre, id_pais) VALUES
 ('Salta', 1);
SELECT * FROM ciudades
WHERE nombre LIKE 'S%';

-- Esta consulta muestra cuántas ventas se realizaron por país

INSERT INTO ventas (id_cliente, id_destino, fecha, estado, monto) VALUES
(1, 6,'2025-03-01 18:00:00','Activa', 4000.00);
SELECT p.nombre, COUNT(v.id_venta) AS cantidad_ventas 
FROM ventas v 
JOIN destinos d ON v.id_destino = d.id_destino
JOIN ciudades ciu ON d.id_ciudad = ciu.id_ciudad
JOIN paises p ON ciu.id_pais = p.id_pais
GROUP BY p.nombre; 

