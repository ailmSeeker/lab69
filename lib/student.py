#!/usr/bin/env python

from user import User

class Student(User):
    knowledge = []

    def __init__(self, name, last):
        self.first_name = name
        self.last_name = last


    def learn(self,data):
        self.knowledge.append(data)
        return self.knowledge


