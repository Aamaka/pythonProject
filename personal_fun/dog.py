class Dog:
    species = "Cans familiars"

    # constructor
    def __init__(self, name, age, colour="pink"):
        self.name = name
        self.age = age
        self.colour = colour

    #     instance method
    def describe(self):
        return f"my name is {self.name}, i am {self.age} years old"

    # another instance method
    def speak(self, sound):
        return f"{self.name} barks: {sound}"
    #
    # def __str__(self):
    #     return f"my name is {self.name}, i am {self.age} years old"
    #
    # names = ["nos", "love", "joy"]
    # print(names)
    #
    # for name in names:
    #     print(name)


buddy = Dog("bobo", 3, "black")
bae = Dog("lala", 5, "brown")
# print(f"{buddy.name} coat is {buddy.colour}")

print(f"{bae.name} is {bae.age} years old and has a {bae.colour} skin")
# print(bae.speak("woof"))
# print(bae)
# print(buddy.speak("yap"))
print(bae.__str__())
print(buddy.describe())
