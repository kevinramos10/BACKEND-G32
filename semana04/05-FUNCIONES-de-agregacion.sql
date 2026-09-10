SELECT * FROM productos p 
--Funciones de agregacion
--Agregate funciones sirve para poder tener un poco de logica en nuestra consulta

--GROUP BY al usar se tiene que agrupar todas las columnas del select
SELECT id, p.categoria  FROM productos p
--WHERE
GROUP BY id, categoria;

--COUNT sirve para contar
SELECT p.activo, COUNT(activo) 
FROM productos p
GROUP BY p.activo;

SELECT categoria, COUNT(categoria)
FROM productos
GROUP BY categoria;


--SUM sumar
SELECT activo,  SUM(stock)
FROM productos
GROUP BY activo

SELECT categoria,  SUM(stock)
FROM productos
WHERE activo = true
GROUP BY categoria;


--AVG promedio
--PROMEDIO DE LOS PRECIOS POR CATEGORIA
SELECT categoria, AVG(precio) 
FROM productos p 
GROUP BY categoria;

--MIN / MAX  devuleves los valores min o max
--QUIERO LOS VALORES MAXIMOS DE LOS PRECIOS POR CATEGORIA PERO QUE SOLO SEAN ACTIVOS
SELECT p.categoria, MAX(p.precio)
FROM productos p
WHERE activo = true
GROUP BY p.categoria 



SELECT categoria, SUM(stock)
FROM productos
WHERE activo = TRUE 
GROUP BY categoria 
HAVING SUM(stock) >= 40 OR AVG(precio) BETWEEN 10 AND 50
ORDER BY sum(stock) DESC, categoria DESC;

--ASC : 0 - 9 | A - Z
--DESC: 9 - 0 | Z - A












