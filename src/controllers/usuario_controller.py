# src/controllers/usuario_controller.py
from flask import Blueprint, render_template, redirect, request, url_for
from models.usuario import Usuario

usuario_bp = Blueprint('usuario_bp', __name__)

# Ruta de la Aplicación
@usuario_bp.route('/')
def home():
    usuarios = Usuario.obtener_usuarios()
    # Convertir los datos de Resultados a Diccionario
    insertObject = []
    columnNames = ['id', 'nombre_usuario', 'apellido_usuario', 'correo']
    for record in usuarios:
        insertObject.append(dict(zip(columnNames, record)))  # Emparejando cada nombre de columna a su datos
    return render_template('index.html', datos=insertObject)

# Ruta para guardar usuarios en la base de datos
@usuario_bp.route('/usuarios', methods=['POST'])
def guardarUsuarios():
    nombre = request.form['nombre_usuario']
    apellido = request.form['apellido_usuario']
    correo = request.form['correo']
    contrasenia = request.form['contrasenia']
    
    if nombre and apellido and correo and contrasenia:
        Usuario.insertar_usuario(nombre, apellido, correo, contrasenia)
        
    return redirect(url_for('usuario_bp.home'))

# Ruta para eliminar un usuario
@usuario_bp.route('/delete/<string:id>')
def eliminarUsuario(id):
    Usuario.eliminar_usuario(id)
    return redirect(url_for('usuario_bp.home'))


#  Ruta para editar un Usuario
@usuario_bp.route('/edit/<string:id>', methods = ['POST'])
def editarUsuario(id):
    nombre = request.form['nombre_usuario']
    apellido = request.form['apellido_usuario']
    correo = request.form['correo']
    
    if nombre and apellido and correo:
        Usuario.actualizar_usuario(id,nombre, apellido, correo)
    return redirect(url_for('usuario_bp.home'))