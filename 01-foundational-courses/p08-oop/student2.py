# pyright:reportImplicitOverride=false
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
"""
class Student:
    def __init__(self, name:str, house:str):
        self.name: str = name
        self.house:str = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name: str = input("Name:")
    house: str = input("House:")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()
"""


# Example 3
"""
class Student:
    def __init__(self, name:str, house:str):
        if not name:
            raise ValueError("Missing name")
        self.name: str = name
        self.house:str = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name: str = input("Name:")
    house: str = input("House:")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()
"""


# Example 4
"""
class Student:
    def __init__(self, name:str, house:str):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name: str = name
        self.house:str = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name: str = input("Name:")
    house: str = input("House:")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()
"""


# Example 5
"""
class Student:
    name: str
    house: str

    def __init__(self, name:str, house:str):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)


def get_student():
    name: str = input("Name:")
    house: str = input("House:")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()
"""


# Example 6
"""
class Student:
    name: str
    house: str
    patronus: str

    def __init__(self, name: str, house: str, patronus: str):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)


def get_student():
    name: str = input("Name: ")
    house: str = input("House: ")
    patronus: str = input("Patronus: ")
    student = Student(name, house, patronus)
    return student

if __name__ == "__main__":
    main()
"""


"""
# Example 7
class Student:
    name: str
    house: str
    patronus: str

    def __init__(self, name: str, house: str, patronus: str):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "1"
            case "Otter":
                return "2"
            case "Jack Russell terrier":
                return "3"
            case _:
                return "0"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name: str = input("Name: ")
    house: str = input("House: ")
    patronus: str = input("Patronus: ")
    student = Student(name, house, patronus)
    return student

if __name__ == "__main__":
    main()
"""


# Example 8
class Student:
    name: str
    house: str

    def __init__(self, name: str, house: str):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name: str = input("Name: ")
    house: str = input("House: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()


