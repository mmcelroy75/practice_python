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
