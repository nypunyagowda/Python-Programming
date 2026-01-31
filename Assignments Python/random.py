import random

# take range from user
low = int(input("Enter the minimum value: "))
high = int(input("Enter the maximum value: "))

# if user accidentally gives them in reverse order, fix it
if low > high:
    low, high = high, low

# generate random number in the given range (inclusive)
number = random.randint(low, high)

print("Random number:", number)
