def add_num(*numbers):
    total=0
    for n in numbers:
        total+=n
    return total
print(add_num(1,3,4))
print(add_num(1,5,6,2,3,4))