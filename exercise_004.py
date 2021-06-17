import math
from validate import int_validation


def exercise_004():
    divisors = []

    x = int_validation("Enter a number and we'll tell you all the divisors of that number: ")

    for i in range(1, int(math.sqrt(x))):
        if x % i == 0:
            divisors.append(i)
            divisors.append(x // i)

    return sorted(divisors)


if __name__ == '__main__':
    print(exercise_004())
