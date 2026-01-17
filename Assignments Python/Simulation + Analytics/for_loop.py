name = "PythonProgramming"
for index,letters in enumerate(name):
    print(letters*(index+1))'''

#example 2

cities = ["blr","ckm","mlr","mys"]
for city in cities:
    if city == "mlr":
        print(f"found {city}!")
        break
    print(city)

#example 3
l = [12,27,87,89]
for num in l:
    print(num)
else:
    print("all printed")



