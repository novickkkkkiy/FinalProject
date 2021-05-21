import time

import webapp2
from google.appengine.ext import ndb
from webapp2_extras import jinja2
from time import gmtime, strftime
from webapp2_extras.users import users

from model.commentData import commentData


class ProjectHandler(webapp2.RequestHandler):
    def get(self):
        str_key = self.request.GET["id"]
        key = ndb.Key(urlsafe=str_key)
        project = key.get()
        list_data = commentData.query(commentData.project_key == project.key).order(-commentData.hours)

        user = users.get_current_user()

        data = {
            "user": user,
            "list_data": list_data,
            "project": project
        }
        jinja = jinja2.get_jinja2(app=self.app)

        self.response.write(jinja.render_template("myproject.html", **data))

    def post(self):
        str_key = self.request.GET["id"]
        key = ndb.Key(urlsafe=str_key)
        project = key.get()
        comment = self.request.get('userComment')

        user = users.get_current_user()
        comment_data = commentData(text=comment, project_key=project.key)
        comment_data.put()
        time.sleep(0.1)
        list_data = commentData.query(commentData.project_key == project.key).order(-commentData.hours)

        data = {
            "user": user,
            "list_data": list_data,
            "project": project
        }
        jinja = jinja2.get_jinja2(app=self.app)

        self.response.write(jinja.render_template("myproject.html", **data))


app = webapp2.WSGIApplication([
    ('/project', ProjectHandler)
], debug=True)
