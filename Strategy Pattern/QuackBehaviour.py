from abc import ABC, abstractmethod

class QuackBehaviour:
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def quack(self):
        pass