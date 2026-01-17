#Example 1
x = int(input("Enter the number: "))
if x%2==0:
    print("x is even")
else:
    print("x is odd")

#Example 2
signal = input("Enter signal colour: ")
if signal == "red":
    print("STOP")
elif signal == "yellow":
    print("READY")
else:
    print("GO")


#Example 3 Using multiple elif statements
time = int(input("Enter time: "))
if time == 8:
    print("It is breakfast time")
elif time == 13:
    print("It is lunch time")
elif time == 17:
    print("It is snacks time")
elif time == 21:
    print("It is dinner time")
else:
    print("It is not a meal time")


#Example 4 Using Logical operator
day = input("Enter the day: ")
is_raining = False
if day == "Saturday" or day == "Sunday":
    if not is_raining:
        print("Let us visit Mysuru")
    else:
        print("It is raining let us stay home")
else:
    print("It is a weekday let us wait for weekend")

#Example 5 Using Nested if
gender = input("Enter the gender: ").lower().strip()
age = int(input("Enter the age: "))
if gender == "female":
    print("Ticket is free")
else:
    if age <= 5:
        print("You get a child discount")
    elif age >= 60:
        print("You get a senior discount")
    else:
        print("You pay the full price")


        




