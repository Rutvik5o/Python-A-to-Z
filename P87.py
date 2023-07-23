#Class Methods on python

class Instructer:

    followers=0 #-> class object variable

    def __init__(self,name,address):

        self.name=name
        self.address=address

    def display(self,subject_name):
        print(f"Hi, I am {self.name} and I teach {subject_name}")

    def update_followers(self,followers_name):

        self.followers +=1





instructer_1=Instructer("ABC","XYZ")

print(instructer_1.name)

instructer_1.display("Python")

instructer_1.update_followers("Miss.keynel")

print(instructer_1.followers)

instructer_2=Instructer("Kianel","Mexico")

instructer_2.update_followers("Kevai")

print(instructer_2.followers)



