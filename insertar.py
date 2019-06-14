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
        consulta = "INSERT INTO peliculas(titulo, anio) VALUES (?, ?);"
        # Podemos llamar muchas veces a .execute con datos distintos
        cursor.execute(consulta, ("Volver al futuro 1", 1985))
        cursor.execute(consulta, ("Pulp Fiction", 1994))
        cursor.execute(consulta, ("It", 2017))
        cursor.execute(consulta, ("Ready Player One", 2018))
        cursor.execute(consulta, ("Spider-Man: un nuevo universo", 2018))
        cursor.execute(consulta, ("Avengers: Endgame", 2019))
        cursor.execute(consulta, ("John Wick 3: Parabellum", 2019))
        cursor.execute(consulta, ("Toy Story 4", 2019))
        cursor.execute(consulta, ("It 2", 2019))
        cursor.execute(consulta, ("Spider-Man: lejos de casa", 2019))

except Exception as e:
    print("Ocurrió un error al insertar: ", e)
finally:
    conexion.close()
