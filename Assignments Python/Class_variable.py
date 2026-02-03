class add:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.answer=0
    def calculate(self):
        self.answer = self.a + self.b
    def display(self):
        print("Number 1 is: ",self.a)
        print("Number 2 is: ",self.b)
        print("Solution is: ",self.answer)
a = add(10,30)
a.calculate()
a.display()