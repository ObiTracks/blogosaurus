import webapp2
import jinja2
import os

#dev_appserver.py app.yaml: This is the line of code to run the server from the command terminal

the_jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_environment.get_template('template/index.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

class BlogEntryHandler(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_environment.get_template('template/new_post.html')
        self.response.write(template.render())

class BlogSubmissionHandler(webapp2.RequestHandler):
    def post(self):
        blog_title = self.request.get('title')
        blog_author = self.request.get('author')
        blog_entry = self.request.get('entry')

        template_variables = {
            "blog_title": blog_title,
            "blog_author": blog_author,
            "blog_entry": blog_entry
        }

        template = the_jinja_environment.get_template('template/view_post.html')
        self.response.write(template.render(template_variables))

    pass


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/blogentry', BlogEntryHandler),
    ('/blogsubmission', BlogSubmissionHandler)

], debug=True)
