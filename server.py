# Tornado Libraries
from tornado.ioloop import IOLoop
from tornado.escape import json_encode
from tornado.web import RequestHandler, Application, asynchronous, removeslash
from tornado.httpserver import HTTPServer
from tornado.httpclient import AsyncHTTPClient
from tornado.gen import engine, Task, coroutine, Return
# Other Libraries
from motor import MotorClient
import json
from factoid import factoid
from generative import generative
# get url from qa repo
db = MotorClient(url)
# hyperparameters
threshold = 0.8


class MainHandler(RequestHandler):
    @coroutine
    def get(self):

        question = self.get_argument('question')
        items = factoid(question)
        if items[0] >= threshold:
            answer = items[1]
        else:
            answer = generative(question)

        jsonData = {
            'status': 200,
            'message': answer,
            'payload': response

        }
        self.write(json.dumps(jsonData))

    def write_error(self, status_code, **kwargs):
        jsonData = {
            'status': int(status_code),
            'message': "Internal server error",
            'answer': 'NULL'
        }
        self.write(json.dumps(jsonData))

    def options(self):
        self.set_status(204)
        self.finish()

settings = dict(
    # db=db,
    debug=True
)

application = Application([
    (r"/", MainHandler),
], **settings)

if __name__ == "__main__":
    server = HTTPServer(application)
    server.listen(5000)
    IOLoop.current().start()
