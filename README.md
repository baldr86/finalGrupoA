finalGrupoA

Integrantes: Pablo Petrich, Paola Enderle y Patricia Palazzo

Proyecto Grupo A: Biblioteca P.P.P.

Se basa en la idea de una biblioteca pública y gratuita. Requiere ser socio para acceder a préstamos de libros.

Para su ejecución se requiere la ejecución de : pip install django-crispy-forms

                  se requiere la creación de superusuario, para que sea identificado como personal de staff.

Al ingresar se visualiza nombre de la biblioteca y  barra de menú con las siguientes opciones:

•	Inicio: accesible desde cualquier otro lugar, retorna al inicio

•	Nosotros:  se describe motivaciones del proyecto, y de quienes lo llevan a cabo

•	Personal P.P.P.:  visible cuando se loguea un miembro del staff, personal de la biblioteca: al ingresar se habilita otro menú en la parte inferior:

    	Libros: se accede a listado de libros, para cada elemento muestra opciones:

            "ver": se muestra el detalle de todos los campos del formulario, luego se regresa a la lista de libros

            "editar”: se puede modificar cualquiera de los campos, luego de enviar retorna a la lista de libros

            "borrar": se muestra nombre del libro, autor y género, se pregunta para confirmar o cancelar, y se retorna a lista de libros

            "nuevo”: al final del listado, se accede a formulario con los campos: nombre, autor, publicación, genero, editorial - 
            
             al enviar vuelve a la lista de libros.

    	Cursos: se accede a listado de cursos, para cada elemento muestra opciones:

            "ver": se muestra el detalle de todos los campos del formulario, luego se regresa a la lista de cursos

            "editar”: se puede modificar cualquiera de los campos, luego de enviar retorna a la lista de cursos

            "borrar": se muestra nombre del curso y día/horario, se pregunta para confirmar o cancelar, y se retorna a lista de cursos

            "nuevo”: al final del listado, se accede a formulario con los campos: nombre, código, docente, día/horario -
            
            al enviar vuelve a la lista de cursos.


    	Socios: se accede a listado de socios, para cada elemento muestra opciones:

            "ver": se muestra el detalle de todos los campos del formulario, luego se regresa a la lista de socios

            "editar”: se puede modificar cualquiera de los campos, luego de enviar retorna a la lista de socios

            "borrar": se muestra nombre del socio, mail, y teléfono, se pregunta para confirmar o cancelar, y retorna a lista de socios

            "nuevo”: al final del listado se accede a formulario con los campos: nombre, documento, mail, teléfono - 
            
            al enviar vuelve a la lista de socios.

    	Posts: se accede a visualizar los posts. Se muestra imagen, título, contenido, y con íconos pequeños se muestra la cantidad
    
             de “vistas”, “likes” y “comentarios” que tiene el post, además del tiempo de publicación (en días y horas / 
             
             horas y minutos).

             Para cada post muestra opción de:
         
             "editar”: se puede modificar cualquiera de los campos, luego de enviar retorna a la lista de posts
         
             "eliminar”: se muestra título del post, y se pregunta para confirmar o cancelar, y se retorna a lista de posts
         
             "nuevo”: a través de botón en parte superior izquierda del listado, se accede a formulario con los campos:
             
             título, contenido, imagen, autor(seleccionable de lista de usuarios) - al enviar vuelve a la lista de posts.


•	Catálogo: para visualizar lista de TODOS los libros: Título – Autor. Acceso sin restricciones.

•	Buscar libros: acceso a formulario de búsqueda por título o palabra clave. Se muestra listado de libros encontrados o mensaje

                 si no se encontró. Acceso sin restricciones.

•	Cursos: para visualizar lista de TODOS los cursos: Nombre – Dia y Horario. Acceso sin restricciones.

•	Crea tu cuenta: creación de nuevas cuentas de usuarios. Cualquier persona puede ser usuario. Se ingresa a formulario que pide:

                  nombre de usuario - mail - contraseña - repetir contraseña (se exigen todos los campos completos y la
                  
                  igualdad de las contraseñas ingresadas)- en caso de algún error da mensaje de "usuario no creado, 
                  
                  intente nuevamente"

•	Ingresar: para login de usuarios ya registrados. Al loguearse se muestra saludo, aparece opción en menú para "salir",
            
              desaparece opción de “crear cuenta", y se habilita opción de menú "Nuestras recomendaciones".
              
              Si el usuario logueado es personal de staff, se habilita opción “Personal P.P.P.”
              
              En caso de error muestra mensaje de ingreso erróneo.

•	Perfil: visible sólo para usuarios logueados.

            Se accede a visualizar los datos de perfil: imagen de avatar, nombre de usuario y mail.
            
            Permite “editar”: cambiar imagen de avatar, o los campos de usuario: mail y contraseña.                     


•	Salir: para logout del usuario logueado, da mensaje de despedida, habilita opción de "crear cuenta" e "ingresar" 

           del menú principal, deshabilita opción de "Nuestras recomendaciones" y "perfil", además, deshabilita
           
           opción de "Personal P.P.P." en caso que el usuario logueado haya sido un miembro del staff.        
         

Botón central “Quiero ser socio”, que hace scroll y muestra requisitos: presentarse personalmente en la Sede de

                                  la Biblioteca, con DNI, y firmar la inscripción. 
    
Templates: 

Se adecuó una página de descarga gratuita del sitio Bootstrap. El template  “padre.html” es heredado por

los siguientes: “accesoacuenta”, "agregaravatar", “buscarlibro”, “catalogo”, “creatucuenta”, “curso_confirm_delete”, 

“curso_detail”, “curso_form”, “curso_list”, “cursos”, "editarperfil",“libro_confirm_delete”, “libro_detail”, “libro_form”,

“libro_list”, “libros”, “listadocursos”,”logout”, “menustaff”, “nosotros”,"perfil", “post_confirm_delete”, “post_create”,

“post_detail”, “post_form”, “post_list”, “resultado”, “socio_confirm_delete”, “socio_detail”, “socio_form”,

“socio_list”, “socios”

Tareas de los integrantes del grupo:

Pablo: tema posts completo, creación, edición, eliminación, listado, conteo de vistas, likes, y comentarios:  vistas,

formularios y templates, URLS correspondientes. Perfil: edición de perfil de usuario, clases, vistas y templates para

carga de avatares y modificación de datos de usuario. Creación de video explicativo del proyecto. Revisiones y 

controles generales. 

Paola: creación de modelo y formulario de cursos, sección “nosotros”: template y vista, revisión de proyecto en general,

creación de plantilla de pruebas de control.

Patricia: adecuación página HTML descargada de Bootstrap, menús (control de acceso), creación de cuenta de usuario, login,

logout:  vistas, clases, templates, URLS. CRUD: libros, socios, cursos: URLS, vistas, formularios y templates. 

Carga de base de datos, redacción readme, revisión en general.


