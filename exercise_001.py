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
