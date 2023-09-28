print("Operator Overloading")


class ComplxNumber:

    def __init__(self,r,i):

        self.real=r

        self.imaginary=i


    def __add__(self,other):

        return f"{self.real + other.real} + {self.imaginary + other.imaginary} i"



       #another way #return str(self.real + other.real) + "+" + str(self.imaginary + other.imaginary)+"i"



c1=ComplxNumber(1,2)
c2=ComplxNumber(10,12)

print(c1+c2)


