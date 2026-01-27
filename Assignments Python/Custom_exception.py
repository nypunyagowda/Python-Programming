class InvalidAgeException(Exception):
    "raise when age is less than number"
number = 18
try:
    age = int(input("enetr the age: "))
    if age < number:
        raise InvalidAgeException
    else:
        print("you are eligible to vote")
except InvalidAgeException:
    print("you are not eligible to vote")
finally:
    print("this is finally block")
