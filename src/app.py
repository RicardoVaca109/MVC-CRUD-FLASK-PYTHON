# app.py (si decides no usar __init__.py)
from flask import Flask
# from src.controllers.usuario_controller import usuario_bp
from controllers.usuario_controller import usuario_bp
import os


# Inicialización de la aplicación Flask
template_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates')
app = Flask(__name__, template_folder=template_dir)

# Registro del Blueprint
app.register_blueprint(usuario_bp)

if __name__ == '__main__':
    app.run(debug=True, port=4000)