import pandas as pd
import pandas_datareader.data as stock_reader
# from pandas_datareader import data
import datetime
import numpy as np
from sqlalchemy import create_engine

field_info = pd.read_excel(
    'csrcindustry.xls', dtype={'证券代码\nSecurities Code': np.str})

field_info.columns = ['effective_date', 'securities_code',
                      'securities_name', 'securities_name_en',
                      'exchange', 'CSRC_industry_code',
                      'CSRC_industry_name', 'CSRC_industry_name_en',
                      'CSRC_industry_code_full', 'CSRC_industry_name_full', 'CSRC_industry_name_full_en']


# print(field_info.columns.values)
def replace(item):
    if(item == 'Shanghai'):
        return '.SS'
    elif(item == 'Shenzhen'):
        return '.SZ'


field_info['stock_code'] = field_info['exchange'].map(replace)
field_info['stock_code'] = field_info['securities_code'] + \
    field_info['stock_code']

print(field_info.shape)

# 失败股票411,449,715,905,1057,1401,1404,1507,1665,2006,2243
for i in range(2007, field_info.shape[0]):
    print('current:', i, 'stock_code', field_info['stock_code'][i])
    stock = stock_reader.DataReader(
        field_info['stock_code'][i], "yahoo", datetime.datetime(2019, 1, 1), datetime.datetime(2020, 1, 8))
    stock_data = pd.DataFrame(
        columns=['stock_code', 'stock_name', 'field_id', 'exchange', 'value_open', 'value_close', 'volume'])
    
    stock_data['value_close'] = stock['Close']
    stock_data['value_open'] = stock['Open']
    stock_data['volume'] = stock['Volume']
    stock_data['stock_name'] = field_info['securities_name'][i]
    stock_data['stock_code'] = field_info['stock_code'][i]
    stock_data['field_id'] = field_info['CSRC_industry_code_full'][i]
    stock_data['exchange'] = field_info['exchange'][i]
    print('before insert')
    pd.io.sql.to_sql(stock_data, 'stock', create_engine(
        'mysql+pymysql://root:@localhost:3306/stock?charset=utf8'), schema='stock', if_exists='append')
