# Palindrome number checker

num = int(input("Enter a number: "))
original = num
reverse_num = 0

while num > 0:
    digit = num % 10              # get last digit
    reverse_num = reverse_num * 10 + digit
    num //= 10                    # remove last digit

if original == reverse_num:
    print(original, "is a palindrome")
else:
    print(original, "is not a palindrome")
