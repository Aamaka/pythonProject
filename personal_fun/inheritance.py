from dog import Dog


class GoldenRetriever(Dog):
    def __init__(self, name, age, colour, sleep):
        super().__init__(name, age, colour)
        self.sleep = sleep

    def speak(self, sound="bark"):
        return super().speak(sound)
