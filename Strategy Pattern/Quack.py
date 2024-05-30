from QuackBehaviour import QuackBehaviour

class Quack(QuackBehaviour):
    def __init__(self) -> None:
        super().__init__()

    def quack(self):
        print("Quack")