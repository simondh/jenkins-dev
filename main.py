"""
/Users/simonhewitt/ComputerStuff/jenkins_home/PythonProj/main.py

Simple Tornado tht responds to a few URLs.
Use: for developing a Jenkins build
"""
import tornado.ioloop
import tornado.web
import os
import socket
import json
# import json_util

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        hostname = socket.gethostname()
        uid = os.getuid()
        info = {'hostname': hostname, 'uid': uid}
        # self.write(json.dumps(info, default=json_util.default))
        self.write(json.dumps(info))
        self.finish()

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
