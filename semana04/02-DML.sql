--DML: Data MAnipulation Lagnguage
--Para entrar a la bd prueba
\c prueba

-- INSERT : Ingresar nuevos registros a una tabla
-- SELECT : Obtener la informacion de determinados registros de una o varias tablas
-- UPDATE: Actuzlizar la informacion registrada
-- DELETE: Elimina de manera permanente los registros en base a condiciones

--INSERT INTO nobre_tabla (nombre_col_1, nom_col_2,...) VALUES (VAL_1, VAL_2,...)

INSERT INTO personas (id, nombre, apellido, correo, fecha_nacimiento) VALUES
                        (DEFAULT, 'Eduardo', 'de Rivero', 'ederiveroman@gmail.com', '1999-12-31');
-- DEFAULT > Indicamos el valor por defecto definido en la columna
-- En las columnas SERIAL agarra el valor que le toca
-- En SQL comillas simples para informacion de texto, 
-- Comillas dobles para nombres de tablas, columnas, etc
-- En SQL Se usa el ISO 8601 para las fechas en el cual el formato es YYYY-MM-DD HH:MM:SS:mmmm
                     

-- Si voy a insertar usando el orden de las columnas con el que la cree puedo precindir del nombre de las columnas PERO si o si tengo que declarar todas las columnas
INSERT INTO personas VALUES (DEFAULT, 'Martha', 'Escobedo', 'mescobedo@gmail.com', '2005-02-14'),
                            (DEFAULT, 'Rodrigo','Jimenez', 'rjimenez@gmail.com', '1989-06-15'),
                            (DEFAULT, 'Marge', 'Marquez', 'mmarquez@gmail.com', '2006-09-07');


--Volviendo al DDL ALTER (Modificar la tabla)
ALTER TABLE personas ADD COLUMN sexo TEXT;

--Eliminar columnas --Este elimina la columna persona
ALTER TABLE personas DROP COLUMN fecha_nacimiento;

-- Cambiar el tipo de dato de alguna columna
--Si cambiamos de texto a entero, entonces debemos de corroborar el cambio
ALTER TABLE personas ALTER COLUMN sexo TYPE INT USING sexo::INT;

-- Cambiar el nombre de la columna antigua por el nuevo
ALTER TABLE personas RENAME COLUMN sexo TO peso;

-- ====================================================================


--SELECT:  LOS DATOS
--SELECT nom_col1, nom_col2.... FROM tablaa;
--Ahora si queremos visualizar todos las columnas de la consulta
--SELECT * FROM tabla


SELECT nombre FROM personas;

SELECT * FROM personas;

-- Se le puede agregar condiciones para que solo algunos sean seleccionados

SELECT * FROM personas WHERE id > 2;

SELECT * FROM personas WHERE id > 2 AND nombre = 'Rodigo' OR nombre = 'Marge';