from FlyBehaviour import FlyBehaviour

class FlyRocketPowered(FlyBehaviour):
    def __init__(self) -> None:
        super().__init__()

    def fly(self):
        print('I am flying with a rocket!')

