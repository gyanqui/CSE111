"""
File: L06 Teach: Team Activity
Author: Gab Yanqui
Date: 02/07/2023
Purpose: Use the debugger in VS Code to step through the program and
verify that it works correctly.
"""
"""write a Python program named esteem.py that implements the Rosenberg
self-esteem scale. Your program must ask the user to respond to each of
the ten statements with D, d, a, or A which mean strongly disagree, disagree,
agree, and strongly agree. Your program must compute the score for each
answer and sum and display the person’s total score. You should think
about how you will separate this program into functions before you begin
writing the program.
"""

def main():

    print("""This program is an implementation of the Rosenberg
Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
Please rate how much you agree with each of the
statements by responding with one of these four letters:

D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement. """)
    
    print()#blank line
    positive_first = input("""01. I feel that I am a person of worth, at least on an equal plane with others.
    Enter D, d, a, or A: """)
    positive_second = input("""02. I feel that I have a number of good qualities.
    Enter D, d, a, or A: """)
    negative_third = input("""03. All in all, I am inclined to feel that I am a failure.
    Enter D, d, a, or A: """)
    positive_fourth = input("""04. I am able to do things as well as most other people.
    Enter D, d, a, or A: """)
    negative_fifth = input("""05. I feel I do not have much to be proud of.
    Enter D, d, a, or A: """)
    positive_sixth = input("""06. I take a positive attitude toward myself.
    Enter D, d, a, or A: """)
    positive_seventh = input("""07. On the whole, I am satisfied with myself.
    Enter D, d, a, or A: """)
    negative_eigth = input("""08. I wish I could have more respect for myself.
    Enter D, d, a, or A: """)
    negative_nineth = input("""09. I certainly feel useless at times.
    Enter D, d, a, or A: """)
    negative_tenth = input("""10. At times I think I am no good at all.
    Enter D, d, a, or A: """)


    first= positive_questions(positive_first)
    second= positive_questions(positive_second)
    third= negative_questions(negative_third)
    fourth= positive_questions(positive_fourth)
    fifth= negative_questions(negative_fifth)
    sixth= positive_questions(positive_sixth)
    seventh= positive_questions(positive_seventh)
    eigth= negative_questions(negative_eigth)
    nineth= negative_questions(negative_nineth)
    tenth= negative_questions(negative_tenth)


    score = first + second + third + fourth + fifth + sixth + seventh + eigth + nineth + tenth

    print(f'Your score is {score}')
    print('A score below 15 may indicate problematic low self-esteem.')

def positive_questions(answer):


    if answer == "D":
        score = 0
    elif answer == "d":
        score = 1
    elif answer == "a":
        score = 2
    elif answer == "A":
        score = 3
    return score

def negative_questions(answer):

    if answer == "D":
        score = 3
    elif answer == "d":
        score = 2
    elif answer == "a":
        score = 1
    elif answer == "A":
        score = 0
    return score


if __name__ == "__main__":
    main()