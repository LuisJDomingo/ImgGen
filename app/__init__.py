print("inocio __init__")

from flask import Flask
from pymongo import MongoClient
from .routes import main_bp

def create_app():
    app = Flask(__name__, template_folder='../templates')

    # Configuración de la base de datos
    app.config["MONGO_URI"] = "mongodb://localhost:27017/image_gen_app"
    app.db_client = MongoClient(app.config["MONGO_URI"])
    app.db = app.db_client.get_database()

    # Registro del blueprint
    app.register_blueprint(main_bp)
    print("he creado la app")
    print("comando dir: \n\t",dir(app),"\n")
    print("comando app.url_map: \n\t",app.url_map)
    print("comando app.config: \n\t", app.config)
    print("comando vars: \n\t", vars(app))
    print("---------------------------------------")
    # import pdb; pdb.set_trace()


    return app
