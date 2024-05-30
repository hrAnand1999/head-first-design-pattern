from FlyBehaviour import FlyBehaviour

class FlyNoWay(FlyBehaviour):
    def __init__(self) -> None:
        super().__init__()

    def fly(self):
        print('I can not fly')

