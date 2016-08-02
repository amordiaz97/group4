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
import json
import logging


env=jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
result = { }



class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = env.get_template('homepage.html')
		self.response.write(template.render())

class SongHandler(webapp2.RequestHandler):
	def get(self):
		template = env.get_template('project-song.html')
		self.response.write(template.render())

class DisneyHandler(webapp2.RequestHandler):
	def get(self):
		template = env.get_template('disney.html')
		self.response.write(template.render())

class foodHandler(webapp2.RequestHandler):
	def get(self):
		template = env.get_template('food.html')
		self.response.write(template.render())

class MatchingSongHandler(webapp2.RequestHandler):  
	def get(self):
		songs = {"Crazy in Love - Beyonce" : "https://www.youtube.com/embed/ViwtNLUqkMY" , 
		"This Is What You Came For - Calvin Harris ft. Rihanna" : "https://www.youtube.com/embed/kOkQ4T5WO9E" , 
		"Dani California - Red Hot Chili Peppers" : "https://www.youtube.com/embed/Sb5aq5HcS1A" , 
		"Cosmic Love - Florence and the Machine" : "https://www.youtube.com/embed/2EIeUlvHAiM", 
		"Hips Don't Lie - Shakira" : "https://www.youtube.com/embed/DUT5rEU6pqM",
		"Stairway to Heaven - Led Zeppelin" : "https://www.youtube.com/embed/oW_7XBrDBAA",
		"Work It - Missy Elliot" : "https://www.youtube.com/embed/cjIvu7e6Wq8",
		"Unsteady - X Ambassadors" : "https://www.youtube.com/embed/V0lw3qylVfY",
		"Promise - Romeo Santos ft Usher" : "https://www.youtube.com/embed/Y3XyWhrZnqE",
		"No Problem - Chance The Rapper ft. Lil Wayne & 2 Chainz" : "https://www.youtube.com/embed/_2LXpNmjxMw",
		"Homecoming - Kanye ft. Chris Martin" : "https://www.youtube.com/embed/LQ488QrqGE4",
		"Viva La Vida - Coldplay" : "https://www.youtube.com/embed/Tmb7YIKqLeM",
		"Where Ya At - Drake & Future" : "https://www.youtube.com/embed/lw3Or6eqIpI",
		"Friday - Rebecca " : "https://www.youtube.com/embed/kfVsfOSbJY0",
		"Single Ladies - Beyonce" : "https://www.youtube.com/embed/4m1EFMoRFvY",
		"Dancing Queen - ABBA" : "https://www.youtube.com/embed/y62OlGvC-bk",
		"Dream On - Aerosmith" : "https://www.youtube.com/embed/hHRNSeuvzlM",
		"Bohemian Rhapsody - Queen" : "https://www.youtube.com/embed/fJ9rUzIMcZQ",
		"Never Gonna Give You Up - Rick Astley" : "https://www.youtube.com/embed/dQw4w9WgXcQ",
		"Roses - Chainsmokers ft. Rozes" : "https://www.youtube.com/embed/FyASdjZE0R0"
		}
		
		template = env.get_template('song.html')
		result = random.choice(songs.keys())
		value = songs[result]
		data = {'link' : value, 'result': result}
		self.response.write(template.render(data)) #we need to add the dictionary that will pass on the variable(song) to the document



app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/song_quiz', SongHandler),
	('/matching_song', MatchingSongHandler),
	('/disney', DisneyHandler),
	('/food', foodHandler)
], debug=True)
