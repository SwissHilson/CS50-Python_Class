students = [
    {"name" : "Hermione", "house" : "Gryffinder", "patronus" : "Otter"},
    {"name" : "Harry", "house" : "Gryffinder", "patronus" : "Stag"},
    {"name" : "Ron", "house" : "Gryffinder", "patronus" : "Jack Russell Terrier"},
    {"name" : "Draco", "house" : "Slytherin", "patronus" : None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=', ')