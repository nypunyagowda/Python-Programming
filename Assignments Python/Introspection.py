import inspect

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I am {self.name}"

# Create object
s = Student("Alice", 20)

# --- INTROSPECTION STARTS ---

print("Type of object:", type(s))

print("\nAttributes & methods of object:")
print(dir(s))

print("\nDoes object have 'age' attribute?")
print(hasattr(s, "age"))

print("\nValue of 'name' attribute:")
print(getattr(s, "name"))

print("\nIs greet callable?")
print(callable(s.greet))

print("\nSource code of greet method:")
print(inspect.getsource(Student.greet))

print("\nSignature of greet method:")
print(inspect.signature(Student.greet))
