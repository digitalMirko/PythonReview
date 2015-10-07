# Python Programming Review
# file name: python_review07_while_loops.py
# JetBrains PyCharm 4.5.4 under Python 3.5.0

import random  # random number generator
import sys     # sys module
import os      # operating system

# while loops are going to be used when you have no idea
# ahead of time how many times you are going to need to loop

# Generate a random number, from 0 to 99
random_num = random.randrange(0,100)
# while random number is not 15 do...
while(random_num != 15):
    # prints random number
    print(random_num)
    # gets another random number, then when it gets 15, it jumps out
    # of the loop, if you didn't add this, an infinite loop occurs
    random_num = random.randrange(0,100)
    """ outputs:
        59
        94
        13
        52
        83
        22
        7 """
print('\n')
# Use a while loop like a for loop,
i = 0 # create an iterator
# while i is less than or equal to 20
while(i <= 20):
    # print out all the even numbers
    if(i%2 == 0):
        print(i)
    # if i is equal to 9
    elif(i == 9):   # print up to 9
        break       # then break out of loop
    else:
        # increment value of i by 1
        i += 1  # i = i + 1
        # continue skips the rest of the stuff and jumps back to the beginning
        continue
    i += 1  # increment i
""" outputs:
    0
    2
    4
    6
    8 """
