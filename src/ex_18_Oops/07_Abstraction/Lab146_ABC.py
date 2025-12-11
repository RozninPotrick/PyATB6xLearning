from abc import ABC, abstractmethod

class Father(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def laon(self):
        pass

class Amit(Father):

    def laon(self):
        print("Giving the 50 k Loan")

amit = Amit("Amit Sharma")
amit.laon()