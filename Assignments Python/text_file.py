# Write data to a file (creates file if it doesn't exist)
with open("sample.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")
    file.write("Python file handling is easy.\n")

print("Data written successfully.")

