# Python Programming Review
# file name: python_review12_constructors.py
# JetBrains PyCharm 4.5.4 under Python 3.5.0

import random  # random number generator
import sys     # sys module
import os      # operating system

class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    # Another thing inside of classes,
    # Constructors: called to setup or initialize an object
    # def: define, constructor is two underscores init then two more underscores
    # In this situation when ever an object is created, we are going
    # to demand all the values be passed in here
    # name, height, weight, sound
    def __init__(self, name, height, weight, sound):
        # then when passed in we want them to be changed or defined
        # initializing them, setting up those objects
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
    # create setters and getters for all of them
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