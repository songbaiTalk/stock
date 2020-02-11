# encoding=utf-8

# 数据库操作函数

def insertRequests(requests, table, api, session):

    words_expressions = '(page,requestid, api, url, state, times, req)'
    value_expression = []
    for request in requests:
        value_expression.append(''.format(
            request['page'], request['requestid'], request['api'], request['url'], request['state'], request['times'], request['response']))
    ','.join(value_expression)
    update_expression = 'req=req, state=state'
    sql = 'insert into {}  values {} on duplicate key update {}'.format(
        table, words_expressions, value_expression, update_expression)
    session.execute(sql)
    session.commit()
    session.close()


def getUrlsRequests(requests,table,api,session):
    pass