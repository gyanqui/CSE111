"""
File: L03 Teach: Team Activity
Author: Gab Yanqui
Date: 01/19/2023
Purpose: Write your own functions with parameters and then
call those functions with arguments. 
"""
"""
Write a Python program named fitness.py that does the following:
1. Asks the user to enter four values:
    a. gender
    b. birthdate in this format: YYYY-MM-DD
    c. weight in U.S. pounds
    d. height in U.S. inches
2. Converts the weight from pounds to kilograms (1 lb = 0.45359237 kg)
3. Converts inches to centimeters (1 in = 2.54 cm).
4. Calculates age, BMI, and BMR.
5. Prints age, weight in kg, height in cm, BMI, and BMR.
"""

# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime

def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input('Please enter your gender (M or F): ')
    birth= input('Enter your birthdate (YYYY-MM-DD): ')
    pounds = float(input('Enter your weight in U.S. pounds: '))
    inches = float(input('Enter your height in U.S. inches: '))    

    # Call the compute_age function to compute the user's age in years
    years = compute_age(birth)

    # Call kg_from_lb function to convert from pounds to kg
    kg = kg_from_lb(pounds)

    # Call the cm_from_inches function to convert from in to cm
    cm = cm_from_in(inches)

    # Call the m_from_cm fuction to convert from cm to m
    m = m_from_cm(cm)

    # Call the body_mass_index function
    bmi = body_mass_index(kg, cm)

    # Call the basal?metabolic_rate function
    bmr = basal_metabolic_rate(gender, kg, cm, years)

    # Print the results for the user to see.
    print(f'Age (years): {years}')
    print(f'Weight (kg): {kg:.2f}')
    print(f'Height (m): {m:.2f}')
    print(f'Body mass index: {bmi:.1f}')
    print(f'Basal metabolic rate (kcal/day): {bmr:.0f}')
    pass

def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1
    return years

def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    height = pounds * 0.45359237
    return height

def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    height = inches * 2.54
    return height

def m_from_cm(cm):
    """Converta length in cm to meters.
    Parameter cm: a leanth in cm.
    Return: the length in m.
    """
    m = cm / 100
    return m

def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000 * weight) / (height ** 2)
    return bmi

def basal_metabolic_rate(g, w, h, a):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if g.upper() == "F":
        bmr = 447.593 + 9.247 * w + 3.098 * h - 4.330 * a
    else:
        bmr = 88.362 + 13.397 * w + 4.799 * h - 5.677 * a
    return bmr

# Call the main function so that
# this program will start executing.
main()