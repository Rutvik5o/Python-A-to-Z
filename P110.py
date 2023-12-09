#When you are importing a file then that this name is assigned to value of that prticular module.

#when we directly run file then only main execute

def display(name):
    return name

def do_something():
    print("This function is doing something")


if __name__ =="__main__":

    print("This is 110.py file")

    name=input("Enter Your Name")

    print(display(name))

    do_something()