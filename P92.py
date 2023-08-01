#-> Hierarchical Inheritence

#->Parent -> Child 1
#         -> Child 2
#         -> Child 3


class Human:

    def __init__(self,name,age):

        print("Calling init from human class.")

        self.name=name

        self.age=age

    def showDetails(self):

        print(f"-> Name: {self.name},\n-> Age: {self.age}")

    def eat(self):

        print("I can Eat.")


class Male(Human):

    def __init__(self,m_name,location):

        print("Calling init from Male Class.")

        Human.__init__(self,m_name,age)

        self.location=location

    def sleep(self):

        print("I can sleep whole day.")

class Female(Human):

    def __init__(self,name,age,can_dance):

        print("Calling init from female class.")

        super().__init__(name,age)

        self.know_dancing=can_dance

    def showDetails_F(self):

        Human.showDetails(self)

        print(f"Know_Dacing : {self.know_dancing}")


    def work(self):

        print("I can Code.")


female_1=Female("Jiya",20,True)

female_1.showDetails_F()

print(female_1.age)

#male_1=Male("Hello",18,"Delhi")

#print(Male.mro())