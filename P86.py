# self & __initt__():

class Instructer:

    def __init__(self):
        print("Creating a new object")


instructer_1=Instructer #-> Created New object

instructer_1.name="XYZ"
instructer_1.address="Delhi"

print(instructer_1.name)
print(instructer_1.address)


instructer_2=Instructer #-> Creating One more object

instructer_2.name="ABC"
instructer_2.address="Mumbai"

print(instructer_2.name)
print(instructer_2.address)


print("-> Using Parameter")

class Instructer:
    def __init__(self,instructer_name,address,followers=0): #Giving Default arguments

        self.name=instructer_name
        self.address=address
        self.followers=followers           #-> Default

instructer_1=Instructer("James","Kolkata",500)

instructer_2=Instructer("Adam","Haveli")

print(f"Hi I am {instructer_1.name} & i am living on {instructer_1.address} & My Followers is {instructer_1.followers}")

print(instructer_2.followers)


