d = {"Alice":84, "Bob":74,"Carol":92}
for marks in d.items():
    print(marks)
for marks in d.keys():
    print(marks)
for marks in d.values():
    print(marks)
for students , marks in d.items():
    print(f"{students} - {marks}") 