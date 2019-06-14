/*
    Conexión a SQLServer con Python
    Ejemplo de CRUD evitando inyecciones SQL
    
    @author parzibyte

    Más tutoriales en:
                        parzibyte.me/blog
*/
CREATE TABLE IF NOT EXISTS peliculas(
    id bigint identity(1,1) primary key,    
    titulo VARCHAR(255) NOT NULL,
    anio SMALLINT NOT NULL
);
