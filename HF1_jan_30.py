class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def __repr__(self):
        return self.__str__()

def main():
    students = [
        Student("John", "Doe"),
        Student("Jane", "Doe"),
        Student("Alice", "Smith")]
    
    print("Eredeti sorrend:")
    print(students)

    # A lista rendezése név szerint
    sorted_students = sorted(students, key=lambda student: student.firstname)

    # A rendezett lista kiíratása
    print("\nRendezett lista:")
    print(sorted_students)

if __name__ == "__main__":
    main()
    
    '''A tapasztalatok a következők lennének:

Az eredeti lista kiíratásánál a __str__ metódus hívódik meg minden Student objektumra.
A rendezett lista kiíratásánál viszont a __repr__ metódus hívódik meg minden Student objektumra,
mert a sorted vagy sort függvények a __repr__-t használják az objektumok ábrázolásához.'''
