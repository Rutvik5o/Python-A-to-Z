# Debugging

#(1)


def display():
    for i in range(1,11):
        if i == 10:
            print("Bye!..")

display()

#(2)

import random

dice_numbers=["One","Two","Three","Four","Five","Six"]

dice_num=random.randint(0,5)

print(dice_numbers[dice_num])

#(3)

year=int(input("In Which year yu were born?"))

if year>1980 and year <=1996:
    print("You are a X")
elif year > 1996:
    print("You are a Y")


#(4)

age=int(input("How old are you?"))

if age>= 18:
    print(f"You can bote at {age}")


#(5)

a,b=0,0

a=int(input("Enter a -> "))

b=int(input("Enter b -> "))

multiplication = a*b

print(multiplication)



#(6)

n=int(input("Enter a Number"))

if n % 2== 0:
    print("Even")
else:
    print("Odd")

#(7)

for number in range(1,16):

    if number % 3 == 0 and number % 5 == 0:

        print("FizzBuzz")

    elif number % 3 == 0:

        print("Fizz")

    elif number % 5 == 0:

        print("Buzz")

    else:

        print(number)

