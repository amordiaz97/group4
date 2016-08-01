#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2

env=jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

songs: {"Crazy in Love by Beyonce" : "https://www.youtube.com/watch?v=ViwtNLUqkMY" , "This Is What You Came For by Calvin Harris ft. Rihanna" : "https://www.youtube.com/watch?v=kOkQ4T5WO9E" , "Dani California by Red Hot Chili Peppers" : "https://www.youtube.com/watch?v=Sb5aq5HcS1A" , "Cosmic Love by Florence and the Machine" : "https://www.youtube.com/watch?v=2EIeUlvHAiM", }



class MainHandler(webapp2.RequestHandler):
    def get(self):
    	template = env.get_template('project-draft.html')
    	self.response.write(template.render())
    	

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
