from datetime import date, datetime
import random

class Cmd():
    greetings = [
        'Hello ',
        'Hi ',
        'Greetings ',
        'Hey '
    ]
    
    messages = [
        ', ',
        ', ',
        ', '
    ]

    def __init__(self):
        """
        Constructor
        """
    
    def about(self):
        return '```---- About Me ----```'

    def signUpMessage(self, user):
        return ':sun_with_face: ' + random.choice(self.greetings) + user + ', thank you for using our service! A message is on the way for further steps! Hang tight!' 
