import time

import webapp2
from google.appengine.ext import ndb
from webapp2_extras import jinja2

from webapp2_extras.users import users

from model.projectData import projectData


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            login_logout_url = users.create_logout_url("/")
        else:
            login_logout_url = users.create_login_url("/")

        jinja = jinja2.get_jinja2(app=self.app)

        list_projects = projectData.query().order(-projectData.hours)

        d = {
            "login_logout_url": login_logout_url,
            "user": user,
            "list_projects": list_projects
        }

        self.response.write(jinja.render_template("index.html", **d))

    def post(self):
        photo = self.request.get('photolink')
        link = self.request.get('githubLink')
        description = self.request.get('description')

        project_data = projectData(image=photo, title=link, text=description)
        project_data.put()
        time.sleep(0.1)
        list_projects = projectData.query().order(-projectData.hours)
        user = users.get_current_user()
        data = {
            "user": user,
            "list_projects": list_projects
        }
        jinja = jinja2.get_jinja2(app=self.app)

        self.response.write(jinja.render_template("index.html", **data))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
