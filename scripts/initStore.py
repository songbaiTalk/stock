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

store_data = pd.DataFrame(
    columns=['stock_code', 'stock_name', 'field_id', 'possession'])

store_data['stock_code'] = field_info['stock_code']
store_data['stock_name'] = field_info['securities_name']
store_data['field_id'] = field_info['CSRC_industry_code_full']
store_data['possession'] = 0
pd.io.sql.to_sql(store_data, 'store', create_engine(
    'mysql+pymysql://root:@localhost:3306/stock?charset=utf8'), schema='stock', if_exists='append')
