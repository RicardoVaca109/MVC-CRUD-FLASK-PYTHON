Proyecto CRUD MVC en Python con Flask y MySQL  
Este proyecto implementa una aplicación web básica de gestión de usuarios con un CRUD (Crear, Leer, Actualizar, Eliminar) usando Python, Flask y MySQL, 
siguiendo el patrón arquitectónico MVC (Modelo-Vista-Controlador). La aplicación permite administrar usuarios con vistas amigables y una estructura 
organizada en controladores y modelos.

Estructura del Proyecto:
-Modelos: Define la lógica de la base de datos, con métodos para obtener, insertar, actualizar y eliminar usuarios.
-Controladores: Maneja las rutas y la lógica de negocio de la aplicación, interactuando con los modelos para realizar acciones en la base de datos.
-Vistas: Proporciona la interfaz de usuario mediante plantillas HTML, facilitando la interacción y visualización de datos.

Requisitos Previos:
-Python 3 instalado en tu máquina.
-MySQL como sistema de base de datos.
-Flask para el framework web.
-Conexión a la Base de Datos: Configura tu conexión en el archivo database.py y un archivo extra tipo .env con los valores usuario y contraseña de la
  base de datos.


Crea una base de datos en MySQL.
Actualiza el archivo database.py para incluir las credenciales y la información de conexión.
Configura las tablas:
Crea la tabla usuarios en tu base de datos MySQL:

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50),
    apellido_usuario VARCHAR(50),
    correo VARCHAR(50),
    contrasenia VARCHAR(100)
);

Estructura de Archivos:
*models/usuario.py: Define el modelo Usuario y los métodos para interactuar con la base de datos.
*controllers/usuario_controller.py: Contiene las rutas y controladores para el manejo de usuarios.
*templates/index.html: Archivo HTML que muestra la lista de usuarios, y formularios para crear y editar usuarios.
