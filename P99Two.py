from P99 import vehicle


class Bike(vehicle):


    def __init__(self,n,color):

        super().__init__(n)

        self.color=color

    def start(self):

        print("Start With Kick")

    def display(self):

        print(f"My color is {self.color}")


class scooty(vehicle):

    def __init__(self,n):

        super().__init__(n)

    def start(self):

        print("Self Start")



class car(vehicle):

    def __init__(self,n,x):

        super().__init__(n)

        self.no_of_gears=6


    def start(self):

        print("Start With Key")

