# Python Programming Review
# file name: python_review02_lists.py
# JetBrains PyCharm 4.5.4 under Python 3.5.0

import random  # random number generator
import sys     # sys module
import os      # operating system

# List will allow you to create a list of value and then
# manipulate them, then each value will have an index
# with the first one having the index of 0
# An index is like a label so we can find ourselves around

# create a grocery_list, put everything you want to store inside
# of the brackets, they can be Strings, numbers, different data
# types if you like, make sure they are all in quotes
grocery_list = ['Juice', 'Tomatoes', 'Potatoes','Bananas']
# printing first item in the list
print('First Item', grocery_list[0])
# output: First Item Juice

# change value for first item
grocery_list[0] = "Green Juice"
print('First Item', grocery_list[0])
# output: First Item Green Juice

# print subset of a list from index 1 to index 3
# but not include index 3
print(grocery_list[1:3])
# output: ['Tomatoes', 'Potatoes']

# Can store in a string by putting an equal sign with a String
# name or String variable on the side
gList = (grocery_list[1:3])
print(gList)
# output: ['Tomatoes', 'Potatoes']

# Also put other things, ex. lists of lists inside of a list
other_events = ['Wash Car', 'Pick Up Kids', 'Cash Check']

# create another list where we store two lists together
to_do_list = [other_events, grocery_list]
print(to_do_list)
# output: [['Wash Car', 'Pick Up Kids', 'Cash Check'], ['Green Juice', 'Tomatoes', 'Potatoes', 'Bananas']]

# if we wanted to get the second item out of the list,
# lists are basically boxes inside of boxes
# 2nd item out of the 2nd list, 1 representing the second grouping
# Tomatoes which is the 2nd item in the 2nd list choose 1
print((to_do_list[1][1]))   # output: Tomatoes

# append items
print(grocery_list)
# output: ['Green Juice', 'Tomatoes', 'Potatoes', 'Bananas']

grocery_list.append('Onions')   # Onions will show up last
print(grocery_list)
# output: ['Green Juice', 'Tomatoes', 'Potatoes', 'Bananas', 'Onions']

# inserting a new item in a very specific index
# 2nd index which is #1, with pickle inside
grocery_list.insert(1, "Pickle")
print(grocery_list)
# output: ['Green Juice', 'Pickle', 'Tomatoes', 'Potatoes', 'Bananas', 'Onions']

# Remove items, Ex. "Pickle"
grocery_list.remove("Pickle")
print(grocery_list)
# output: ['Green Juice', 'Tomatoes', 'Potatoes', 'Bananas', 'Onions']

# Sort items
grocery_list.sort()
print(grocery_list)
# output: ['Bananas', 'Green Juice', 'Onions', 'Potatoes', 'Tomatoes']

# Reverse Sort
grocery_list.reverse()
print(grocery_list)
# output: ['Tomatoes', 'Potatoes', 'Onions', 'Green Juice', 'Bananas']

# Delete an item, Ex. index 4 item
del grocery_list[4]
print(grocery_list)
# output: ['Tomatoes', 'Potatoes', 'Onions', 'Green Juice']

# combine lists together
to_do_list2 = other_events + grocery_list
print(to_do_list2)
# output: ['Wash Car', 'Pick Up Kids', 'Cash Check', 'Tomatoes', 'Potatoes', 'Onions', 'Green Juice']

# get the length of the items from to_do_list2
print(len(to_do_list2))
# output: 7

# get the maximum or since working with Strings, highest alphabetically
print(max(to_do_list2))
# output: Wash Car

# minimum item or what ever comes first alphabetically
print(min(to_do_list2))
# output: Cash Check

