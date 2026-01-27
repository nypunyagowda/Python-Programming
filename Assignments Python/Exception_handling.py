try: 
    value = int(input("enter the number>> "))
    result = 10 / value
except ValueError:
    print("it is a value error")
except DivisionByZero:
    print("division by zero")
else:
    print(f"Result: {result}")
finally:
    print(" cleanup complete ")
