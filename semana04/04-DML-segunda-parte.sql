--Continuando con el DML
--UPDATE > Actualizar los registros de determinadas tablas

--Si en el UPDATE no se pone condicionales se van a modificar todos los registros
--UPDATE nombre_tabla SET nombre = 'Ayudin' WHERE id = 1

select * from productos p;

UPDATE productos p SET nombre = 'Arroz Faraon 5kg' WHERE id = 1;

-- Actualizar el nombre de 'Cerveza Cusque¤a 620ml' a 'Cerveza Cusqueña 622ml'

UPDATE productos p SET nombre = 'Cerveza Cusqueña 623ml' WHERE nombre = 'Cerveza Cusqueña 622ml';

--UPDATE productos SET nombre = ' Cerveza Cusqueña 620ml' WHERE nombre LIKE 'Cerveza Cusqueña 620ml'; es lo mismo

--DELETE: Siempre va con where sino se borra todo
--DELETE FROM nombre_tabla WHERE condicionales;

DELETE FROM productos WHERE id = 9;


--La unica forma de revertir los cambios es solo si la query esta en una transaccion


