# finalGrupoA
Proyecto final del curso de Python en CoderHouse
Proyecto Grupo A: Biblioteca P.P.P.
Se basa en la idea de una biblioteca pública y gratuita.
Página Inicio: /app_biblioteca/
    Muestra menú de opciones:
        Inicio: accesible desde cualquier otro lugar
        Catálogo: para visualizar lista de TODOS los libros: Título – Autor
        Cursos: para visualizar lista de TODOS los cursos: Nombre – Dia y Horario
        Buscar libros: acceso a formulario de búsqueda por título o palabra clave. Muestra listado de libros encontrados o mensaje si no se encontró. 
        Crea tu cuenta: en construcción, para creación de nuevas cuentas de socios
        Acceso a socios: en construcción, para login / logout de socios ya registrados
    Botón “Quiero ser socio”, que hace scroll y muestra requisitos
Página Libros:  /app_biblioteca/libros/
    Ingreso a formulario de alta de modelo Libro:  nombre, autor, publicación, genero, editorial
    Se envían datos y se retorna a página de inicio
Página Cursos: /app_biblioteca/cursos/
    Ingreso a formulario de alta de modelo Cursos:  nombre, código, docente, día-horario
    Se envían datos y se retorna a página de inicio
Página Socios: /app_biblioteca/socios/
    Ingreso a formulario de alta de modelo Socio: nombre, documento, mail, teléfono
    Se envían datos y se retorna a página de inicio
    
Templates: 
    Se adecuó una página de descarga gratuita del sitio Bootstrap.
    El template  “padre.html” es heredado por los siguientes: 
    “catalogo.html”, “listadocursos.html”, “buscarlibro.html”, “resultado.html”, “cursos.html”, “libros.html”, “socios.html”, “creatucuenta.html”, “accesoasocios.html”




