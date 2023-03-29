"""
File: L02 Teach: Team Activity
Author: Gab Yanqui
Date: 01/10/2023
Purpose: Practice calling functions applying a discount. 
"""
"""
You work for a retail store that wants to increase sales on Tuesday
and Wednesday, which are the store's slowest sales days. On Tuesday
and Wednesday, if a customer's subtotal is greater than $50, the
store will discount the customer's purchase by 10%.
"""

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Define a function named main.
def main():
    # Call the now() method to get the current date and
    # time as a datetime object from the computer's OS.
    current_date_and_time = datetime.now()

    # Call the weekday() method to get the day of the
    # week from the current_date_and_time object.
    day_of_week = current_date_and_time.weekday()

    # Call the subtotal() function to get subtotal
    subtotal = float(input('Please enter the subtotal: '))

    # Call conditionals to add discount just if applycable
    if (day_of_week == 1 or day_of_week == 2) and subtotal >= 50:
        discount = round(subtotal * 0.10, 2)
        print(f'Discount amount: {discount:.2f}')
        subtotal -= discount
        
    # Callculate regular total
    tax = round(subtotal * 0.06, 2)
    print(f'Sales tax amount: {tax:.2f}')
    total = tax + subtotal
    print(f'Total: {total:.2f}')

main()