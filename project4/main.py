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
from google.appengine.api import users
import webapp2
import jinja2
import random
import json
import logging


env=jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))




class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                (user.nickname(), users.create_logout_url('/home')))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                users.create_login_url('/home'))

        self.response.out.write('<html><body>%s</body></html>' % greeting)

class HomeHandler(webapp2.RequestHandler):
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

class MatchingFoodHandler(webapp2.RequestHandler):
	def post(self):
			template = env.get_template('matching_food.html')
			pic_link = " "
			foods = { "Kiwi: You are very versatile, always switching up your physical appearance to match your daily mood. Your enemy is chocolate." : "/static/Pictures/foodpics/kiwi.jpg", 
			"Lemon: You have a sour personality. People see you as bright, but at times you may be bitter. " : "/static/Pictures/foodpics/lemon.jpg", 
			"Chocolate: You are mellow; and you often go with the flow. You are also intelligent and love to be the center of attention. You have a very flexible nature. Your natural enemy is a potato. ": "/static/Pictures/foodpics/coco.jpg",
			"Potatoes : You have a starchy personality. You always dress on point, whether you are french, baked, or mashed. " : "/static/Pictures/foodpics/potatoes.jpg", 
			"Pizza Crust: You are so picky and reluctant to try new foods. This means you have a stubborn tendency to complete one task before moving on to another." : "/static/Pictures/foodpics/pizzacrust.jpg",
			"Sushi: You have a refined character that contains an excessive amount of style and poise." : "/static/Pictures/foodpics/sushi.jpg",
			"Banana: You are funny and never let anything get in the way of a joke! You always make your friends laugh. Your natural enemy is a lemon." :"/static/Pictures/foodpics/banana.jpg",
			"Shrimp: You have a selfish personality, you must stay true to meeting your goals and build your confidence. Your enemy is sushi. " : "/static/Pictures/foodpics/shrimp.jpg",
			"Bread: You have your own distinctive and taste. You are full of fun and you are easy to get along with." : "/static/Pictures/foodpics/bread.jpg",
			"Spaghetti: You are very genuine. Your have a very warm and comforting personality.":  "/static/Pictures/foodpics/spaghetti.jpg"
			}
			food_points = {
				"Kiwi: You are very versatile, always switching up your physical appearance to match your daily mood. Your enemy is chocolate." : 0,
				"Lemon: You have a sour personality. People see you as bright, but at times you may be bitter. " : 0,
				"Chocolate: You are mellow; and you often go with the flow. You are also intelligent and love to be the center of attention. You have a very flexible nature. Your natural enemy is a potato. " : 0,
				"Potatoes : You have a starchy personality. You always dress on point, whether you are french, baked, or mashed. " : 0,
				"Pizza Crust: You are so picky and reluctant to try new foods. This means you have a stubborn tendency to complete one task before moving on to another." : 0,
				"Sushi: You have a refined character that contains an excessive amount of style and poise." : 0,
				"Banana: You are funny and never let anything get in the way of a joke! You always make your friends laugh. Your natural enemy is a lemon." : 0,
				"Shrimp: You have a selfish personality, you must stay true to meeting your goals and build your confidence. Your enemy is sushi. " : 0,
				"Bread: You have your own distinctive and taste. You are full of fun and you are easy to get along with." : 0,
				"Spaghetti: You are very genuine. Your have a very warm and comforting personality." : 0
			}
			firstName = self.request.get('letter')
			pizza = self.request.get('pizzatop')
			chicken = self.request.get('chxtype')
			herb = self.request.get("herbguess")
			rather = self.request.get('ratherpick')
			halloween = self.request.get('fruit')
			hungry_yes_no = self.request.get('feeling')
			favorite_place = self.request.get('place2eat')

#comparing pizza responses
			if pizza == 'sausage':
				food_points['Kiwi: You are very versatile, always switching up your physical appearance to match your daily mood. Your enemy is chocolate.'] += 1
				food_points["Spaghetti: You are very genuine. Your have a very warm and comforting personality."] += 1
			elif pizza == 'pepperoni':
				food_points["Potatoes : You have a starchy personality. You always dress on point, whether you are french, baked, or mashed. "] += 1
				food_points["Shrimp: You have a selfish personality, you must stay true to meeting your goals and build your confidence. Your enemy is sushi. "] += 1
			elif pizza == 'mushroom':
				 food_points["Lemon: You have a sour personality. People see you as bright, but at times you may be bitter. "] += 1
				 food_points["Bread: You have your own distinctive and taste. You are full of fun and you are easy to get along with."] += 1
			elif pizza == 'olives':
				food_points["Pizza Crust: You are so picky and reluctant to try new foods. This means you have a stubborn tendency to complete one task before moving on to another."] += 1
				food_points["Sushi: You have a refined character that contains an excessive amount of style and poise."] += 1
			elif pizza == 'chicken':
				food_points["Chocolate: You are mellow; and you often go with the flow. You are also intelligent and love to be the center of attention. You have a very flexible nature. Your natural enemy is a potato. "] += 1
				food_points["Banana: You are funny and never let anything get in the way of a joke! You always make your friends laugh. Your natural enemy is a lemon."] += 1
#comparing chicken responses
			if chicken == 'chxtenders':
				food_points['Kiwi: You are very versatile, always switching up your physical appearance to match your daily mood. Your enemy is chocolate.'] += 1
				food_points["Chocolate: You are mellow; and you often go with the flow. You are also intelligent and love to be the center of attention. You have a very flexible nature. Your natural enemy is a potato. "] += 1
				food_points["Banana: You are funny and never let anything get in the way of a joke! You always make your friends laugh. Your natural enemy is a lemon."] += 1
			elif chicken == 'chxnugs':
				food_points["Spaghetti: You are very genuine. Your have a very warm and comforting personality."] += 1
				food_points["Potatoes : You have a starchy personality. You always dress on point, whether you are french, baked, or mashed. "] += 1
				food_points["Shrimp: You have a selfish personality, you must stay true to meeting your goals and build your confidence. Your enemy is sushi. "] += 1
			elif chicken == 'friedchx':
				food_points["Lemon: You have a sour personality. People see you as bright, but at times you may be bitter. "] += 1
				food_points["Bread: You have your own distinctive and taste. You are full of fun and you are easy to get along with."] += 1
			elif chicken == 'rostchx':
				food_points["Pizza Crust: You are so picky and reluctant to try new foods. This means you have a stubborn tendency to complete one task before moving on to another."] += 1
				food_points["Sushi: You have a refined character that contains an excessive amount of style and poise."] += 1
			elif chicken == 'nochx':
				food_points['Kiwi: You are very versatile, always switching up your physical appearance to match your daily mood. Your enemy is chocolate.'] -= 1
				food_points["Lemon: You have a sour personality. People see you as bright, but at times you may be bitter. "] -= 1
				food_points["Chocolate: You are mellow; and you often go with the flow. You are also intelligent and love to be the center of attention. You have a very flexible nature. Your natural enemy is a potato. "] += 1
				food_points["Potatoes : You have a starchy personality. You always dress on point, whether you are french, baked, or mashed. "] -= 1
				food_points["Pizza Crust: You are so picky and reluctant to try new foods. This means you have a stubborn tendency to complete one task before moving on to another."] -= 1
				food_points["Sushi: You have a refined character that contains an excessive amount of style and poise."] -= 1
				food_points["Banana: You are funny and never let anything get in the way of a joke! You always make your friends laugh. Your natural enemy is a lemon."] -= 1
				food_points["Shrimp: You have a selfish personality, you must stay true to meeting your goals and build your confidence. Your enemy is sushi. "] -= 1
				food_points["Bread: You have your own distinctive and taste. You are full of fun and you are easy to get along with."] -= 1
				food_points["Spaghetti: You are very genuine. Your have a very warm and comforting personality."] -= 1
