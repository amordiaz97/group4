from google.appengine.ext import ndb

class Quiz(ndb.Model):
	user_name = ndb.StringProperty(required=True)
	results = ndb.StringProperty(required=True)
