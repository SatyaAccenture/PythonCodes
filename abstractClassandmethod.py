from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        self


class Laptop(Computer):
    def process(self):
        print("Process")
l1=Laptop()
l1.process()
