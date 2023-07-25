# Concept Of Inheritence

class Human:

    def __init__(self,num_heart):

        self.num_eyes=2

        self.num_nose=1

        self.num_heart=num_heart


    def eat(self):

        print("I can eat")

    def work(self):

        print("I can work")



class Male(Human):

    def __init__(self,name,heart):

        super().__init__(heart)

        self.name=name

    def flirt(self):

        print("I can flirt")

    def work(self):

        super().work()

        print("I can code")

    def display(self):

        print(f"Hi,i am {self.name} and I have {self.num_heart} heart.")


male_1=Male("ABC",1)

#male_1.flirt()

#male_1.work()

print(male_1.num_eyes)

print(male_1.name)

male_1.display()



