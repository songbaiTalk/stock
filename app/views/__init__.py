# encoding=utf-8
# from .requestpool import requestpool
from .stock import stock


def init_bp(app):
    # app.register_blueprint(requestpool)
    app.register_blueprint(stock)
