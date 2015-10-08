# Python Programming Review
# file name: python_review11_objects.py
# JetBrains PyCharm 4.5.4 under Python 3.5.0

import random  # random number generator
import sys     # sys module
import os      # operating system

# the concept of object oriented programming allows us
# to model real world things using code. Just like every
# real world object has attributes like color, height & weight
# And every real world object has abilities like walk, talk &
# eat. we're going to define attributes using variables inside
# of things called classes.
# And the abilities are just going to be functions.

# define real world object using a class
class Animal:
    # create attribute name
    # by proceeding these variables with two underscores
    # these are going to be private
    __name = "" # "" or None signifies lack of a value
    # height
    __height = 0  # private
    # weight
    __weight = 0  # private
    # sound
    __sound = 0   # private
    # if we want to change these values (above) we will need
    # to use a function inside the class that is going to
    # allow us to change it.

    # to get those values we will need to use a function inside the class.

    # if we want to set the name, self allows an object to refer
    # to itself inside of the class
    def set_name(self, name):
        self.__name = name
    # get the name since its private
    def get_name(self):
        return  self.__name

    # this is encapsulation, it allows us to say is the name they
    # passed in here (self, name) valid and if it is we will set it
    # verifying that the data is good