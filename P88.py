# Exercise 26

class Circle:  # Class names should start with an uppercase letter

    pi = 3.14  # Class object Attribute

    def __init__(self, radius=6):  # The constructor name should be __init__, not __int__
        self.radius = radius
        self.area = Circle.pi * radius * radius  # Use the class name instead of "circle"

    def get_circumference(self):  # Method name should be "get_circumference" instead of "get_circumstances"
        return 2 * Circle.pi * self.radius  # Use the class name instead of "circle"


circle_1 = Circle(4)  # -> Override

print(f"The Circumference of Circle 1 is -> {circle_1.get_circumference()}.")

circle_2 = Circle(14)

print(f"The Circumference of Circle 2 is -> {circle_2.get_circumference()}.")

print(f"The Area of Circle 1 is -> {circle_1.area}")


print("Assigntment Work")

class Rectangle:

    def __init__(self,l,b):

        self.l=l

        self.b=b

    def area_of_rectangle(self):

        return self.l * self.b

    def circum_of_rectangle(self):

        return (2 * self.l) + (2 * self.b)


rect1=Rectangle(10,20)

print(f"Area of Reactangle is -> {rect1.area_of_rectangle()}")

print(f"Circumstances of Rectangle is {rect1.circum_of_rectangle()}.")