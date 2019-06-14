"""
	Conexión a SQLServer con Python
	Ejemplo de CRUD evitando inyecciones SQL
	
	@author parzibyte

	Más tutoriales en:
						parzibyte.me/blog
"""
from bd import conexion
try:
    with conexion.cursor() as cursor:
        consulta = "SELECT id, titulo, anio FROM peliculas WHERE titulo like ?;"
    # Para Avengers Endgame
    busqueda = "endg"
    cursor.execute(consulta, ("%" + busqueda + "%"))

    # Con fetchall traemos todas las filas
    peliculas = cursor.fetchall()

    # Recorrer e imprimir
    for pelicula in peliculas:
        print(pelicula)
except Exception as e:
    print("Ocurrió un error al consultar con where: ", e)
finally:
    conexion.close()
