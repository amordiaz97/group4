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
result = { }



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
	def post (self):
			template = env.get_template('food.html')
			foods = { "Kiwi: You are very versatile, always switching up your physical appearance to match your daily mood. Your enemy is chocolate." : "kiwi.jpg", 
			"Lemon: You have a sour personality. People see you as bright, but at times you may be bitter. " : "lemon.jpg", 
			"Chocolate: You are mellow; and you often go with the flow. You are also intelligent and love to be the center of attention. You have a very flexible nature. Your natural enemy is a potato. ": "chocolate.jpg",
			"Potatoes : You have a starchy personality. You always dress on point, whether you are french, baked, or mashed. " : "potatoes.jpg", 
			"Pizza Crust: You are so picky and reluctant to try new foods. This means you have a stubborn tendency to complete one task before moving on to another." : "pizzacrust.jpg",
			"Sushi: You have a refined character that contains an excessive amount of style and poise." : "sushi.jpg",
			"Banana: You are funny and never let anything get in the way of a joke! You always make your friends laugh. Your natural enemy is a lemon." :" banana.jpg",
			"Shrimp: You have a selfish personality, you must stay true to meeting your goals and build your confidence. Your enemy is sushi. " : "shrimp.jpg",
			"Bread: You have your own distinctive and taste. You are full of fun and you are easy to get along with." : "bread.jpg",
			"Bread: You have your own distinctive and taste merits. You are full of fun and you are easy to get along with." : "bread.jpg",
			"Spaghetti: You are very genuine. Your have a very warm and comforting personality.":  "spaghetti.jpg"
		}

class MatchingSongHandler(webapp2.RequestHandler):
    def post(self):
            template = env.get_template('song.html')
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

            firstName = self.request.get('fandlname')
            birthday = self.request.get('birthdaymonth')
            word = self.request.get('wierdwords')
            num = self.request.get('picknum')
            clothes = self.request.get('wear')
            emotion = self.request.get('feeling')
            music = self.request.get('instrument')
            color = self.request.get('colorpick')


