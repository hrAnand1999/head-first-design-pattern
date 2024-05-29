from Duck import Duck

class RedHeadDuck(Duck):
    def __init__(self) -> None:
        super().__init__()

    def display(self):
        print("looks like a RedHead")


red = RedHeadDuck()
red.display()
red.quack()
red.swim()