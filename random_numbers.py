"""
File: L07 Teach: Team Activity
Author: Gab Yanqui
Date: 02/14/2023
Purpose: Practice calling functions applying a discount. 
"""
"""Write a Python program named random_numbers.py that creates a list
of numbers, appends more numbers onto the list, and prints the list.
The program must have two functions named main and append_random_numbers
as follows:

main
Has no parameters
Creates a list named numbers like this:
numbers = [16.2, 75.1, 52.3]
Prints the numbers list
Calls the append_random_numbers function with only one argument to add
one number to numbers
Prints the numbers list
Calls the append_random_numbers function again with two arguments to add
three numbers to numbers
Prints the numbers list
append_random_numbers
Has two parameters: a list named numbers_list and an integer named quantity.
The parameter quantity has a default value of 1
Computes quantity pseudo random numbers by calling the random.uniform function.
Rounds the quantity pseudo random numbers to one digit after the decimal.
Appends the quantity pseudo random numbers onto the end of the numbers_list.
"""

import random

def main():
    # Create a list of words
    words = []
    # Create a number list
    numbers = [16.2, 75.1, 52.3]
    # Print list
    print(numbers)
    # Call the append_random_numbers to add a number to our list
    append_random_numbers(numbers)
    # Print list with new value added
    print(numbers)
    # Call the append_random_numbers to add numbers to our list
    append_random_numbers(numbers, 3)
    # Print list with new numbers added
    print(numbers)
    
    # Call the append_random_word function to add words to the list
    append_random_words(words, 5)
    # Print the list wth the new words added
    print(words)

def append_random_numbers(number_list, quantity=1):
    """Append quantity random numbers onto the numbers list.
    The random numbers are between 0 and 100, inclusive.
    Parameters
        numbers_list: A list of numbers where this function will
            append random numbers.
        quantity: The number of random numbers that this function
            will append onto numbers_list.
    Return: nothing.
    """
    # Create the for loop to add a new value onto the number_list as many times as requested
    for i in range(quantity):
        # Generate a random float between 0 and 100 and round the random float to 1 decimal place
        random_rounded_number = round(random.uniform(0, 100), 1)
        # Append the rounded number to the number_list
        number_list.append(random_rounded_number)

def append_random_words(word_list, quantity=1):
    """Append quantity random words onto the words list.
    Parameters
        words_list: A list of words where this function will
            append random words.
        quantity: The number of random numbers that this function
            will append onto words_list.
    Return: nothing.
    """
    # Create a list of words
    words_list = ['green', 'yellow', 'blue', 'red', 'purple', 'black', 'white']

    # Create the for loop to add a new value onto the word_list as many times as requested
    for i in range(quantity):
        # Generate a random choice from the words list to add to the words list in main
        word= random.choice(words_list)
        # Append the random choice word to the words_list
        word_list.append(word)

# Call main to start this program.
if __name__ == "__main__":
    main()