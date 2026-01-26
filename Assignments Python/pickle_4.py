import pickle

a = [1, 2, 3]
b = {"x": 10}
c = "Hello"

with open("multi.pkl", "wb") as f:
    pickle.dump(a, f)
    pickle.dump(b, f)
    pickle.dump(c, f)

with open("multi.pkl", "rb") as f:
    print(pickle.load(f))
    print(pickle.load(f))
    print(pickle.load(f))
