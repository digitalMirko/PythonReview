# Python Programming Review
# file name: python_review16_polymorphism.py
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

class Dog(Animal):
    __owner = ""   # every dog but not Animal gonna have an owner

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self, owner):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {} " \
               "His owner is {}".format(self.get_name(),
                                        self.get_height(),
                                        self.get_weight(),
                                        self.get_sound(),
                                        self.__owner)

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)

spot = Dog("Spot", 53, 27,"Ruff", "Mirko")

print(spot.toString())
# output: Spot is 53 cm tall and 27 kilograms and says Ruff His owner is Mirko

# Polymorphism: it allows you to refer to objects as their super class
# and then automatically have the correct functions called automatically
# Class AnimalTesting
class AnimalTesting:
    # function get_type that receives animal objects
    def get_type(self, animal):
        # refer to animal and get type
        animal.get_type()

# test animals object of type AnimalTesting
test_animals = AnimalTesting()

# test animals get type - pass in cat object
# actually an animal object
test_animals.get_type(cat)    # outputs: Animal
# test animals get type - pass in dog object named spot
test_animals.get_type(spot)   # outputs: Dog

# multiple sounds example, earlier we didnt pass in any
# pass in 4
spot.multiple_sounds(4)  # output: RuffRuffRuffRuff

# pass in nothing
spot.multiple_sounds()   # output: Ruff

