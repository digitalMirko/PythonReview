# Python Programming Review
# file name: python_review04_dictionaries.py
# JetBrains PyCharm 4.5.4 under Python 3.5.0

import random  # random number generator
import sys     # sys module
import os      # operating system

# Dictionaries are made up of values with a unique key for each value
# you will be storing, similar to lists but you can't join dictionaries
# together like you can with lists with + sign
# Dictionary of Super Villians, names with their real identity
# Dictionary name = {  'Key'  :  'Value' }
super_villians = {'Fiddler' : 'Issac ', 'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Mark Mardon', 'Mirror Master' : 'Sam Scudder',
                  'Pied Piper' : 'Thomas Peterson'}
print(super_villians)
# output: {'Fiddler': 'Issac ', 'Weather Wizard': 'Mark Mardon', 'Pied Piper': 'Thomas Peterson', 'Captain Cold': 'Leonard Snart', 'Mirror Master': 'Sam Scudder'}

# Get secret identity for one of the villians
print(super_villians['Captain Cold']) # output: Leonard Snart

# delete an entry, type in Key to delete
del super_villians['Fiddler']
print(super_villians)
# output: {'Pied Piper': 'Thomas Peterson', 'Mirror Master': 'Sam Scudder', 'Captain Cold': 'Leonard Snart', 'Weather Wizard': 'Mark Mardon'}

# replace a villian
super_villians['Pied Piper'] = 'Hartley Rathaway'
print(super_villians)
# output: {'Mirror Master': 'Sam Scudder', 'Pied Piper': 'Hartley Rathaway', 'Weather Wizard': 'Mark Mardon', 'Captain Cold': 'Leonard Snart'}

# length, how many super villians we have stored
print(len(super_villians)) # output: 4

# Get the value by passing in a key
print(super_villians.get("Pied Piper")) # output: Hartley Rathaway

# Get list of our super villian keys
print((super_villians.keys()))
#output: dict_keys(['Captain Cold', 'Mirror Master', 'Weather Wizard', 'Pied Piper'])

# Get a list of dictionary values
print(super_villians.values())
# output: dict_values(['Sam Scudder', 'Leonard Snart', 'Mark Mardon', 'Hartley Rathaway'])