# this conditional will go through the names entered first
            if firstName.lower() == 'beyonce': 
                if color == "blue":
                    val = songs["Single Ladies - Beyonce"]
                    for key, value in songs.iteritems():
                        if value == "https://www.youtube.com/embed/4m1EFMoRFvY":
                            result = key
                else:
                    val = songs["Crazy in Love - Beyonce"]
                    for key, value in songs.iteritems():
                        if value == "https://www.youtube.com/embed/ViwtNLUqkMY":
                            result = key
                data = {"link": val, 'result': result}
            elif firstName.lower() == 'calvin' or firstName.lower() == 'rihanna': 
                val= songs['This Is What You Came For - Calvin Harris ft. Rihanna']
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/kOkQ4T5WO9E":
                            result = key
                data = {"link": val, 'result': result}
            elif firstName.lower() == 'anthony' or firstName.lower() == 'flea' or firstName.lower() == "chad" or firstName.lower == "josh":
                val = songs["Dani California - Red Hot Chili Peppers"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/Sb5aq5HcS1A":
                            result = key
                data = {"link": val, 'result': result}
            elif firstName.lower() == 'florence':
                val = songs["Cosmic Love - Florence and the Machine"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/2EIeUlvHAiM":
                            result = key
                data = {"link": val, 'result': result}
            elif firstName.lower() == 'shakira':
                val = songs["Hips Don't Lie - Shakira"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/DUT5rEU6pqM":
                            result = key
                data = {"link": val, 'result': result}
            elif firstName.lower() == 'robert' or firstName.lower() == "john" or firstName.lower() == "jimmy":
                val = songs["Stairway to Heaven - Led Zeppelin"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/oW_7XBrDBAA":
                            result = key
                data = {"link": val, 'result': result}
            elif firstName.lower() == 'missy':
                val = songs["Work It - Missy Elliot"]
                for key, value in songs.iteritems():
                    if val == "https://www.youtube.com/embed/cjIvu7e6Wq8":
                            result = key
                data = {"link": value, 'result': result}
            elif firstName.lower() == 'sam' or firstName.lower() == "casey" or firstName.lower() == "noah":
                val = songs["Unsteady - X Ambassadors"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/V0lw3qylVfY":
                            result = key
                data = {"link": val, 'result': result}
            elif firstName.lower() == 'romeo' or firstName.lower() == "usher":
                val = songs["Promise - Romeo Santos ft Usher"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/Y3XyWhrZnqE":
                            result = key
                data = {"link": val, 'result': result}
            elif firstName.lower() == 'chance' or firstName.lower() == "michael" or firstName.lower() == "tauheed":
                val = songs["No Problem - Chance The Rapper ft. Lil Wayne & 2 Chainz"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/_2LXpNmjxMw":
                            result = key
                data = {"link": val, 'result': result}
            elif firstName.lower() == 'kanye' or firstName.lower() == "chris":
                val = songs["Homecoming - Kanye ft. Chris Martin"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/_2LXpNmjxMw":
                            result = key
                data = {"link": val, 'result': result}
            elif firstName.lower() == 'guy' or firstName.lower() == "johny" or firstName.lower() == "will":
                val = songs["Viva La Vida - Coldplay"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/Tmb7YIKqLeM":
                            result = key
                data = {"link": val, 'result': result}
            elif firstName.lower() == 'drake' or firstName.lower() == "nayvadius":
                val = songs["Where Ya At - Drake & Future"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/lw3Or6eqIpI":
                            result = key
                data = {"link": val, 'result': result}
            elif firstName.lower() == "rebecca":
                val = songs["Friday - Rebecca "]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/kfVsfOSbJY0":
                            result = key
                data = {"link": val, 'result': result}
            elif firstName.lower() == "agnetha" or firstName.lower() == "anni-frid" or firstName.lower() == "bjorn" or firstName.lower() == "benny":
                val = songs["Dancing Queen - ABBA"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/y62OlGvC-bk":
                            result = key
                data = {"link": val, 'result': result}
            elif firstName.lower() == "steven" or firstName.lower() == "joe" or firstName.lower() == "brad" or firstName.lower() == "joey" or firstName.lower() == "tom" or firstName.lower() == "ray":
                val = songs["Dream On - Aerosmith"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/hHRNSeuvzlM":
                            result = key
                data = {"link": val, 'result': result}
            elif firstName.lower() == "brian" or firstName.lower() == "roger" or firstName.lower() == "freddie":
                val = songs["Bohemian Rhapsody - Queen"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/fJ9rUzIMcZQ":
                            result = key
                data = {"link": val, 'result': result}
            elif firstName.lower() == "rick":
                val = songs["Never Gonna Give You Up - Rick Astley"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/dQw4w9WgXcQ":
                            result = key
                data = {"link": val, 'result': result}
            elif firstName.lower() == "andrew" or firstName.lower() == "alex":
                val = songs["Roses - Chainsmokers ft. Rozes"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/FyASdjZE0R0":
                            result = key
                data = {"link": val, 'result': result}  
# first line comparing birthdays
            elif birthday == 'September': 
                if color == "blue":
                    val = songs["Single Ladies - Beyonce"]
                    for key, value in songs.iteritems():
                        if value == "https://www.youtube.com/embed/4m1EFMoRFvY":
                            result = key
                else:
                    val = songs["Crazy in Love - Beyonce"]
                    for key, value in songs.iteritems():
                        if value == "https://www.youtube.com/embed/ViwtNLUqkMY":
                            result = key
                data = {"link": val, 'result': result}
            elif birthday == "January": 
                val= songs['This Is What You Came For - Calvin Harris ft. Rihanna']
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/kOkQ4T5WO9E":
                            result = key
                data = {"link": val, 'result': result}
            elif birthday == "October":
                val = songs["Dani California - Red Hot Chili Peppers"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/Sb5aq5HcS1A":
                            result = key
                data = {"link": val, 'result': result}
            elif birthday == "February":
                val = songs["Hips Don't Lie - Shakira"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/DUT5rEU6pqM":
                            result = key
                data = {"link": val, 'result': result}
            elif birthday == "July":
                val = songs["Work It - Missy Elliot"]
                for key, value in songs.iteritems():
                    if val == "https://www.youtube.com/embed/cjIvu7e6Wq8":
                            result = key
                data = {"link": value, 'result': result}
            elif birthday == "June":
                val = songs["Unsteady - X Ambassadors"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/V0lw3qylVfY":
                            result = key
                data = {"link": val, 'result': result}
            elif birthday == "April":
                val = songs["No Problem - Chance The Rapper ft. Lil Wayne & 2 Chainz"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/_2LXpNmjxMw":
                            result = key
                data = {"link": val, 'result': result}
            elif birthday == "March":
                val = songs["Viva La Vida - Coldplay"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/Tmb7YIKqLeM":
                            result = key
                data = {"link": val, 'result': result}
            elif birthday == "November":
                val = songs["Where Ya At - Drake & Future"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/lw3Or6eqIpI":
                            result = key
                data = {"link": val, 'result': result}
            elif birthday == "August":
                val = songs["Bohemian Rhapsody - Queen"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/fJ9rUzIMcZQ":
                            result = key
                data = {"link": val, 'result': result}
            elif birthday == "December":
                val = songs["Dancing Queen - ABBA"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/y62OlGvC-bk":
                            result = key
                data = {"link": val, 'result': result}
#mathcing word
            elif word == 'moist':
                val = songs["Cosmic Love - Florence and the Machine"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/2EIeUlvHAiM":
                            result = key
                data = {"link": val, 'result': result}
            elif num == "94":
                val = songs["Stairway to Heaven - Led Zeppelin"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/oW_7XBrDBAA":
                            result = key
                data = {"link": val, 'result': result}
            elif clothes == "grey":
                val = songs["Promise - Romeo Santos ft Usher"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/Y3XyWhrZnqE":
                            result = key
                data = {"link": val, 'result': result}
            elif emotion == "whymeme":
                val = songs["Homecoming - Kanye ft. Chris Martin"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/_2LXpNmjxMw":
                            result = key
                data = {"link": val, 'result': result}
            elif emotion == "sad":
                val = songs["Never Gonna Give You Up - Rick Astley"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/dQw4w9WgXcQ":
                            result = key
                data = {"link": val, 'result': result}
            elif music == "violin":
                val = songs["Friday - Rebecca "]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/kfVsfOSbJY0":
                            result = key
                data = {"link": val, 'result': result}
            elif color == "red":
                val = songs["Dream On - Aerosmith"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/hHRNSeuvzlM":
                            result = key
                data = {"link": val, 'result': result}  
            elif color == "white":
                val = songs["Roses - Chainsmokers ft. Rozes"]
                for key, value in songs.iteritems():
                    if value == "https://www.youtube.com/embed/FyASdjZE0R0":
                            result = key
                data = {"link": val, 'result': result}                                      #
            self.response.write(template.render(data))


    

class MatchingFoodHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("matching_food.html")
        self.response.write(template.render())

class MatchingDisneyHandler(webapp2.RequestHandler):
    def get(self):
        characters = {"Ariel" : "ariel.png",
        "Hiro" :"h.jpeg",
        "WALL-E": "walle.jpeg",
        "Belle" : "download.jpeg",
        "Aladdin":"aladdin.jpeg",
        "Genie":"genie.jpeg",
        "Pumba":"pumba.jpeg",
        "Rapunzel":"rapunzel.jpeg",
        "Mickey":"mickey.jpeg",
        "Minnie":"minnie.jpeg",
        "Cinderella":"cinderella.jpg",
        "Tarzan":"tarzan.jpg"
        }

        template = env.get_template("matching_disney.html")
        self.response.write(template.render())



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
