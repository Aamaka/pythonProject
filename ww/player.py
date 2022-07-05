class Player:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


player1 = Player("messi", 33)
print(player1.name, player1.age)
