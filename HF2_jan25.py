class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Builder(Human):
    def __init__(self, name, age, construction_experience):
        super().__init__(name, age)
        self.construction_experience = construction_experience

    def __str__(self):
        return f"{super().__str__()}, Occupation: Builder, Construction Experience: {self.construction_experience}"


class Sailor(Human):
    def __init__(self, name, age, sailing_experience):
        super().__init__(name, age)
        self.sailing_experience = sailing_experience

    def __str__(self):
        return f"{super().__str__()}, Occupation: Sailor, Sailing Experience: {self.sailing_experience}"


class Pilot(Human):
    def __init__(self, name, age, flying_hours):
        super().__init__(name, age)
        self.flying_hours = flying_hours

    def __str__(self):
        return f"{super().__str__()}, Occupation: Pilot, Flying Hours: {self.flying_hours}"


# Example usage
human = Human("John Doe", 30)
builder = Builder("Bob Builder", 40, "10 years")
sailor = Sailor("Sally Sailor", 35, "5 years")
pilot = Pilot("Peter Pilot", 45, "1000 hours")

print(human)
print(builder)
print(sailor)
print(pilot)
