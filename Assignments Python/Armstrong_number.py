# Armstrong number check

num = int(input("Enter a number: "))

# Convert number to string to count digits
digits = str(num)
power = len(digits)

sum_of_powers = 0

# Loop through each digit
for d in digits:
    sum_of_powers += int(d) ** power

# Compare result with original number
if sum_of_powers == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")
