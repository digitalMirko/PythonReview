# Python Programming Review
# file name: python_review06_loops.py
# JetBrains PyCharm 4.5.4 under Python 3.5.0

import random  # random number generator
import sys     # sys module
import os      # operating system

# looping allows us to perform an action a set number of times
# for loops, ex. perform something 10 times
# start at 0 work up to 10 but not 10, prints 10 digits
for x in range(0,10):
    print(x, ' ', end="")
    # outputs: 0  1  2  3  4  5  6  7  8  9

# print new line
print('\n')

# for loops to jump through or cycle through a list
grocery_list = ['Juice','Tomatoes','Potatoes','Bananas']

for y in grocery_list :
    print(y)
    """ outputs:
        Juice
        Tomatoes
        Potatoes
        Bananas """

print('\n') # print new line

# define a list of numbers to cycle through, works like a
# list would but you are defining it in the loop
for x in [2,4,6,8,10]:
    print(x)
    """ outputs:
        2
        4
        6
        8
        10  """

print('\n') # print new line

# double up for loops to cycle through a list
# have a list of lists
num_list = [[1,2,3],[10,20,30],[100,200,300]]

# cycle through using a for loop
# range up to 0,1,2,3 up to 3 but doesnt include 3
for x in range(0,3):
    # range up to 0,1,2,3 up to 3 but doesnt include 3
    for y in range(0,3):
        print(num_list[x][y])
        # prints out in order
        """outputs:
            1
            2
            3
            10
            20
            30
            100
            200
            300 """

