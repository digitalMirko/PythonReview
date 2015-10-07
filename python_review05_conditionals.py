# Python Programming Review
# file name: python_review05_conditionals.py
# JetBrains PyCharm 4.5.4 under Python 3.5.0

import random  # random number generator
import sys     # sys module
import os      # operating system

# Statements if else elif are used to perform different actions
# based off of different conditions, those conditions will be
# == , != , > , >= , < , <=
# The if statement will execute code if a condition is met
# note: white space is used to group blocks of code inside of python

age = 22

if age > 16 :
    print('You are old enough to drive')
else :
    print('You are not old enough to drive')

# checking for multiple conditions
# the age is greater than or equal to 21
if age >= 21 :
    print('You are old enough to drive a tractor trailer')
# the age is greater than or equal to 16
elif age >= 16 :
    print('You are old enough to drive a car')
# else any other condition not met above
else :
    print("You are not old enough to drive")
# above example shows that ' or " quotes don't really matter


# combine conditions with logical operators using: and  or  not
# celebrate someones birthday between the ages of 1 and 18
if ((age >= 1) and (age <= 18)):
    print("You are a birthday")
# the age is equal to 21 or age is greater or equal to 65
elif (age == 21) or (age >= 65):
    print("You get a birthday too")
# the age is not equal to 30
elif not(age == 30):
    print("You don't get a birthday either")
# else any other condition not met above
else:
    print("You get a birthday party yeah!")

# Once your condition is met we dont go any check anything else