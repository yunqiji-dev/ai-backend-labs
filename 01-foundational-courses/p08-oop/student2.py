# Example 1
"""
class Student:
    name:str =""
    house:str =""

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()
    """


# Example 2
class Student:
    def __init__(self):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name:")
    house = input("House:")
    student = Student(name, house)

    return student

if __name__ == "__main__":
    main()