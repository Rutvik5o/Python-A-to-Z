class student:

    def __init__(self,name,rollno,age):


        self.name=name #Public instace vareiable

        self._rollno=rollno #Protected Instance Variable

        self.__age=age  #Private Instance Variable


    def __display(self):

        print(f"Hi Myself {self.name} {self.__age} years old with roll no {self._rollno}")

    def displayPrivateData(self):

        self.__display()


class Branch(student):

    def show(self):

        print(f"My Name is {self.rollno} ")



s1=student("Rutvik",1234,18)

print(s1._student__age)

s1._student__display()