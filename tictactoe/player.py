from dataclasses import dataclass


@dataclass(frozen=True)
class Player:
    # def __init__(self, name:str, sign:str) -> None:
    #     self.name = name
    #     self.sign = sign
    name: str
    sign: str


if __name__ == '__main__':
    Player1 = Player("Seguin", "*")
