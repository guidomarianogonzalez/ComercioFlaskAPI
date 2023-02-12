from flask import  Flask
import os
from dotenv import load_dotenv

#importo modulo para crear la api-rest
from flask_restful import Api
#importo el módulo SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

api = Api()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    #ejecuto la funcion load_dotenv y cargo las variables de entorno
    load_dotenv()
    #Configuración de la base de datos a través de las variables de entorno cargadas
    PATH = os.getenv("DATABASE_PATH")
    DB_NAME = os.getenv("DATABASE_NAME")
    #Compruebo si existe archivo, sino lo creo de vuelta
    if not os.path.exists(f"{PATH}{DB_NAME}"):
        os.chdir(f"{PATH}")
        file = os.open(f"{DB_NAME}", os.O_CREAT)
        
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{PATH}{DB_NAME}"

    db.init_app(app)

    import main.resources as resources
    api.add_resource(resources.ClientesResource, "/clientes")
    api.add_resource(resources.ClienteResource, '/cliente/<id>')
    api.add_resource(resources.UsuarioResource, "/usuario/<id>")
    api.add_resource(resources.UsuariosResource,"/usuarios")
    api.add_resource(resources.ComprasResource, '/compras')
    api.add_resource(resources.CompraResource, '/compra/<id>')
    api.add_resource(resources.ProductosResource, '/productos')
    api.add_resource(resources.ProductoResource, '/producto/<id>')
    api.add_resource(resources.ProductosComprasResource, '/productos-compras')
    api.add_resource(resources.ProductoCompraResource, '/producto-compra/<id>')


    api.init_app(app)



    return app



