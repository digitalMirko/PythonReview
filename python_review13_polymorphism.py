# Python Programming Review
# file name: python_review13_polymorphism.py
# JetBrains PyCharm 4.5.4 under Python 3.5.0

import random  # random number generator
import sys     # sys module
import os      # operating system

class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def set_height(self, height):
        self.height = height

    def set_weight(self, weight):
        self.__weight = weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_name(self):
        return  self.__name

    def get_height(self):
        return  self.__height

    def get_weight(self):
        return  self.__weight

    def get_sound(self):
        return  self.__sound

    # Polymorphism
    def get_type(self):
        # print out the object name, class name
        print("Animal") #outputs: Animal

    # print out all information to the screen
    def toString(self):
        # another way of formatting output using {}
        # for the name, height, weight and sound
        return "{} is {} cm tall and {} kilograms and says {}".format(self.__name,
                                                                     self.__height,
                                                                     self.__weight,
                                                                     self.__sound)

# look at how it will look as an object
# object called cat, type Animal, call constructor ('Whiskers', 33 cm tall
# 10 kg in weight and likes to say Meow
cat = Animal('Whiskers', 33, 10, 'Meow')

print(cat.toString())
# outputs: Whiskers is 33 cm tall and 10 kilograms and says Meow
