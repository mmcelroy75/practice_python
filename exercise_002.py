'''
Exercise 2

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

1) If the number is a multiple of 4, print out a different message.
2) Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''


def int_validation(prompt):
    while True:
        try:
            num = int(input(prompt))
            if not isinstance(num, int):
                raise ValueError
            break
        except ValueError:
            print("Your input must be a whole number. Try again.")
    return num


def exercise_002():
    x = int_validation("Enter a number: ")
    y = int_validation("Enter a second number: ")

    if x % 4 == 0:
        print("The first number is a multiple of 4.")

    if x % 2 == 0:
        print("The first number is even.")
    else:
        print("The first number is odd.")

    if x % y == 0:
        print(f"{y} divides evenly into {x}, no remainders.")
    else:
        print(f"{y} does not divide evenly into {x}.")


exercise_002()
