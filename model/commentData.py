from google.appengine.ext import ndb

from model.projectData import projectData


class commentData(ndb.Model):
    hours = ndb.DateTimeProperty(auto_now_add=True)
    text = ndb.StringProperty(required=True)
    project_key = ndb.KeyProperty(kind=projectData)
