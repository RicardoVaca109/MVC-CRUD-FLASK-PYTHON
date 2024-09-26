# Librerías o Imports
from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

# Path absoluto
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

# Unión de carpetas / ruta del index.html como variable almacenada
template_dir = os.path.join(template_dir, 'src', 'templates')

# Inicialización de Flask 
app = Flask(__name__, template_folder=template_dir)


# Ruta de la Aplicación
@app.route('/')
def home():
    # Cursor para conectar a la base de datos / database.py
    cursor = db.conexion_database.cursor()
    
    # Consulta SQL de base de Datos Select 
    cursor.execute("SELECT id, nombre_usuario, apellido_usuario, correo FROM usuarios;") 
    # Resultados
    myresult = cursor.fetchall()
    
    # Convertir los datos de Resultados a Diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))  # Emparejando cada nombre de columna a su dato
    
    cursor.close()
    return render_template('index.html', datos=insertObject)

# Ruta para guardar usuarios en la base de datos
@app.route('/usuarios', methods=['POST'])
def guardarUsuarios():
    username = request.form['nombre_usuario']
    userLastname = request.form['apellido_usuario']
    mail = request.form['correo']
    password = request.form['contrasenia']
    
    if username and userLastname and mail and password:
        cursor = db.conexion_database.cursor()
        sqlInsertQuery = "INSERT INTO usuarios (nombre_usuario, apellido_usuario, correo, contrasenia) VALUES (%s, %s, %s, %s)"
        dataInsertar = (username, userLastname, mail, password)
        cursor.execute(sqlInsertQuery, dataInsertar)
        db.conexion_database.commit()
    
    return redirect(url_for('home'))

# Ruta para eliminar un usuario
@app.route('/delete/<string:id>')
def eliminarUsuario(id):
    cursor = db.conexion_database.cursor()
    sqlDeleteQuery = "DELETE FROM usuarios WHERE id = %s"
    data = (id,)
    cursor.execute(sqlDeleteQuery, data)
    db.conexion_database.commit()
    return redirect(url_for('home'))

# Ruta para editar un Usuario
@app.route('/edit/<string:id>', methods=['POST'])
def editarUsuario(id):
    username = request.form['nombre_usuario']
    userLastname = request.form['apellido_usuario']
    mail = request.form['correo']
    
    if username and userLastname and mail:
        cursor = db.conexion_database.cursor()
        sqlUpdateQuery = "UPDATE usuarios SET nombre_usuario = %s, apellido_usuario = %s, correo = %s WHERE id = %s"
        dataActualizar = (username, userLastname, mail, id)
        cursor.execute(sqlUpdateQuery, dataActualizar)
        db.conexion_database.commit()
    
    return redirect(url_for('home'))

# Condición para lanzar como programa principal
if __name__ == '__main__':
    app.run(debug=True, port=4000)
