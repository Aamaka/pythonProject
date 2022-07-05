from dog import Dog


class BullDog(Dog):
    pass


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


class Dachshund(Dog):
    pass


mill = BullDog("mole", 5, "blue")
milo = JackRussellTerrier("milo", 12, "purple")
pay = Dachshund("pay", 33, "pink")

print(mill.species)
print(milo.speak())

print(type(mill))
print(isinstance(milo, Dog))
