# Python Programming Review
# file name: python_review09_strings.py
# JetBrains PyCharm 4.5.4 under Python 3.5.0

import random  # random number generator
import sys     # sys module
import os      # operating system

# define string
long_string = "I'll catch you if you fall - The Floor"
# print out the 1st four characters, 0 for the 1st index and 4
print(long_string[0:4])  # outputs: I'll

# print the last 5 characters
print(long_string[-5:])  # outputs: Floor

# print up everything to the last 5 characters
print(long_string[:-5])  # outputs: I'll catch you if you fall - The

# you can concatenate or join two strings together using a sub-string
print(long_string[:4] + " be there")  # outputs: I'll be there

# handle formatting with strings using print command
# %c: character, %s: string, %d: signed integer, %.5f: floating point number with 5 places
print("%c is my %s letter and my number %d number is %.5f" %
      ('X', 'favorite', 1, .14))
# outputs: X is my favorite letter and my number 1 number is 0.14000

# capitalize the first letter of a string
print(long_string.capitalize())
# outputs: I'll catch you if you fall - the floor

# return the index value of the start of a String, word Floor, 33rd character
print(long_string.find("Floor"))  # outputs: 33

# return true of all the characters entered in a String or of all letters
print(long_string.isalpha())  # outputs: False

# make sure everything's a number
print(long_string.isalnum())  # outputs: False

# get the length of our String
print(len(long_string))  # outputs: 38

# place a specific word with another word, replace Floor with Ground
print(long_string.replace("Floor", "Ground"))
# outputs: I'll catch you if you fall - The Ground

# strip white space, theres no white space
print(long_string.strip())  # outputs: I'll catch you if you fall - The Floor

# split a string into a list
# how we want strings to be separated with a space
quote_list = long_string.split(" ")
print(quote_list)
# outputs: ["I'll", 'catch', 'you', 'if', 'you', 'fall', '-', 'The', 'Floor']
