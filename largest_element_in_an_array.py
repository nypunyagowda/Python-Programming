arr = (input("Enter the elements: "))

arr = arr.split(",")
arr = [int(x) for x in arr]
largest = arr[0]    #assuming first element to be largest
n = len(arr)
for i in range (n):
    if largest<arr[i]:
        largest = arr[i]
print(largest)

        