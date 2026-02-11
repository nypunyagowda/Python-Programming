# Generate n natural numbers using while loop

n = int(input("Enter the value of n: "))

i = 1
print("First", n, "natural numbers are:")

while i <= n:
    print(i, end=" ")
    i += 1
