import pickle
my_dict = {"name": "Abhinav", "age": 30}

with open("dict.pkl", "wb") as f:
    pickle.dump(my_dict, f)

with open("dict.pkl", "rb") as f:
    loaded_dict = pickle.load(f)

print(loaded_dict)
