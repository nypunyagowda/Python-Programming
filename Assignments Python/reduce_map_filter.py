from functools import reduce

Marks = [45,25,85,76,96,36,55]
updated = list(map(lambda x:x+5,Marks))

passed = list(filter(lambda x :x>50,updated))

total = reduce(lambda x,y : x+y, passed)

print("Updated marks: ", updated)
print("Passed students: ", passed)
print("Total of marks: ", total)