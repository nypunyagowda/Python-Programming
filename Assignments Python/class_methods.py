class Student:
    school_name = "ABC High School"   # class variable

    def __init__(self, name):
        self.name = name              # instance variable

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name    # modifies class variable

# creating objects
s1 = Student("Alice")
s2 = Student("Bob")

print(s1.school_name)
print(s2.school_name)

# calling class method
Student.change_school("XYZ Public School")

print(s1.school_name)
print(s2.school_name)
