import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Aryaman", 25)

with open("person.pkl", "wb") as f:
    pickle.dump(person, f)

with open("person.pkl", "rb") as f:
    loaded_person = pickle.load(f)

print(loaded_person.name, loaded_person.age)
