# Hybrid Inheritence

class A:

    def display(self):

        print("Display From A Class")

class B(A):

    def display(self):

        print("Display From B Class")

class C:

    def show():

        print("Hi From C Class")

class D(B,C):

    def display(self):

        #super().display() can call from that

        print("Display from D Class")


d1=D()
d1.display()
print(D.mro())



