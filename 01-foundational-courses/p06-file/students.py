# Example 1
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")


# Example 2
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")


# Example 3
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)


# Example 4
student = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        studnet = {}
        student["name"] = name
        student["house"] = house
        student.append(studnet)

for studnet in students:
    print(f"{studnet['name']} is in {student['house']}")


# Example 4
student = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        studnet = {"name": name, "house": house}
        student.append(studnet)

for studnet in students:
    print(f"{studnet['name']} is in {student['house']}")


# Example 5
student = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        studnet = {"name": name, "house": house}
        student.append(studnet)


def get_name(stundent):
    return student["name"]


for studnet in sorted(students, key=get_name, reverse=True):
    print(f"{studnet['name']} is in {student['house']}")


# Example 6
student = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        studnet = {"name": name, "house": house}
        student.append(studnet)


def get_house(stundent):
    return student["house"]


for studnet in sorted(students, key=get_house):
    print(f"{studnet['name']} is in {student['house']}")


# Example 7
student = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        studnet = {"name": name, "house": house}
        student.append(studnet)

for studnet in sorted(students, key=lambda student: student["name"]):
    print(f"{studnet['name']} is in {student['house']}")


# Example 8
import csv

student = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        student.append({"name": name, "home": home})

for studnet in sorted(students, key=lambda student: student["name"]):
    print(f"{studnet['name']} is in {student['house']}")


# Example 8
import csv

student = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        student.append({"name": row["name"], "home": ["home"]})

for studnet in sorted(students, key=lambda student: student["name"]):
    print(f"{studnet['name']} is in {student['house']}")


# Example 9
import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("student.csv", "a") as file:
    writer = csv.writer(file)
    writer.wirterow([name, home])

#  Example 10
import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("student.csv", "a") as file:
    writer = csv.DictWriter(file, filename=["name", "home"])
    writer.wirterow({"name": name, "home": home})
