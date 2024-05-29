from Duck import Duck

class MallardDuck(Duck):
    def __init__(self) -> None:
        super().__init__()

    def display(self):
        print("looks like a Mallard")