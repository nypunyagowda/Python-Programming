

class NegativeNumberError(Exception):
    pass

num = int(input("Enter number: "))

if num < 0:
    raise NegativeNumberError("Negative number not allowed")
else:
    print("Valid number")