#comparing herbs starts here
			if herb == 'christmastree':
				food_points['Kiwi: You are very versatile, always switching up your physical appearance to match your daily mood. Your enemy is chocolate.'] += 1
				food_points["Lemon: You have a sour personality. People see you as bright, but at times you may be bitter. "] += 1
				food_points["Chocolate: You are mellow; and you often go with the flow. You are also intelligent and love to be the center of attention. You have a very flexible nature. Your natural enemy is a potato. "] += 1
				food_points["Potatoes : You have a starchy personality. You always dress on point, whether you are french, baked, or mashed. "] += 1
				food_points["Pizza Crust: You are so picky and reluctant to try new foods. This means you have a stubborn tendency to complete one task before moving on to another."] += 1
				food_points["Sushi: You have a refined character that contains an excessive amount of style and poise."] += 1
				food_points["Banana: You are funny and never let anything get in the way of a joke! You always make your friends laugh. Your natural enemy is a lemon."] += 1
				food_points["Shrimp: You have a selfish personality, you must stay true to meeting your goals and build your confidence. Your enemy is sushi. "] += 1
				food_points["Bread: You have your own distinctive and taste. You are full of fun and you are easy to get along with."] += 1
				food_points["Spaghetti: You are very genuine. Your have a very warm and comforting personality."] += 1
			else:
				food_points['Kiwi: You are very versatile, always switching up your physical appearance to match your daily mood. Your enemy is chocolate.'] -= 1
				food_points["Lemon: You have a sour personality. People see you as bright, but at times you may be bitter. "] -= 1
				food_points["Chocolate: You are mellow; and you often go with the flow. You are also intelligent and love to be the center of attention. You have a very flexible nature. Your natural enemy is a potato. "] += 1
				food_points["Potatoes : You have a starchy personality. You always dress on point, whether you are french, baked, or mashed. "] -= 1
				food_points["Pizza Crust: You are so picky and reluctant to try new foods. This means you have a stubborn tendency to complete one task before moving on to another."] -= 1
				food_points["Sushi: You have a refined character that contains an excessive amount of style and poise."] -= 1
				food_points["Banana: You are funny and never let anything get in the way of a joke! You always make your friends laugh. Your natural enemy is a lemon."] -= 1
				food_points["Shrimp: You have a selfish personality, you must stay true to meeting your goals and build your confidence. Your enemy is sushi. "] -= 1
				food_points["Bread: You have your own distinctive and taste. You are full of fun and you are easy to get along with."] -= 1
				food_points["Spaghetti: You are very genuine. Your have a very warm and comforting personality."] -= 1
#comparing rather starts here
			if rather == 'drinkall':
				food_points['Kiwi: You are very versatile, always switching up your physical appearance to match your daily mood. Your enemy is chocolate.'] += 1
				food_points["Lemon: You have a sour personality. People see you as bright, but at times you may be bitter. "] += 1
				food_points["Pizza Crust: You are so picky and reluctant to try new foods. This means you have a stubborn tendency to complete one task before moving on to another."] += 1
				food_points["Sushi: You have a refined character that contains an excessive amount of style and poise."] += 1
				food_points["Shrimp: You have a selfish personality, you must stay true to meeting your goals and build your confidence. Your enemy is sushi. "] += 1
			elif rather == 'share':
				food_points["Chocolate: You are mellow; and you often go with the flow. You are also intelligent and love to be the center of attention. You have a very flexible nature. Your natural enemy is a potato. "] += 1
				food_points["Potatoes : You have a starchy personality. You always dress on point, whether you are french, baked, or mashed. "] += 1
				food_points["Banana: You are funny and never let anything get in the way of a joke! You always make your friends laugh. Your natural enemy is a lemon."] += 1
				food_points["Bread: You have your own distinctive and taste. You are full of fun and you are easy to get along with."] += 1
				food_points["Spaghetti: You are very genuine. Your have a very warm and comforting personality."] += 1
#comparing hallowing fruit 
			if halloween == 'strawberry':
				food_points['Kiwi: You are very versatile, always switching up your physical appearance to match your daily mood. Your enemy is chocolate.'] += 1
				food_points["Spaghetti: You are very genuine. Your have a very warm and comforting personality."] += 1
			elif halloween == 'grape':
				food_points["Sushi: You have a refined character that contains an excessive amount of style and poise."] += 1
			elif halloween == 'blueberry':
				food_points["Potatoes : You have a starchy personality. You always dress on point, whether you are french, baked, or mashed. "] += 1
			elif halloween == 'orange':
				food_points["Lemon: You have a sour personality. People see you as bright, but at times you may be bitter. "] += 1
				food_points["Pizza Crust: You are so picky and reluctant to try new foods. This means you have a stubborn tendency to complete one task before moving on to another."] += 1
				food_points["Shrimp: You have a selfish personality, you must stay true to meeting your goals and build your confidence. Your enemy is sushi. "] += 1
			elif halloween == 'banana':
				food_points["Chocolate: You are mellow; and you often go with the flow. You are also intelligent and love to be the center of attention. You have a very flexible nature. Your natural enemy is a potato. "] += 1
				food_points["Banana: You are funny and never let anything get in the way of a joke! You always make your friends laugh. Your natural enemy is a lemon."] += 2
				food_points["Bread: You have your own distinctive and taste. You are full of fun and you are easy to get along with."] += 1
			elif halloween == 'watermelon':
				food_points["Bread: You have your own distinctive and taste. You are full of fun and you are easy to get along with."] += 1
