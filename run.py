# encoding=utf-8
from app import create_app
import os
env = 'develop'
env = 'product'
app = create_app(env)

if __name__ == '__main__':
    # print(app.url_map) # 打印显示url路由
    app.run(host='0.0.0.0', port=5000)


'''
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
# http_server = HTTPServer(WSGIContainer(pool))
# http_server.listen(4000)
# IOLoop.instance().start()
'''

# env = os.environ.get('FLASK_ENV',"develop")
