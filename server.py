#Tornado Libraries
from tornado.ioloop import IOLoop
from tornado.escape import json_encode
from tornado.web import RequestHandler, Application, asynchronous, removeslash
from tornado.httpserver import HTTPServer
from tornado.httpclient import AsyncHTTPClient
from tornado.gen import engine, Task, coroutine,Return
#Other Libraries
from motor import MotorClient

#get url from qa repo
# url = ..
db = MotorClient(url)
# hyperparameters
threshold = 0.8

class MainHandler(RequestHandler):
	@coroutine
	def get(self):
		# define your own question for test
		question = self.get_argument('question')
		#confidence, question = deep_match(question)
		# for now use your custom match we will replace 
		# that once we are ready with the server
		# if confidence >= threshold:
			#return db.coll.find_one()



settings = dict(
    db=db,
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True,
    cookie_secret="35an18y3-u12u-7n10-4gf1-102g23ce04n6"
)

application = Application([
    (r"/", MainHandler),
], **settings)

if __name__ == "__main__":
    server = HTTPServer(application)
    server.listen(5000)
    IOLoop.current().start()
