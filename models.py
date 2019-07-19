from google.appengine.ext import ndb


class BlogPost(ndb.Model):
    name = ndb.StringProperty();
    title = ndb.StringProperty();
    content = ndb.TextProperty();
