from FlyBehaviour import FlyBehaviour

class FlyWithWings(FlyBehaviour):
    def __init__(self) -> None:
        super().__init__()

    def fly(self):
        print('I am flying with wings.')

