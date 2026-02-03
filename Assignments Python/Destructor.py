class Animal:
    def __init__(self):
        print("class animal is created")
    def __del__(self):
        print("animal is destroyed")
obj = Animal()
del obj