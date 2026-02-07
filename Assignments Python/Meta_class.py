# Define a metaclass
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")

        # Add a new attribute automatically
        dct["college"] = "ABC University"

        return super().__new__(cls, name, bases, dct)


# Use the metaclass
class Student(metaclass=MyMeta):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")


# Create object
s = Student("Alice")

# Access normal and metaclass-added attributes
s.display()
print("College:", s.college)
