'''
Exercise 2

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''

import datetime


def int_validation(prompt, x):
    while True:
        try:
            num = int(input(prompt))
            if num < x or not isinstance(num, int):
                raise ValueError
            break
        except ValueError:
            print("Your input must be a whole number. Try again.")
    return num


def exercise_001():
    name = input("What is your name? ").title()
    age = int_validation("What is your age? ", 1)
    y = int_validation("Enter another number: ", 1)

    year = datetime.timedelta(days=365)
    years_to_100 = (100 - age)
    age_at_100 = datetime.datetime.today() + (year * years_to_100)
    time = age_at_100.strftime("%Y")

    for i in range(y):
        print(f"{name} will turn 100 in {time}.\n")


exercise_001()
