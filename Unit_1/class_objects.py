# Step 1: Create a user-defined exception
class InvalidAgeError(Exception):
    pass


# Step 2: Function that uses the exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    else:
        print("Eligible to vote")


# Step 3: Handle the exception
try:
    check_age(16)
except InvalidAgeError as e:
    print("Error:", e)
