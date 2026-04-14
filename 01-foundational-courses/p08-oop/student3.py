# pyright:reportImplicitOverride=false
class Student:

    def __init__(self, name: str, house: str) -> None:
        self.name: str = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self) -> str:
        return self._house

    @house.setter
    def house(self, house: str) -> None:
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house: str = house

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


