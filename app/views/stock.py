# encoding=utf-8
from flask import Blueprint, request, jsonify
from app.models import Stock, Transaction, Store
from app.ext import db

stock = Blueprint('stock', __name__,
                  url_prefix='/stock/api')

@stock.route('/test', methods=['GET'])
def test():
    return jsonify({
        "code": 200,
        "msg": '',
        "data": None
    })

@stock.route('/stockListByDateAndField', methods=['POST'])
def stockListByDateAndField():
    # 获取POST的参数
    date = request.form['date']
    field_id = request.form['fieldId']
    result = Stock.query.filter(Stock.date == date).filter(
        Stock.field_id == field_id)
    resp = list()
    for stock in result:
        resp.append({
            'stock_name': stock.stock_name,
            'value_close': stock.value_close,
            'value_open': stock.value_open,
        })
    return jsonify({
        "code": 200,
        "msg": "",
        "data": resp
    })

@stock.route('/stockTrade', methods=['POST'])
def stockTrade():
    amount = float(request.form['amount'])
    stock_code = request.form['stock_code']
    price = request.form['price']
    date = request.form['date']
    store = Store.query.filter(
        Store.stock_code == stock_code).first()
    store = int(store.possession)

    if(store + amount < 0):
        return jsonify({
            code: 201,
            msg: '卖出量超出持有量',
            data: None
        })
    Store.query.filter(
        Store.stock_code == stock_code).update({"possession": store + amount})

    transaction = Transaction(stock_code=stock_code,
                              amount=amount, price=price, date=date)
    db.session.add(transaction)
    db.session.commit()
    return jsonify({
        "code": 200,
        "msg": "",
        "data": None
    })

@stock.route('/stockTradeList', methods=['POST'])
def stockTradeList():
    stock_code = request.form['stock_code']
    result = Transaction.query.filter(
        Transaction.stock_code == stock_code)
    resp = list()
    for tradeItem in result:
        resp.append({
            'price': tradeItem.price,
            'amount': tradeItem.amount,
            'date': tradeItem.date
        })
    return jsonify({
        "code": 200,
        "msg": "",
        "data": resp
    })

@stock.route('/stockListByStockCode', methods=['POST'])
def stockListByStockCode():
    stock_code = request.form['stock_code']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    result = Stock.query.filter(
        Stock.stock_code == stock_code).filter(Stock.date.between(start_date, end_date))
    records = list()
    baseInfo = {
        "stock_name": "",
        "exchange": "",
        "field_id": ""
    }
    for i, stock in enumerate(result):
        print(i, stock.stock_name)
        if (i == 0):
            baseInfo["stock_name"] = stock.stock_name
            baseInfo["exchange"] = stock.exchange
            baseInfo["field_id"] = stock.field_id
        records.append({
            'value_close': stock.value_close,
            'value_open': stock.value_open,
            "volume": stock.volume
        })
    return jsonify({
        "code": 200,
        "msg": "",
        "data": {
            "baseInfo": baseInfo,
            "record": records
        }
    })
