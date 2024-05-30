from QuackBehaviour import QuackBehaviour

class MuteQuack(QuackBehaviour):
    def __init__(self) -> None:
        super().__init__()

    def quack(self):
        print("<< Silence >>")