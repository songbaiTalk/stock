from flask import Flask

from app.views import init_bp
from app.settings import envs
from app.ext import init_ext

def create_app(env):
    app = Flask(__name__)

    # config class
    app.config.from_object(envs.get(env))

    # extendes example db
    init_ext(app)

    # registe->blueprint
    init_bp(app)


    return app