#comparing hungry ?
			if hungry_yes_no == 'sad':
				food_points['Kiwi: You are very versatile, always switching up your physical appearance to match your daily mood. Your enemy is chocolate.'] += 1
				food_points["Lemon: You have a sour personality. People see you as bright, but at times you may be bitter. "] += 1
				food_points["Chocolate: You are mellow; and you often go with the flow. You are also intelligent and love to be the center of attention. You have a very flexible nature. Your natural enemy is a potato. "] += 1
				food_points["Potatoes : You have a starchy personality. You always dress on point, whether you are french, baked, or mashed. "] += 1
				food_points["Pizza Crust: You are so picky and reluctant to try new foods. This means you have a stubborn tendency to complete one task before moving on to another."] += 1
				food_points["Sushi: You have a refined character that contains an excessive amount of style and poise."] += 1
				food_points["Banana: You are funny and never let anything get in the way of a joke! You always make your friends laugh. Your natural enemy is a lemon."] += 1
				food_points["Shrimp: You have a selfish personality, you must stay true to meeting your goals and build your confidence. Your enemy is sushi. "] += 1
				food_points["Bread: You have your own distinctive and taste. You are full of fun and you are easy to get along with."] += 1
				food_points["Spaghetti: You are very genuine. Your have a very warm and comforting personality."] += 1
			elif hungry_yes_no == 'hungry':
				food_points['Kiwi: You are very versatile, always switching up your physical appearance to match your daily mood. Your enemy is chocolate.'] += 1
				food_points["Lemon: You have a sour personality. People see you as bright, but at times you may be bitter. "] += 1
				food_points["Pizza Crust: You are so picky and reluctant to try new foods. This means you have a stubborn tendency to complete one task before moving on to another."] += 1
				food_points["Sushi: You have a refined character that contains an excessive amount of style and poise."] += 1
				food_points["Shrimp: You have a selfish personality, you must stay true to meeting your goals and build your confidence. Your enemy is sushi. "] += 1
			elif hungry_yes_no == "crazy":
				food_points['Kiwi: You are very versatile, always switching up your physical appearance to match your daily mood. Your enemy is chocolate.'] -= 1
				food_points["Lemon: You have a sour personality. People see you as bright, but at times you may be bitter. "] -= 1
				food_points["Chocolate: You are mellow; and you often go with the flow. You are also intelligent and love to be the center of attention. You have a very flexible nature. Your natural enemy is a potato. "] += 1
				food_points["Potatoes : You have a starchy personality. You always dress on point, whether you are french, baked, or mashed. "] -= 1
				food_points["Pizza Crust: You are so picky and reluctant to try new foods. This means you have a stubborn tendency to complete one task before moving on to another."] -= 1
				food_points["Sushi: You have a refined character that contains an excessive amount of style and poise."] -= 1
				food_points["Banana: You are funny and never let anything get in the way of a joke! You always make your friends laugh. Your natural enemy is a lemon."] -= 1
				food_points["Shrimp: You have a selfish personality, you must stay true to meeting your goals and build your confidence. Your enemy is sushi. "] -= 1
				food_points["Bread: You have your own distinctive and taste. You are full of fun and you are easy to get along with."] -= 1
				food_points["Spaghetti: You are very genuine. Your have a very warm and comforting personality."] -= 1
#comparing favorite_place
			if favorite_place == 'KFC':
				food_points['Kiwi: You are very versatile, always switching up your physical appearance to match your daily mood. Your enemy is chocolate.'] += 1
			elif favorite_place == 'mcdonalds':
				food_points["Banana: You are funny and never let anything get in the way of a joke! You always make your friends laugh. Your natural enemy is a lemon."] += 1
			elif favorite_place == '711':
				food_points["Chocolate: You are mellow; and you often go with the flow. You are also intelligent and love to be the center of attention. You have a very flexible nature. Your natural enemy is a potato. "] += 1
			elif favorite_place == 'chipotle':
				food_points["Shrimp: You have a selfish personality, you must stay true to meeting your goals and build your confidence. Your enemy is sushi. "] += 1
			elif favorite_place == 'pizzahut':
				food_points["Pizza Crust: You are so picky and reluctant to try new foods. This means you have a stubborn tendency to complete one task before moving on to another."] += 1
			elif favorite_place == 'chicfila':
				food_points["Bread: You have your own distinctive and taste. You are full of fun and you are easy to get along with."] += 1
			elif favorite_place == 'dominos':
				food_points["Potatoes : You have a starchy personality. You always dress on point, whether you are french, baked, or mashed. "] += 1
				food_points["Pizza Crust: You are so picky and reluctant to try new foods. This means you have a stubborn tendency to complete one task before moving on to another."] += 1
			elif favorite_place == 'tacobell':
				food_points["Lemon: You have a sour personality. People see you as bright, but at times you may be bitter. "] += 1
			elif favorite_place == 'pandaexpress':
				food_points["Spaghetti: You are very genuine. Your have a very warm and comforting personality."] += 1
			elif favorite_place == "wholefoods":
				food_points["Sushi: You have a refined character that contains an excessive amount of style and poise."] += 1

			maxi = 0
			for n in food_points:
				if food_points[n] > maxi:
					maxi = food_points[n]
#matching food item code below
			if maxi == food_points["Kiwi: You are very versatile, always switching up your physical appearance to match your daily mood. Your enemy is chocolate."]:
				food_match = foods["Kiwi: You are very versatile, always switching up your physical appearance to match your daily mood. Your enemy is chocolate."]
				for key,value in foods.iteritems():
					if value == "/static/Pictures/foodpics/kiwi.jpg":
						pic_link = key
			elif maxi == food_points["Lemon: You have a sour personality. People see you as bright, but at times you may be bitter. "]:
				food_match = foods["Lemon: You have a sour personality. People see you as bright, but at times you may be bitter. "]
				for key,value in foods.iteritems():
					if value == "/static/Pictures/foodpics/lemon.jpg":
						pic_link = key
			elif maxi == food_points["Chocolate: You are mellow; and you often go with the flow. You are also intelligent and love to be the center of attention. You have a very flexible nature. Your natural enemy is a potato. "]:
				food_match = foods["Chocolate: You are mellow; and you often go with the flow. You are also intelligent and love to be the center of attention. You have a very flexible nature. Your natural enemy is a potato. "]
				for key,value in foods.iteritems():
					if value == "/static/Pictures/foodpics/coco.jpg":
						pic_link = key	
			elif maxi == food_points["Potatoes : You have a starchy personality. You always dress on point, whether you are french, baked, or mashed. "]:
				food_match =foods["Potatoes : You have a starchy personality. You always dress on point, whether you are french, baked, or mashed. "]
				for key,value in foods.iteritems():
					if value == "/static/Pictures/foodpics/potatoes.jpg":
						pic_link = key
			elif maxi == food_points["Pizza Crust: You are so picky and reluctant to try new foods. This means you have a stubborn tendency to complete one task before moving on to another."]:
				food_match = foods["Pizza Crust: You are so picky and reluctant to try new foods. This means you have a stubborn tendency to complete one task before moving on to another."]
				for key,value in foods.iteritems():
					if value == "/static/Pictures/foodpics/pizzacrust.jpg":
						pic_link = key
			elif maxi == food_points["Sushi: You have a refined character that contains an excessive amount of style and poise."]:
				food_match = foods["Sushi: You have a refined character that contains an excessive amount of style and poise."]
				for key,value in foods.iteritems():
					if value == "/static/Pictures/foodpics/sushi.jpg":
						pic_link = key			
			elif maxi == food_points["Banana: You are funny and never let anything get in the way of a joke! You always make your friends laugh. Your natural enemy is a lemon."]:
				food_match= foods["Banana: You are funny and never let anything get in the way of a joke! You always make your friends laugh. Your natural enemy is a lemon."]
				for key,value in foods.iteritems():
					if value == "/static/Pictures/foodpics/banana.jpg":
						pic_link = key
			elif maxi == food_points["Shrimp: You have a selfish personality, you must stay true to meeting your goals and build your confidence. Your enemy is sushi. "]:
				food_match = foods["Shrimp: You have a selfish personality, you must stay true to meeting your goals and build your confidence. Your enemy is sushi. "]
				for key,value in foods.iteritems():
					if value == "/static/Pictures/foodpics/shrimp.jpg":
						pic_link = key
			elif maxi == food_points["Bread: You have your own distinctive and taste. You are full of fun and you are easy to get along with."]:
				food_match = foods["Bread: You have your own distinctive and taste. You are full of fun and you are easy to get along with."]
				for key,value in foods.iteritems():
					if value == "/static/Pictures/foodpics/bread.jpg":
						pic_link = key
			elif maxi == food_points["Spaghetti: You are very genuine. Your have a very warm and comforting personality."]:
				food_match =foods["Spaghetti: You are very genuine. Your have a very warm and comforting personality."]
				for key,value in foods.iteritems():
					if value == "/static/Pictures/foodpics/spaghetti.jpg":
						pic_link = key
			
			data = {'food': pic_link, 'picture': food_match}
			self.response.write(template.render(data))

