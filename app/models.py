# encoding=utf-8
from app.ext import db

import datetime


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stock_code = db.Column(db.String(20))
    stock_name = db.Column(db.String(20))
    field_id = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    exchange = db.Column(db.String(20))
    value_close = db.Column(db.Float)
    value_open = db.Column(db.Float)
    volume = db.Column(db.Integer)

    # def __init__(self):
    #     print('stock Model init')


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stock_code = db.Column(db.String(20))
    price = db.Column(db.Float)
    amount = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    # def __init__(self):
    #     print('transaction Model init')


class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stock_code = db.Column(db.String(20))
    stock_name = db.Column(db.String(20))
    field_id = db.Column(db.Integer)
    possession = db.Column(db.Integer)
    index = db.Column(db.Integer)

    # def __init__(self):
    #     print('store Model init')
