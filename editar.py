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

        consulta = "UPDATE peliculas SET titulo = ? WHERE id = ?;"
        nuevo_titulo = "Ready Player One: comienza el juego"
        id_editar = 2
        cursor.execute(consulta, (nuevo_titulo, id_editar))

    # No olvidemos hacer commit cuando hacemos un cambio a la BD
    conexion.commit()
except Exception as e:
    print("Ocurrió un error al editar: ", e)
finally:
    conexion.close()
