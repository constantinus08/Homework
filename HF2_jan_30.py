class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        # Először a lastname alapján rendezzük
        if self.lastname != other.lastname:
            return self.lastname < other.lastname
        # Ha a lastname egyezik, akkor a firstname alapján rendezzük
        return self.firstname < other.firstname

def main():
    students = [
        Student("John", "Smith"),
        Student("Jane", "Jones"),
        Student("Mary", "Evans"),
        Student("Robert", "Smith")
    ]

    # A sorted() függvény automatikusan használja a __lt__ metódust a rendezéshez
    sorted_students = sorted(students)

    print("Rendezett lista:")
    for student in sorted_students:
        print(student)

if __name__ == "__main__":
    main()
