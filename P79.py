#Modify a global varible

a=10

def displayy():
    global a                 #-> Global keyword
    a=a+1
    print(a)

displayy()




def display():
    a=20
    def show():
        global a  #-> in local you can also make global variable use global keyword
        a=30


    print(f"value of before calling show() function is {a}")
    show()
    print(f"value of after calling showw() function is {a}")

display()
print(a)   #-> its print 30 bcoz its consider value of global keyword as global


print("Let's see one more example")

name="Good"
def display():
    global name
    name= name+ "Morning"

print(name)
display()
print(name)