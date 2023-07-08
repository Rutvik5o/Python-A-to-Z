# Local & Global scope

a=10          #-> global
def display():
    a=15       #-> local
    print(a)

display()



b=10
def display():
    b=15
    def show():
        print(b)
    show()

display()


a,b=5,6
if a<b:
    c=a+b
print(c)