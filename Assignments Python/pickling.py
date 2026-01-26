import pickle

data = {
    "name": "Alice",
    "age": 22,
    "skills": ["Python", "Java", "SQL"]
}

with open("data.pkl", "wb") as f:   # wb = write binary
    pickle.dump(data, f)

print("Object pickled successfully!")
