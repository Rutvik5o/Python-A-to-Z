#Python Function As Argument

#(1) Function was accecpting other function as argument

#(2) returning a function

#(1): 

#Example:
'''def greet():

    print("hi")


def display(other_def_fun):

    print("this is display() function")

    other_def_fun()



display(greet) '''   #display is higher order function


def greet_louder (name):

    print(f"Hi {name.upper()}")

def greet_softer(name):

    print(f"Hi {name.lower()}")

def hello(other_def_func,name1):

    print("This is display() function")

    other_def_func(name1)


hello(greet_louder,"rutvik")
hello(greet_softer,"RUTVIK")






