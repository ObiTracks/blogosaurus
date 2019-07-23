import webapp2
import jinja2
import os

import models

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
        blog_entry = self.request.get('name')

        blog_post = models.BlogPost(name=blog_author, title=blog_title, )
        blog_post.put()

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

"""
class Movie(ndb.Model):
    mov_title = ndb.StringProperty()
    runtime = ndb.IntegerPropery()
    user_rating = ndb.IntegerPropery()

new_movie1 = Movie(mov_title = "Twilight", runtime = 101, user_rating = 5)
new_movie2 = Movie(mov_title = "Avengers", runtime = 160, user_rating = 3)
new_movie3 = Movie1(mov_title = "Star Wars", runtime = 200, user_rating = 0)
"""
