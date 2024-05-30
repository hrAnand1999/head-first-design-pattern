from abc import ABC, abstractmethod

class FlyBehaviour:
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def fly(self):
        pass