from user import User

import random

class Teacher(User):

    knowledge = ['1']
    
    def __init__(self, name, last):
        self.first_name = name
        self.last_name = last

    def teach(self):
        return self.knowledge[0]


        

    
