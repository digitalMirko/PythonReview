# Python Programming Review
# file name: python_review15_method_overloading.py
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

    def get_type(self):
        print("Animal") #outputs: Animal

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self.__name,
                                                                     self.__height,
                                                                     self.__weight,
                                                                     self.__sound)
cat = Animal('Whiskers', 33, 10, 'Meow')

print(cat.toString())
# outputs: Whiskers is 33 cm tall and 10 kilograms and says Meow

# Inheritance: all it means is when you inherit from another class that your
# automatically going to get all the variables, methods or functions that
# are created in the class you are inheriting from.
# Class called Dog, inherit from the Animal class
class Dog(Animal):
    # automatically get every variable and function already in the Animal class
    # give it a name like owner
    __owner = ""   # every dog but not Animal gonna have an owner

    # then over right the constructor for the Animal class
    # i want to do something more specific here since its a dog
    # still require them to enter a: name, height, weight, sound
    # but now i also require them to enter an owner name
    def __init__(self, name, height, weight, sound, owner):
        # set the owner, make it equal to the owner value they passed in
        self.__owner = owner
        # if we want the name, height, weight, sound to be handled by
        # the Animal super classes constructor on top
        # super, its a super class, then Dog, self, init then pass in
        # the name, height, weight, sound
        super(Dog, self).__init__(name, height, weight, sound)

    # Allow them to set the owner, owner passed here
    def set_owner(self, owner):
        # self owner, owner value passed in
        self.__owner = owner

    # Do the same thing to get the owner
    def get_owner(self, owner):
        return self.__owner

    # define get type
    def get_type(self):
        # print we are using a Dog object
        print("Dog")

    # override functions on our super class, change the toSting, add the __owner
    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {} " \
               "His owner is {}".format(self.get_name(),
                                        self.get_height(),
                                        self.get_weight(),
                                        self.get_sound(),
                                        self.__owner)

# Method overloading: you are able to perform different tasks based
# off of the attributes that are sent in
# function multiple sounds, want them to have the option to send in
# how many times we want our dog bark in, set the attribute how_many
# equal to none, which means its going to be ok for them to not send in
# how many barks our dog will make
    def multiple_sounds(self, how_many=None):
        # if how many is None
        if how_many is None:
            print(self.get_sound())
    # else if how many was passed in, get sound and print out how many
    # times they wanted it printed out
        else:
            print(self.get_sound() * how_many)
# a way of getting around method overloading
#this example just shows we don't require attributes to be sent into our function

# create dog object, named Spot, 53cm tall, 27kg weight, sound: Ruff, owner: Mirko
spot = Dog("Spot", 53, 27,"Ruff", "Mirko")

print(spot.toString())
# output: Spot is 53 cm tall and 27 kilograms and says Ruff His owner is Mirko
