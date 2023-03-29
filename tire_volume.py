"""
File: L02 Prove: Assignment
Author: Gab Yanqui
Date: 01/10/2023
Purpose: Calculate the volume of space inside a tire in the USA and add store user
inputs to a txt file. 
"""
"""
Write a program named tire_volume.py that computes the approximate volume of air 
inside a tire. Add code near the end of that program that does the following:

Gets the current date from the computer’s operating system.
Opens a text file named volumes.txt for appending.
Appends to the end of the volumes.txt file one line of text that contains the 
following five values:
    current date
    width of the tire
    aspect ratio of the tire
    diameter of the wheel
    volume of the tire
"""

import math
from datetime import datetime

w = int(input('Enter the width of the tire in mm (ex 205): '))
a= int(input('Enter the aspect ratio of the tire (ex 60): '))
d= int(input('Enter the diameter of the wheel in inches (ex 15): '))

#adjust all in ml and convert it to lt
v = f'{(math.pi * w ** 2 * a * (w * a + 2540 * d))/10000000000:.2f}'
print(f'The approximate volume is {v} liters')

print()#blank line
c_decision = input('Do you want to buy a tire with the dimensions you entered (yes/no)? ')

# Get current date
current_date = datetime.now()
# Convert date to a string in the desired format
current_date_str = current_date.strftime("%Y-%m-%d")

with open("volumes.txt", "at") as volumes_file:
    if c_decision.lower() == 'yes': 
        pnumber = int(input('Enter your phone number: '))
        # Append a line of text to the file with pnumber
        volumes_file.write(f'{current_date_str}, {w}, {a}, {d}, {v}, {pnumber}\n')
        
    else:
        # Append a line of text to the file
        volumes_file.write(f'{current_date_str}, {w}, {a}, {d}, {v}\n')
print('Thanks for using my program. Good bye!')