class Duck:

    def swim(self):

        print("I am duck and I am swim")

    def speaks(self):

        print("Quack Quack")


class Dog:

    def swim(self):

        print("I am god and I am swim")

    def speaks(self):

        print("Woof Woof")


def display(duck):

    duck.swim()

    duck.speaks()

    print("Information Displayed")

class Demo:  #using class

    def display(self,obj):

        obj.swim()

        obj.speaks()

        print("Information Displayed")


d=Duck()

dog=Dog()

display(dog)

display(d)


demo=Demo()  #class on function
demo.display(d)
demo.display(dog)