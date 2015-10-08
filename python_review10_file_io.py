# Python Programming Review
# file name: python_review10_file_io.py
# JetBrains PyCharm 4.5.4 under Python 3.5.0

import random  # random number generator
import sys     # sys module
import os      # operating system

# file io or input output
# create or open a file
# opening a file called "test.txt", wb allows you to write to the file
test_file = open("test.txt", "wb")

# output on screen file mode being used in this situation, wb
print(test_file.mode)  # outputs: wb

# if you forgot your file name, this will remind you
print(test_file.name)  # outputs: test.txt

# write text to a screen or to a file
test_file.write(bytes("Write me to the file\n", 'UTF-8'))

# close a file
test_file.close()


# read information from a file
# open file, reading and writing (r+)
test_file = open("test.txt","r+")

# read the data out of the file
text_in_file = test_file.read()

# print out the info
print(text_in_file)  # outputs: Write me to the file

# delete the file, use the os module, put in file name ("")
# and its removed
os.remove("test.txt")