#(2)  Here Returning a function

def hello(name):

    print("hello has been executed")

    def greet():

        print("Hare Krishna")

    def welcome():

        print("Jay Shree Ram")

    
    if name == "Rutvik":

        return greet
    
    else:

        return welcome
    

new_func1=hello("Rutvik")

new_func2=hello("Rutvik Prajapati")

new_func1()

new_func2()