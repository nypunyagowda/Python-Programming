class Database:
    def __init__(self):
    
        self.__storage = {}
    def write(self,key,value):
        self.__storage[key] = value
    def read(self,key):
        if key in self.__storage:
            print(self.__storage[key])
        else:
            print("DB item not available")
db = Database()
db.write("name","Alice")
db.read("name")
 