class MatchingSongHandler(webapp2.RequestHandler):
	def post(self):
			template = env.get_template('song.html')
			songs = {"This Is What You Came For - Calvin Harris ft. Rihanna" : "https://www.youtube.com/embed/kOkQ4T5WO9E" , 
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
			song_points = {
				"This Is What You Came For - Calvin Harris ft. Rihanna" : 0,
				"Dani California - Red Hot Chili Peppers" : 0,
				"Cosmic Love - Florence and the Machine" : 0,
				"Hips Don't Lie - Shakira" : 0,
				"Stairway to Heaven - Led Zeppelin" : 0,
				"Work It - Missy Elliot" : 0,
				"Unsteady - X Ambassadors" : 0,
				"Promise - Romeo Santos ft Usher" : 0,
				"No Problem - Chance The Rapper ft. Lil Wayne & 2 Chainz" : 0,
				"Homecoming - Kanye ft. Chris Martin" : 0,
				"Viva La Vida - Coldplay" : 0,
				"Where Ya At - Drake & Future" : 0,
				"Friday - Rebecca " : 0,
				"Single Ladies - Beyonce" : 0,
				"Dancing Queen - ABBA" : 0,
				"Dream On - Aerosmith" : 0,
				"Bohemian Rhapsody - Queen" : 0,
				"Never Gonna Give You Up - Rick Astley" : 0,
				"Roses - Chainsmokers ft. Rozes" : 0
			}

			firstName = self.request.get('fandlname')
			birthday = self.request.get('birthdaymonth')
			word = self.request.get('wierdwords')
			num = self.request.get('picknum')
			clothes = self.request.get('wear')
			emotion = self.request.get('feeling')
			music = self.request.get('instrument')
			color = self.request.get('colorpick')


# using points to determine your matching song starts right here
			if firstName.lower() == 'calvin' or firstName.lower() == 'rihanna': 
				song_points["This Is What You Came For - Calvin Harris ft. Rihanna"] += 1
			elif firstName.lower() == 'beyonce':
				song_points['Single Ladies - Beyonce'] +=1
			elif firstName.lower() == 'anthony' or firstName.lower() == 'flea' or firstName.lower() == "chad" or firstName.lower == "josh":
				song_points['Dani California - Red Hot Chili Peppers'] +=1
			elif firstName.lower() == 'florence':
				song_points["Cosmic Love - Florence and the Machine"] +=1
			elif firstName.lower() == 'shakira':
				song_points["Hips Don't Lie - Shakira"] +=1
			elif firstName.lower() == 'robert' or firstName.lower() == "john" or firstName.lower() == "jimmy":
				song_points["Stairway to Heaven - Led Zeppelin"] +=1
			elif firstName.lower() == 'missy':
				song_points["Work It - Missy Elliot"] +=1
			elif firstName.lower() == 'sam' or firstName.lower() == "casey" or firstName.lower() == "noah":
				song_points["Unsteady - X Ambassadors"] +=1
			elif firstName.lower() == 'romeo' or firstName.lower() == "usher":
				song_points["Promise - Romeo Santos ft Usher"] +=1
			elif firstName.lower() == 'chance' or firstName.lower() == "michael" or firstName.lower() == "tauheed":
				song_points["No Problem - Chance The Rapper ft. Lil Wayne & 2 Chainz"] +=1
			elif firstName.lower() == 'kanye' or firstName.lower() == "chris":
				song_points["Homecoming - Kanye ft. Chris Martin"] +=1
			elif firstName.lower() == 'guy' or firstName.lower() == "johny" or firstName.lower() == "will":
				song_points["Viva La Vida - Coldplay"] +=1
			elif firstName.lower() == 'drake' or firstName.lower() == "nayvadius":
				song_points["Where Ya At - Drake & Future"] +=1
			elif firstName.lower() == "rebecca":
				song_points["Friday - Rebecca "] +=1
			elif firstName.lower() == "agnetha" or firstName.lower() == "anni-frid" or firstName.lower() == "bjorn" or firstName.lower() == "benny":
				song_points["Dancing Queen - ABBA"] +=1
			elif firstName.lower() == "steven" or firstName.lower() == "joe" or firstName.lower() == "brad" or firstName.lower() == "joey" or firstName.lower() == "tom" or firstName.lower() == "ray":
				song_points["Dream On - Aerosmith"] +=1
			elif firstName.lower() == "brian" or firstName.lower() == "roger" or firstName.lower() == "freddie":
				song_points["Bohemian Rhapsody - Queen"] +=1
			elif firstName.lower() == "rick":
				song_points["Never Gonna Give You Up - Rick Astley"] +=1
			elif firstName.lower() == "andrew" or firstName.lower() == "alex":
				song_points["Roses - Chainsmokers ft. Rozes" ] +=1	
# first line comparing birthdays
			if birthday == 'January' : 
				song_points["Dream On - Aerosmith"] +=1
		 		song_points["This Is What You Came For - Calvin Harris ft. Rihanna"] += 1
		 		song_points["Stairway to Heaven - Led Zeppelin"] +=1
		 	elif birthday == 'February':
		 		song_points["Roses - Chainsmokers ft. Rozes" ] +=1	
		 		song_points["Never Gonna Give You Up - Rick Astley"] +=1
		 		song_points["This Is What You Came For - Calvin Harris ft. Rihanna"] += 1
		 		song_points["Hips Don't Lie - Shakira"] +=1
		 	elif birthday == "March":
				song_points["Dancing Queen - ABBA"] +=1
				song_points["Homecoming - Kanye ft. Chris Martin"] +=1
			elif birthday == "April":
				song_points["No Problem - Chance The Rapper ft. Lil Wayne & 2 Chainz"] +=1
			elif birthday == "May":
				song_points["Viva La Vida - Coldplay"] +=1
			elif birthday == "June":
				song_points["Friday - Rebecca "] +=1
				song_points["Homecoming - Kanye ft. Chris Martin"] +=1
			elif birthday == "July":
				song_points["Bohemian Rhapsody - Queen"] +=1
				song_points["Promise - Romeo Santos ft Usher"] +=1
				song_points["Work It - Missy Elliot"] +=1
			elif birthday == "August":
				song_points['Dani California - Red Hot Chili Peppers'] +=1
				song_points["Cosmic Love - Florence and the Machine"] +=1
			elif birthday == "September":
				song_points["No Problem - Chance The Rapper ft. Lil Wayne & 2 Chainz"] += 2 
				song_points['Single Ladies - Beyonce'] +=1
			elif birthday == "October":
				song_points["Where Ya At - Drake & Future"] +=1
				song_points["Promise - Romeo Santos ft Usher"] +=1
			elif birthday == "November":
				song_points["Where Ya At - Drake & Future"] +=1
				song_points["Unsteady - X Ambassadors"] +=1
# #mathcing word
			if word == 'moist':
				song_points["This Is What You Came For - Calvin Harris ft. Rihanna"] += 1
				song_points['Single Ladies - Beyonce'] +=1
				song_points['Dani California - Red Hot Chili Peppers'] +=1
				song_points["Hips Don't Lie - Shakira"] +=1
				song_points["Cosmic Love - Florence and the Machine"] +=1
			elif word == "ointment":
				song_points["Stairway to Heaven - Led Zeppelin"] +=1
				song_points["Work It - Missy Elliot"] +=1
				song_points["Unsteady - X Ambassadors"] +=1
				song_points["Promise - Romeo Santos ft Usher"] +=1
				song_points["No Problem - Chance The Rapper ft. Lil Wayne & 2 Chainz"] +=1
			elif word == "yeast":
				song_points["Homecoming - Kanye ft. Chris Martin"] +=1
				song_points["Viva La Vida - Coldplay"] +=1
				song_points["Where Ya At - Drake & Future"] +=1
				song_points["Friday - Rebecca "] +=1
				song_points["Dancing Queen - ABBA"] +=1
			elif word == "sizzle":
				song_points["Dream On - Aerosmith"] +=1
				song_points["Bohemian Rhapsody - Queen"] +=1
				song_points["Never Gonna Give You Up - Rick Astley"] +=1
				song_points["Roses - Chainsmokers ft. Rozes" ] +=1
# #matching number starts here
			if num == '34':
				song_points["Dream On - Aerosmith"] +=1
				song_points["Bohemian Rhapsody - Queen"] +=1
				song_points["Never Gonna Give You Up - Rick Astley"] +=1
			elif num == "85":
				song_points["Homecoming - Kanye ft. Chris Martin"] +=3
				song_points["Viva La Vida - Coldplay"] +=3
				song_points["Where Ya At - Drake & Future"] +=3
			elif num == "11":
				song_points["Stairway to Heaven - Led Zeppelin"] +=2
				song_points["Work It - Missy Elliot"] +=2
				song_points["Unsteady - X Ambassadors"] +=2
			elif num == "94":
				song_points["This Is What You Came For - Calvin Harris ft. Rihanna"] += 5
				song_points['Single Ladies - Beyonce'] +=5
				song_points['Dani California - Red Hot Chili Peppers'] +=5
			elif num == "561":
				song_points["Roses - Chainsmokers ft. Rozes" ] +=2
				song_points["Friday - Rebecca "] +=2
				song_points["Dancing Queen - ABBA"] +=2
			elif num == "100":
				song_points["Promise - Romeo Santos ft Usher"] +=1
				song_points["No Problem - Chance The Rapper ft. Lil Wayne & 2 Chainz"] +=1
				song_points["Hips Don't Lie - Shakira"] +=1
				song_points["Cosmic Love - Florence and the Machine"] +=1
# #clothes comparison starts here
			if clothes == "grey":
				song_points["Promise - Romeo Santos ft Usher"] +=2
				song_points["No Problem - Chance The Rapper ft. Lil Wayne & 2 Chainz"] +=2
				song_points["Hips Don't Lie - Shakira"] +=2
				song_points["Cosmic Love - Florence and the Machine"] +=2
				song_points["Friday - Rebecca "] +=2
				song_points["Dancing Queen - ABBA"] +=2
			elif clothes == "orange":
				song_points["Work It - Missy Elliot"] +=2
				song_points["Unsteady - X Ambassadors"] +=2
				song_points["This Is What You Came For - Calvin Harris ft. Rihanna"] += 2
				song_points['Single Ladies - Beyonce'] +=2
				song_points['Dani California - Red Hot Chili Peppers'] +=2
				song_points["Roses - Chainsmokers ft. Rozes" ] +=2
			elif clothes == "tree":
				song_points["Dream On - Aerosmith"] +=1
				song_points["Bohemian Rhapsody - Queen"] +=1
				song_points["Never Gonna Give You Up - Rick Astley"] +=1
				song_points["Homecoming - Kanye ft. Chris Martin"] +=1
				song_points["Viva La Vida - Coldplay"] +=1
				song_points["Where Ya At - Drake & Future"] +=1
				song_points["Stairway to Heaven - Led Zeppelin"] +=1
# #emotion comarison starts here
			if emotion == 'sad':
				song_points["Promise - Romeo Santos ft Usher"] +=1
				song_points["No Problem - Chance The Rapper ft. Lil Wayne & 2 Chainz"] +=1
				song_points["Hips Don't Lie - Shakira"] +=1
			elif emotion == 'hungry':
				song_points["Cosmic Love - Florence and the Machine"] +=1
				song_points["Friday - Rebecca "] +=1
				song_points["Dancing Queen - ABBA"] +=1
				song_points["Work It - Missy Elliot"] +=1
			elif emotion == 'crazy':
				song_points["Unsteady - X Ambassadors"] +=1
				song_points["This Is What You Came For - Calvin Harris ft. Rihanna"] += 1
				song_points['Single Ladies - Beyonce'] +=2
				song_points['Dani California - Red Hot Chili Peppers'] +=1
			elif emotion == "whatmeme":
				song_points["Roses - Chainsmokers ft. Rozes" ] +=1
				song_points["Dream On - Aerosmith"] +=1
				song_points["Bohemian Rhapsody - Queen"] +=1
				song_points["Never Gonna Give You Up - Rick Astley"] +=1
			elif emotion == "whymeme":
				song_points["Homecoming - Kanye ft. Chris Martin"] +=1
				song_points["Viva La Vida - Coldplay"] +=1
				song_points["Where Ya At - Drake & Future"] +=1
				song_points["Stairway to Heaven - Led Zeppelin"] +=1
# #music comparison starts here
			if music == "trumpet":
				song_points["Promise - Romeo Santos ft Usher"] +=1
				song_points["No Problem - Chance The Rapper ft. Lil Wayne & 2 Chainz"] +=1
				song_points["Hips Don't Lie - Shakira"] +=1
			elif music == "guitar":
				song_points["Cosmic Love - Florence and the Machine"] +=1
				song_points["Friday - Rebecca "] +=1
				song_points["Dancing Queen - ABBA"] +=1
				song_points["Work It - Missy Elliot"] +=1
			elif music == "violin":
				song_points["Unsteady - X Ambassadors"] +=1
				song_points["This Is What You Came For - Calvin Harris ft. Rihanna"] += 1
				song_points['Single Ladies - Beyonce'] +=2
				song_points['Dani California - Red Hot Chili Peppers'] +=1
			elif music == "piano":
				song_points["Roses - Chainsmokers ft. Rozes" ] +=1
				song_points["Dream On - Aerosmith"] +=1
				song_points["Bohemian Rhapsody - Queen"] +=1
				song_points["Never Gonna Give You Up - Rick Astley"] +=1
			elif music == "saxophone":
				song_points["Homecoming - Kanye ft. Chris Martin"] +=1
				song_points["Viva La Vida - Coldplay"] +=1
				song_points["Where Ya At - Drake & Future"] +=1
				song_points["Stairway to Heaven - Led Zeppelin"] +=1
				val = songs["Friday - Rebecca "]
# # color comparison starts here
			if color == "red":
				song_points["Dream On - Aerosmith"] +=1
				song_points["Bohemian Rhapsody - Queen"] +=1
				song_points["Never Gonna Give You Up - Rick Astley"] +=1
			elif color == "blue":
				song_points["Homecoming - Kanye ft. Chris Martin"] += 1
				song_points["Viva La Vida - Coldplay"] +=1
				song_points["Where Ya At - Drake & Future"] +=1
			elif color == "yellow":
				song_points["Stairway to Heaven - Led Zeppelin"] +=1
				song_points["Work It - Missy Elliot"] +=1
				song_points["Unsteady - X Ambassadors"] +=1
			elif color == "black":
				song_points["This Is What You Came For - Calvin Harris ft. Rihanna"] += 1
				song_points['Single Ladies - Beyonce'] +=1
				song_points['Dani California - Red Hot Chili Peppers'] +=1
			elif color == "green":
				song_points["Roses - Chainsmokers ft. Rozes" ] +=1
				song_points["Friday - Rebecca "] +=1
				song_points["Dancing Queen - ABBA"] +=1
			elif color == "white":	
				song_points["Promise - Romeo Santos ft Usher"] +=1
				song_points["No Problem - Chance The Rapper ft. Lil Wayne & 2 Chainz"] +=1
				song_points["Hips Don't Lie - Shakira"] +=1
				song_points["Cosmic Love - Florence and the Machine"] +=1
			maxi = 0
			for n in song_points:
				if song_points[n] > maxi:
					maxi = song_points[n]
			

			if maxi == song_points["This Is What You Came For - Calvin Harris ft. Rihanna"]:
				val = songs["This Is What You Came For - Calvin Harris ft. Rihanna"]
				for key,value in songs.iteritems():
					if value == "https://www.youtube.com/embed/kOkQ4T5WO9E":
						result = key
			elif maxi == song_points["Dani California - Red Hot Chili Peppers"]:
				val = songs["Dani Californoa - Red Hot Chili Peppers"]
				for key,value in songs.iteritems():
					if value == "https://www.youtube.com/embed/Sb5aq5HcS1A":
						result = key
			elif maxi == song_points["Cosmic Love - Florence and the Machine"]:
				val = songs["Cosmic Love - Florence and the Machine"]
				for key,value in songs.iteritems():
					if value == "https://www.youtube.com/embed/2EIeUlvHAiM":
						result = key	
			elif maxi == song_points["Hips Don't Lie - Shakira"]:
				val = songs["Hips Don't Lie - Shakira"]
				for key,value in songs.iteritems():
					if value == "https://www.youtube.com/embed/DUT5rEU6pqM":
						result = key
			elif maxi == song_points["Stairway to Heaven - Led Zeppelin"]:
				val = songs["Stairway to Heaven - Led Zeppelin"]
				for key,value in songs.iteritems():
					if value == "https://www.youtube.com/embed/oW_7XBrDBAA":
						result = key
			elif maxi == song_points["Work It - Missy Elliot"]:
				val = songs["Work It - Missy Elliot"]
				for key,value in songs.iteritems():
					if value == "https://www.youtube.com/embed/cjIvu7e6Wq8":
						result = key			
			elif maxi == song_points["Unsteady - X Ambassadors"]:
				val = songs["Unsteady - X Ambassadors"]
				for key,value in songs.iteritems():
					if value == "https://www.youtube.com/embed/V0lw3qylVfY":
						result = key
			elif maxi == song_points["Promise - Romeo Santos ft Usher"]:
				val = songs["Promise - Romeo Santos ft Usher"]
				for key,value in songs.iteritems():
					if value == "https://www.youtube.com/embed/Y3XyWhrZnqE":
						result = key
			elif maxi == song_points["No Problem - Chance The Rapper ft. Lil Wayne & 2 Chainz"]:
				val = songs["No Problem - Chance The Rapper ft. Lil Wayne & 2 Chainz"]
				for key,value in songs.iteritems():
					if value == "https://www.youtube.com/embed/_2LXpNmjxMw":
						result = key
			elif maxi == song_points["Homecoming - Kanye ft. Chris Martin"]:
				val = songs["Homecoming - Kanye ft. Chris Martin"]
				for key,value in songs.iteritems():
					if value == "https://www.youtube.com/embed/LQ488QrqGE4":
						result = key
			elif maxi == song_points["Viva La Vida - Coldplay"]:
				val = songs["Viva La Vida - Coldplay"]
				for key,value in songs.iteritems():
					if value == "https://www.youtube.com/embed/Tmb7YIKqLeM":
						result = key
			elif maxi == song_points["Where Ya At - Drake & Future"]:
				val = songs["Where Ya At - Drake & Future"]
				for key,value in songs.iteritems():
					if value == "https://www.youtube.com/embed/lw3Or6eqIpI":
						result = key
			elif maxi == song_points["Friday - Rebecca "]:
				val = songs["Friday - Rebecca "]
				for key,value in songs.iteritems():
					if value == "https://www.youtube.com/embed/kfVsfOSbJY0":
						result = key
			elif maxi == song_points["Single Ladies - Beyonce"]:
				val = songs["Single Ladies - Beyonce"]
				for key,value in songs.iteritems():
					if value == "https://www.youtube.com/embed/4m1EFMoRFvY":
						result = key
			elif maxi == song_points["Dancing Queen - ABBA"]:
				val = songs["Dancing Queen - ABBA"]
				for key,value in songs.iteritems():
					if value == "https://www.youtube.com/embed/y62OlGvC-bk":
						result = key
			elif maxi == song_points["Dream On - Aerosmith"]:
				val = songs["Dream On - Aerosmith"]
				for key,value in songs.iteritems():
					if value == "https://www.youtube.com/embed/hHRNSeuvzlM":
						result = key	
			elif maxi == song_points["Bohemian Rhapsody - Queen"]:
				val = songs["Bohemian Rhapsody - Queen"]
				for key,value in songs.iteritems():
					if value == 'https://www.youtube.com/embed/fJ9rUzIMcZQ':
						result = key	
			elif maxi == song_points["Never Gonna Give You Up - Rick Astley"]:
				val = songs["Never Gonna Give You Up - Rick Astley"]
				for key,value in songs.iteritems():
					if value == "https://www.youtube.com/embed/dQw4w9WgXcQ":
						result = key	
			elif maxi == song_points["Roses - Chainsmokers ft. Rozes"]:
				val = songs["Roses - Chainsmokers ft. Rozes"]
				for key,value in songs.iteritems():
					if value == "https://www.youtube.com/embed/FyASdjZE0R0":
						result = key	
					
			data = {"link": val, 'result': result}
			self.response.write(template.render(data))

class MatchingDisneyHandler(webapp2.RequestHandler):
    def post(self):
		template = env.get_template("matching_disney.html")
		characters = {"Ariel" : "/static/Pictures/ariel.png",
					"Hiro" :"/static/Pictures/h.jpeg",
					"WALL-E": "/static/Pictures/walle.jpeg",
					"Belle" : "/static/Pictures/download.jpeg",
					"Aladdin":"/static/Pictures/aladdin.jpeg",
					"Genie":"/static/Pictures/genie.jpeg",
					"Pumba":"/static/Pictures/pumba.jpeg",
					"Rapunzel":"/static/Pictures/rapunzel.jpeg",
					"Mickey":"/static/Pictures/mickey.jpeg",
					"Minnie":"/static/Pictures/minnie.jpeg",
					"Cinderella":"/static/Pictures/cinderella.jpg",
					"Tarzan":"/static/Pictures/tarzan.jpg"
		}

		character_points = {"Ariel" : 0,
						"Hiro" : 0,
						"WALL-E": 0,
						"Belle" : 0,
						"Aladdin": 0,
						"Genie": 0,
						"Pumba": 0,
						"Rapunzel": 0,
						"Mickey": 0,
						"Minnie": 0,
						"Cinderella": 0,
						"Tarzan": 0
						}

		firstName = self.request.get('fandlname')
		place = self.request.get('place')
		color = self.request.get('color')
		num = self.request.get('picknum')
		food = self.request.get('food')
		date = self.request.get('prom')
		power = self.request.get('superpower')
		weapon = self.request.get('item')
		weather = self.request.get('climate')
		accessory = self.request.get('access')


# using points to determine your matching song starts right here
		if firstName.lower() == 'ariel' or firstName.lower() == 'eric': 
			character_points["Ariel"] += 1
		elif firstName.lower() == 'hiro':
			character_points['Hiro'] +=1
		elif firstName.lower() == 'aladdin' or firstName.lower() == 'jasmin' or firstName.lower() == "ali":
			character_points['Aladdin'] +=1
		elif firstName.lower() == 'timon':
			character_points["Pumba"] +=1
		elif firstName.lower() == 'rapunzel':
			character_points["Rapunzel"] +=1
		elif firstName.lower() == 'michael' or firstName.lower() == "mickey" or firstName.lower() == "mouse":
			character_points["Mickey"] +=1
		elif firstName.lower() == 'minnie':
			character_points['Minnie'] +=1
		elif firstName.lower() == 'cindy' or firstName.lower() == "cinderella":
			character_points['Cinderella'] +=1
		elif firstName.lower() == 'tarzan':
			character_points['Tarzan'] +=1
		elif firstName.lower() == 'walle' or firstName.lower() == "william" or firstName.lower() == "will":
				song_points["WALL-E"] +=1
# comparing place starts here
		if place == 'Sea':
			character_points["Ariel"] +=1
			character_points["Tarzan"] +=1
			character_points["Aladdin"] +=1
			character_points["Genie"] +=1
			character_points["Pumba"] +=1
		elif place == 'Ice Castle':
			character_points["Cinderella"] +=1
			character_points["Mickey"] +=1
			character_points["Minnie"] +=1
			character_points["WALL-E"] +=1
		elif place == 'Library':
			character_points["Belle"] +=1
			character_points["Hiro"] +=1
		elif place == 'A Hidden Tower':
			character_points["Rapunzel"] +=1
# comparing color starts here
		if color == "Pink":
			character_points["Rapunzel"] +=1
			character_points["Pumba"] +=1
		elif color == "Blue":
			character_points["Cinderella"] +=1
			character_points["Genie"] +=1
			character_points["Aladdin"] +=1
			character_points["Ariel"] +=1
		elif color == "green":
			character_points["Tarzan"] +=1
			character_points["Belle"] +=1
		elif color == "red":
			character_points["Mickey"] +=1
			character_points["Minnie"] +=1
			character_points["Hiro"] +=1
			character_points["WALL-E"] +=1
#comparing numbers starts here
		if num == '4':
			character_points["Hiro"] +=8
			character_points["Ariel"] +=8
		elif num == '8':
			character_points["WALL-E"] +=4
			character_points["Belle"] +=4
		elif num == '11':
			character_points["Aladdin"] +=1
			character_points["Cinderella"] +=1
		elif num == '7':
			character_points["Genie"] +=6
			character_points["Pumba"] +=6
		elif num == '6':
			character_points["Rapunzel"] +=7
			character_points["Mickey"] +=7
		elif num == '1':
			character_points["Minnie"] +=11
			character_points["Tarzan"] +=11
#comparing food starts here
		if food == 'pizza':
			character_points["Ariel"] +=1
			character_points["Hiro"] +=1
			character_points["WALL-E"] +=1
		elif food == 'salad':
			character_points["Genie"] +=1
			character_points["Aladdin"] +=1
			character_points["Pumba"] +=1
		elif food == 'macaroon':
			character_points["Rapunzel"] +=1
			character_points["Mickey"] +=1
			character_points["Minnie"] +=1
		elif food == 'waffles':
			character_points["Tarzan"] +=1
			character_points["Cinderella"] +=1
			character_points["Belle"] +=1
#comparing date starts here
		if date == 'Ariel':
			character_points["Ariel"] +=1
			character_points["Hiro"] +=1
			character_points["WALL-E"] +=1
			character_points["Genie"] +=1
			character_points["Aladdin"] +=1
			character_points["Pumba"] +=1
			character_points["Mickey"] +=1
			character_points["Tarzan"] +=1
		elif date == 'Beast':
			character_points["Ariel"] +=1
			character_points["Cinderella"] +=1
			character_points["Rapunzel"] +=1
			character_points["Belle"] +=1
			character_points["Minnie"] +=1
		elif date == 'BabyMax':
			character_points["Ariel"] +=1
			character_points["Cinderella"] +=1
			character_points["Rapunzel"] +=1
			character_points["Belle"] +=1
			character_points["Minnie"] +=1
		elif date == 'Aladdin':
			character_points["Ariel"] +=1
			character_points["Cinderella"] +=1
			character_points["Rapunzel"] +=1
			character_points["Belle"] +=1
			character_points["Minnie"] +=1
		elif date == 'Rapunzel':
			character_points["Ariel"] +=1
			character_points["Hiro"] +=1
			character_points["WALL-E"] +=1
			character_points["Genie"] +=1
			character_points["Aladdin"] +=1
			character_points["Pumba"] +=1
			character_points["Mickey"] +=1
			character_points["Tarzan"] +=1
#comparing powers
		if power == 'flying':
			character_points["Rapunzel"] +=1
			character_points["Pumba"] +=1
			character_points["Genie"] +=1
			character_points["Aladdin"] +=1
		elif power == 'Teletransportation':
			character_points["Ariel"] +=1
			character_points["WALL-E"] +=1
		elif power == 'Invisble':
			character_points["Ariel"] +=1
			character_points["Mickey"] +=1
			character_points["WALL-E"] +=1
		elif power == 'SuperhumanSpeed':
			character_points["Tarzan"] +=1
		elif power == 'strength':
			character_points["Belle"] +=1
			character_points["Minnie"] +=1
			character_points["Rapunzel"] +=1
			character_points["Cinderella"] +=1
			character_points["Tarzan"] +=1
#comparing weapons
		if weapon == 'sword':
			character_points["Tarzan"] +=1
			character_points["Aladdin"] +=1
		elif weapon == 'Rose':
			character_points["Mickey"] +=1
			character_points["Minnie"] +=1
			character_points["Cinderella"] +=1
			character_points["Rapunzel"] +=1
		elif weapon == 'Book':
			character_points["Belle"] +=1
		elif weapon == 'Robots':
			character_points["WALL-E"] +=1
		elif weapon == 'Magic':
			character_points["Pumba"] +=1
			character_points["Ariel"] +=1
			character_points["Genie"] +=1
			character_points["Aladdin"] +=1
#comparing weather
		if weather == "Storm":
			character_points["Ariel"] +=1
			character_points["Tarzan"] +=1
			character_points["Aladdin"] +=1
		elif weather == 'Sunny':
			character_points["Mickey"] +=1
			character_points["Minnie"] +=1
		elif weather == 'Cloudy':
			character_points["Pumba"] +=1
			character_points["WALL-E"] +=1
			character_points["Cinderella"] +=1
			character_points["Rapunzel"] +=1
		elif weather == 'Snow':
			character_points["Belle"] +=1
		elif weather == 'Windy':
			character_points["Genie"] +=1
			character_points["Hiro"] +=1
# comparing accessory
		if accessory == 'Tiara':
			character_points["Ariel"] +=1
			character_points["Cinderella"] +=1
			character_points["Rapunzel"] +=1
			character_points["Belle"] +=1
		elif accessory == "Hat":
			character_points["Pumba"] +=1
			character_points["Mickey"] +=1
			character_points["Minnie"] +=1
		elif accessory == "slipper":
			character_points["Genie"] +=1
			character_points["Aladdin"] +=1
		elif accessory == "helmet":
			character_points["WALL-E"] +=1
			character_points["Hiro"] +=1
			character_points["Tarzan"] +=1

		maxi = 0
		for n in character_points:
			if character_points[n] > maxi:
				maxi = character_points[n]
			

		if maxi == character_points["Ariel"]:
			pic = characters["Ariel"]
			for key,value in characters.iteritems():
				if value == "/static/Pictures/ariel.png":
					char = key
		elif maxi == character_points["Hiro"]:
			pic = characters["Hiro"]
			for key,value in characters.iteritems():
				if value == "/static/Pictures/h.jpeg":
					char = key
		elif maxi == character_points["WALL-E"]:
			pic = characters["WALL-E"]
			for key,value in characters.iteritems():
				if value == "/static/Pictures/walle.jpeg":
					char = key	
		elif maxi == character_points["Belle"]:
			pic = characters["Belle"]
			for key,value in characters.iteritems():
				if value == "/static/Pictures/download.jpeg":
					char = key
		elif maxi == character_points["Aladdin"]:
			pic = characters["Aladdin"]
			for key,value in characters.iteritems():
				if value == "/static/Pictures/aladdin.jpeg":
					char = key
		elif maxi == character_points["Genie"]:
			pic = characters["Genie"]
			for key,value in characters.iteritems():
				if value == "/static/Pictures/genie.jpeg":
					char = key			
		elif maxi == character_points["Pumba"]:
			pic = characters["Pumba"]
			for key,value in characters.iteritems():
				if value == "/static/Pictures/pumba.jpeg":
					char = key
		elif maxi == character_points["Rapunzel"]:
			pic = characters["Rapunzel"]
			for key,value in characters.iteritems():
				if value == "/static/Pictures/rapunzel.jpeg":
					char = key
		elif maxi == character_points["Mickey"]:
			pic = characters["Mickey"]
			for key,value in characters.iteritems():
				if value == "/static/Pictures/mickey.jpeg":
					char = key
		elif maxi == character_points["Minnie"]:
			pic = characters["Minnie"]
			for key,value in characters.iteritems():
				if value == "/static/Pictures/minnie.jpeg":
					char = key
		elif maxi == character_points["Cinderella"]:
			pic= characters["Cinderella"]
			for key,value in characters.iteritems():
				if value == "/static/Pictures/cinderella.jpg":
					char = key
		elif maxi == character_points["Tarzan"]:
			pic = characters["Tarzan"]
			for key,value in characters.iteritems():
				if value == "/static/Pictures/tarzan.jpg":
					char = key
		
		data = {'character': char, 'picture': pic}
		self.response.write(template.render(data))

 




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/home', HomeHandler),
    ('/song_quiz', SongHandler),
    ('/matching_song', MatchingSongHandler),
    ('/disney', DisneyHandler),
    ('/food', foodHandler),
    ('/matching_food', MatchingFoodHandler),
    ('/matching_disney', MatchingDisneyHandler),
], debug=True)
