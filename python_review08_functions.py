# Python Programming Review
# file name: python_review08_functions.py
# JetBrains PyCharm 4.5.4 under Python 3.5.0

import random  # random number generator
import sys     # sys module
import os      # operating system

# functions allow us to both re-use and write more readable code
# define a function that adds numbers
# define a function, function name (parameters it receives)
def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum # return something to the caller of this function

# make sure you define your functions before you call them
# calling function below
print(addNumber(1, 4))   # outputs: 5

# also assign it to a String
string = addNumber(1, 4) # works the same way when called

# note even though sumNum is created inside the variable up above
# it is not available outside it, it doesnt exist outside
# unresolved reference error thrown, its not defined, out of scope
# print(sumNum)

# get input from the user
print('What is your name')  # outputs: What is your name

# get input from user using sys.stdin.readline()
name = sys.stdin.readline()

# prints out Hello with persons name entered
print('Hello ', name)  # outputs Hello Mirko
