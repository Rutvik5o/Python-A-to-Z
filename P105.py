print("Method Overloading & Overiding")

print("Using Default Argument")

print("Using Args")


class Demo:

    def add(self,*args):

        total=0

        for i in args:

            total+=i

        return total

d=Demo()

print(d.add(2,3))

print(d.add(1,2,3))

print(d.add(3,4,551,35))