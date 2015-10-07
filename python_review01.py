# Python Programming Review
# file name: python_review01.py
# JetBrains PyCharm 4.5.4 under Python 3.5.0

import random  # random number generator
import sys     # sys module
import os      # operating system

# simple hello world
print("Hello World") #output: Hello World

# single line comment example
'''
Multiline comment example
'''

# variable: a place we store values
name = "Mirko"  # String named "Mirko"
# print out variable
###  Git comment change test (10/6/2015)
print(name)  #output: Mirko
name = 15
print(name)  #output: 15
# Variable has to start with a letter then it can have
# numbers or underscores

# 5 main data types in python
# Numbers, Strings, Lists, Tuples, Dictionaries

# 7 Different Arithmetic operators: Ex.
# plus: +
print("5 + 2 = ", 5+2) # outputs: 5 + 2 =  7

# minus: -
print("5 - 2 = ", 5-2) # outputs: 5 - 2 =  3

# multiplication: *
print("5 * 2 = ", 5*2) # outputs: 5 * 2 =  10

# division: /
print("5 / 2 = ", 5/2) # outputs: 5 / 2 =  2.5

# modulus: %  remainder
print("5 % 2 = ", 5%2) # outputs: 5 % 2 =  1

# exponential calculation: **
print("5 ** 2 = ", 5**2) # outputs: 5 ** 2 =  25

# floor division: //  division where answer is rounded down
print("5 // 2 = ", 5//2) # outputs: 5 // 2 =  2

# Order of operation matters:
# if you have multiplication or division they will be performed
# before addition or subtraction. Ex.

#       String        ,      Arithmetic
print("1 + 2 - 3 * 2 =", 1 + 2 - 3 * 2)
# output: 1 + 2 - 3 * 2 = -3

# have different values then this one
#       String           ,   Arithmetic
print("(1 + 2 - 3) * 2 =", (1 + 2 - 3) * 2)
# output: (1 + 2 - 3) * 2 = 0
# use braces when you can when ever you are working with arithmetic

# String is just going to be a String of characters, numbers between
# single(') or double(") quotes, if you want to put a quote in there
# use a \" or \'
quote = "\"Always remember you are unique"

# multi line string
multi_line_quote = '''just
like everyone else'''

# join together
new_string = quote + multi_line_quote

# format using print
print("%s %s %s" % ('I Like the quote', quote, multi_line_quote))
# output: I Like the quote "Always remember you are unique just like everyone else

# printing things out to the screen without having a new line show up every time
print("I don't like ", end="")  # end="" gets rid of the new line
print("newlines")
# output: I don't like newlines

# printing a new line \n
print('\n')      # prints new line
print('\n'* 5)   # prints 5 new lines
