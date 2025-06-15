class person:
    def __init__(self,name,email,phone,age):
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age
        self.status = True


    def showPerson(self):
        print("-----------------------")
        print("Name:",self.name)
        print("Email:",self.email)
        print("Phone:",self.phone)
        print("Age:",self.age)
        print("Status:",self.status)


demo = person("Harsh","harsh@gmail.com",9483593539,40)
demo.showPerson()

demo2 = person("Rahul","Rahul@gmail.com",4353262,43)
demo2.showPerson()
