#  Example 1
"""
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")


def get_name():
    return input("What's your name: ")


def get_house():
    return input("What's your house: ")


if __name__ == "__main__":
    main()
"""


#  Example 2
"""
def main():
    name, house = get_student()
    print(f"{name} from {house}")


def get_student():
    name = input("What's your name: ")
    house = input("What's your house: ")
    return name, house


if __name__ == "__main__":
    main()
"""


#  Example 3
"""
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("What's your name: ")
    house = input("What's your house: ")
    return (name, house)


if __name__ == "__main__":
    main()
"""


#  Example 4
"""
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] == "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("What's your name: ")
    house = input("What's your house: ")
    return [name, house]


if __name__ == "__main__":
    main()
"""


#  Example 5
"""
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    student = {}
    student['name'] = input("What's your name: ")
    student['house'] = input("What's your house: ")
    return student


if __name__ == "__main__":
    main()
"""


#  Example 6
"""
def main():
    student = get_student()
    if student["name"] = "Padma"
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("What's your name: ")
    house= input("What's your house: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()
"""