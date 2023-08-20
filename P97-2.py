import P97 as m

print(m.a)
print(m.area_of_square(16))



## for import any specific item from module

from P97 import calculator as x  #-> Rename using as

x(10,20)


#from P97 import *  #-> For import everything




import P97
a,b=4,5
sum=a+b



print("Sum is:",sum)  #Acessed local variable value
print("value of a from another module is:",P97.a)  #Acessing module value of module