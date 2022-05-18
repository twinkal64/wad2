import webapp2
class Mainpage(webapp2.RequestHandler):
defget(self):
self.response.write("Hello World")
app webapp2.WSGIA
application([('/ ',Mainpage)],debug=true)