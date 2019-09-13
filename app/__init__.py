from flask import Flask
from config import config_options
# from flask_bootstrap import Bootstrap

# bootstrap = Bootstrap()

def kora_app(config_name):

    # Initializing the application
    app = Flask(__name__)

    # Create the configurations of the app
    app.config.from_object(config_options[config_name])

    #Initialization of extentions
    # bootstrap.init_app(app)

    # registration of the blueprint
    # from .main import main
    # app.register_blueprint(main_blueprint)

    # setting the configurations
    from.request import config_request
    config_request(app)


    return app


