from Duck import Duck
from QuackBehaviour import QuackBehaviour

class RubberDuck(Duck, QuackBehaviour):
    def __init__(self) -> None:
        super().__init__()

    def display(self):
        print("looks like a Rubber duck")

    def quack(self):
        print('Rubber duck is quackking')


rubber_duck = RubberDuck()
rubber_duck.display()
rubber_duck.quack()
rubber_duck.swim()
