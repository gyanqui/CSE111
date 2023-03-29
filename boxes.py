"""
File: L02 Prepare: Checkpoint
Author: Gab Yanqui
Date:01/09/2023
Purpose: Funcions: Built-in Functions: Function inside modelus, methods  .
"""
"""
A manufacturing company needs a program that will help its employees
pack manufactured items into boxes for shipping. Write a Python
program named boxes.py that asks the user for two integers:  1) the
number of manufactured items and 2) the number of items that the user
will pack per box. Your program must compute and print the number of
boxes necessary to hold the items. This must be a whole number. Note
that the last box may be packed with fewer items than the other boxes.
"""

from math import ceil

num_items = int(input('Enter the number of items: '))
items_per_box = int(input('Enter the number of items per box: '))

num_boxes = ceil(num_items / items_per_box)

# Compute the number of boxes by dividing
# and then calling the math.ceil function.
print()#This is a blank line
print(f'For {num_items} items, packing {items_per_box} items in each box, you will need {num_boxes} boxes. ')