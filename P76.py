#PrintVsReturn

def fun(a,b):  #Print
    c=a+b
    print(c)

output=fun(10,15)                    #||
print(output) #<-its print none      #fun(10,15)

def fun1(a,b): #Return
    c=a+b
    return c #return statement stop exectuion of current function

output=fun1(10,15)
print(output)



def func(x):
    return x+1


def func2(a,b):
    c=a+b
    return c

output2=func2(3,4)
final_output=func(output2)

print(final_output)
