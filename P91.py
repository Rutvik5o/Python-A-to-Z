#Multilevel Inheritence
#Parent -> Child 1 -> Child 2

class Human:

    can_breath=True

    def __init__(self,num_heart):

        print("Calling init from Human Classes.")

        self.eyes=2

        self.heart=num_heart

    def eat(self):

        print("I can Eat.")

    def work(self):

        print("I can Work.")


class Male(Human):

    def __init__(self,name):

        print("Calling init from Male Class.")

        self.name=name


    def sleep(self):

        print("I can sleep whole day.")

class Boy(Male):

    def __init__(self,heart,name,can_dance):

        Human.__init__(self,heart)

        Male.__init__(self,name)

        self.know_dancing=can_dance

    def work(self):

        #Human.work(self) #-> 1st method

        super().work #-> 2nd method

        print("I can Code.")



boy_1=Boy(1,"Rahul",True)

print(boy_1.name)

print(boy_1.know_dancing)

print(boy_1.can_breath)

print(Boy.mro())




