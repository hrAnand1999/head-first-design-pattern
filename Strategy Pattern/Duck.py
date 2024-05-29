from abc import ABC, abstractmethod

class Duck :
    def __init__(self) -> None:
        pass

    @abstractmethod
    def display(self):
        pass

    def quack(self):
        print("All ducks are quacking")

    def swim(self):
        print("All duck are swimming")


