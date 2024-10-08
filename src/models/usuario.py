from database import conexion_database

#modelo Usuario
class Usuario:
    
    @staticmethod  # Método para obtener los usuarios de la base de datos
    def obtener_usuarios():
        cursor = conexion_database.cursor()
        cursor.execute("SELECT id, nombre_usuario, apellido_usuario, correo FROM usuarios;")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados

    @staticmethod  # Método para crear un nuevo usuario
    def insertar_usuario(nombre, apellido, correo, contrasenia):
        cursor = conexion_database.cursor()
        sql_query_insertar = "INSERT INTO usuarios (nombre_usuario, apellido_usuario, correo, contrasenia) VALUES (%s, %s, %s, %s)"
        data_insertar = (nombre, apellido, correo, contrasenia)
        cursor.execute(sql_query_insertar, data_insertar)
        conexion_database.commit()
        cursor.close()

    @staticmethod  # Método para eliminar un usuario
    def eliminar_usuario(id):
        cursor = conexion_database.cursor()
        sql_query_eliminar = "DELETE FROM usuarios WHERE id = %s"
        data = (id,)
        cursor.execute(sql_query_eliminar, data)
        conexion_database.commit()
        cursor.close()
        
    @staticmethod  # Método para actualizar datos del usuario
    def actualizar_usuario(id,nombre, apellido,correo):
        cursor = conexion_database.cursor()
        sql_query_editar = "UPDATE usuarios SET nombre_usuario = %s, apellido_usuario = %s, correo = %s WHERE id = %s"
        data_actualizada = (nombre, apellido, correo, id)
        cursor.execute(sql_query_editar, data_actualizada)
        conexion_database.commit()
        cursor.close()
        
        
        
        
        
        
        





