from google.appengine.ext import ndb


class projectData(ndb.Model):
    hours = ndb.DateTimeProperty(auto_now_add=True)
    image = ndb.StringProperty()
    title = ndb.StringProperty()
    text = ndb.StringProperty()
