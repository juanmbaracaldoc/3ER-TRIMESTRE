CREATE DATABASE base_data_yeisonM;

//2

\c base_data_Mendieta; SELECT current_database(); \conninfo

//3

CREATE TABLE clientes ( id SERIAL PRIMARY KEY, nombre VARCHAR(100) NOT NULL, email VARCHAR(150) UNIQUE, telefono VARCHAR(15), fecha_registro DATE DEFAULT CURRENT_DATE, activo BOOLEAN DEFAULT TRUE );

//4

INSERT INTO clientes (nombre, email, telefono, fecha_registro, activo) VALUES ('Juan Pérez', 'juan.perez@email.com', '555-0123', '2024-01-15', TRUE); INSERT INTO clientes (nombre, email) VALUES ('María García', 'maria.garcia@email.com'); INSERT INTO clientes (nombre, email, telefono) VALUES ('Carlos López', 'carlos@email.com', '555-0124'), ('Ana Martínez', 'ana@email.com', '555-0125'), ('Luis Rodríguez', 'luis@email.com', '555-0126');

//5

SELECT * FROM clientes; SELECT nombre, email FROM clientes; SELECT nombre, telefono FROM clientes WHERE activo = TRUE; SELECT COUNT(*) FROM clientes; SELECT nombre, email FROM clientes ORDER BY nombre; SELECT * FROM clientes LIMIT 3;

//6

SELECT * FROM clientes WHERE nombre = 'Juan Pérez'; SELECT * FROM clientes WHERE nombre LIKE '%García%'; SELECT * FROM clientes WHERE fecha_registro = '2024-01-15'; SELECT * FROM clientes WHERE fecha_registro > '2024-01-01'; SELECT * FROM clientes WHERE activo = TRUE AND fecha_registro > '2024-01-01'; SELECT * FROM clientes WHERE nombre LIKE '%Juan%' OR nombre LIKE '%María%'; SELECT * FROM clientes WHERE nombre IN ('Juan Pérez', 'María García', 'Carlos López'); SELECT * FROM clientes WHERE nombre NOT LIKE '%López%';