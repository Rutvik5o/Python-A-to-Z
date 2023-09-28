print("Abstract Class & Abstract Method") #-> By Default Not Supported


from abc import ABC,abstractmethod

class vehicle(ABC):

    def __init__(self,n):

        self.no_of_types=n

    @abstractmethod


    def start(self):

        pass

    def display(self):

        print("Hi I am calling from Vehicle Class")





