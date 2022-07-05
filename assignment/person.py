class Person:
    ID = 0

    def __init__(self, first_name, last_name, year, month, day):
        self.first_name = first_name
        self.last_name = last_name
        self._year = year
        self._month = month
        self._day = day
        Person.ID += 1
    #
    # def repr(self):
    #     return f"<Person: {self.first_name}"

    def __str__(self):
        return f"<Person: {{name={self.first_name}, {self.last_name}, age={self.age}}}"

    @property
    def age(self):
        return self.age

    @staticmethod
    def age(year):
        return 2022 - year

    # @property
    # def age(self):
    #     return self.age

    # @age.deleter
    # def age(self):
    #     print("Age deleted")
    #     del self.age

    @classmethod
    def get_nun_of_id(cls):
        return cls.ID

    @staticmethod
    def get_age(self, year):
        return 2022 - self.year


p1 = Person("bola", "seun", 2002, "march", 7)
print(p1)