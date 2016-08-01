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
import random

env=jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

songs = {"Crazy in Love - Beyonce" : "https://www.youtube.com/embed/watch?v=ViwtNLUqkMY" , 
        "This Is What You Came For - Calvin Harris ft. Rihanna" : "https://www.youtube.com/embed/watch?v=kOkQ4T5WO9E" , 
        "Dani California - Red Hot Chili Peppers" : "https://www.youtube.com/embed/watch?v=Sb5aq5HcS1A" , 
        "Cosmic Love - Florence and the Machine" : "https://www.youtube.com/embed/watch?v=2EIeUlvHAiM", 
        "Hips Don't Lie - Shakira" : "https://www.youtube.com/embed/watch?v=DUT5rEU6pqM",
        "Stairway to Heaven - Led Zeppelin" : "https://www.youtube.com/embed/watch?v=oW_7XBrDBAA",
        "Work It - Missy Elliot" : "https://www.youtube.com/embed/watch?v=cjIvu7e6Wq8",
        "Unsteady - X Ambassadors" : "https://www.youtube.com/embed/watch?v=V0lw3qylVfY",
        "Promise - Romeo Santos ft Usher" : "https://www.youtube.com/embed/watch?v=Y3XyWhrZnqE",
        "No Problem - Chance The Rapper ft. Lil Wayne & 2 Chainz" : "https://www.youtube.com/embed/watch?v=_2LXpNmjxMw",
        "Homecoming - Kanye ft. Chris Martin" : "https://www.youtube.com/embed/watch?v=LQ488QrqGE4",
        "Viva La Vida - Coldplay" : "https://www.youtube.com/embed/watch?v=Tmb7YIKqLeM",
        "Where Ya At - Drake & Future" : "https://www.youtube.com/embed/watch?v=lw3Or6eqIpI",
        "Friday - Rebecca " : "https://www.youtube.com/embed/watch?v=kfVsfOSbJY0",
        "Single Ladies - Beyonce" : "https://www.youtube.com/embed/watch?v=4m1EFMoRFvY",
        "Dancing Queen - ABBA" : "https://www.youtube.com/embed/watch?v=y62OlGvC-bk",
        "Dream On - Aerosmith" : "https://www.youtube.com/embed/watch?v=hHRNSeuvzlM",
        "Bohemian Rhapsody - Queen" : "https://www.youtube.com/embed/watch?v=fJ9rUzIMcZQ",
        "Never Gonna Give You Up - Rick Astley" : "https://www.youtube.com/embed/watch?v=dQw4w9WgXcQ",
        "Roses - Chainsmokers ft. Rozes" : "https://www.youtube.com/watch?v=FyASdjZE0R0"
        }

class MainHandler(webapp2.RequestHandler):
    def get(self):

        template = env.get_template('project-draft.html')
        self.response.write(template.render())

    	template = env.get_template('project-draft.html')
    	self.response.write(template.render())

class SongHandler(webapp2.RequestHandler):  
    def get(self):
        template = env.get_template('song.html')
        # self.songShuffle('songs')
        result = {'link': 'https://www.youtube.com/embed/watch?v=eRaFMlZ1YHA'}
        # result = random.choice(songs.values())
        self.response.write(template.render(result)) #we need to add the dictionary that will pass on the variable(song) to the document

class SongHandler(webapp2.RequestHandler):	
	def get(self):
		template = env.get_template('song.html')
		# self.songShuffle('songs')
		result = {'link': 'https://www.youtube.com/embed/watch?v=eRaFMlZ1YHA'}
		# result = random.choice(songs.values())
		self.response.write(template.render(result)) #we need to add the dictionary that will pass on the variable(song) to the document


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/matching_song', SongHandler)
], debug=True)
