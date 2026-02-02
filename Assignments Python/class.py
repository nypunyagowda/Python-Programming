class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def walk(self):
        print(f"{self.name} is walking")
a = Human("Alice",21)
b = Human("Bob",18) 
a.walk()
b.walk()    