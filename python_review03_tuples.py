# Python Programming Review
# file name: python_review03_tuples.py
# JetBrains PyCharm 4.5.4 under Python 3.5.0

import random  # random number generator
import sys     # sys module
import os      # operating system

"""
A tuple is a sequence of immutable Python objects.
Tuples are sequences, just like lists. The differences between
tuples and lists are, the tuples cannot be changed unlike lists
and tuples use parentheses, whereas lists use square brackets.
"""
# sometimes you have data that you don't want to be easily changed
pi_tuple = (3,1,4,1,5,9)
print(pi_tuple)   # output: (3, 1, 4, 1, 5, 9)

# if you need to change a tuple you can change it into a list
# then change it there, then convert back to a tuple
# convert tuple into a list
new_tuple = list(pi_tuple)
print(new_tuple)  # output: [3, 1, 4, 1, 5, 9]
# convert list back into a tuple
new_list = tuple(new_tuple)
print(new_list)   # output: (3, 1, 4, 1, 5, 9)

# length of a tuple
len(new_tuple)
print(len(new_tuple)) # output: 6

# minimum of a tuple
min(new_tuple)
print(min(new_tuple)) # output: 1

# maximum of a tuple
max(new_tuple)
print(max(new_tuple)) # output: 9

