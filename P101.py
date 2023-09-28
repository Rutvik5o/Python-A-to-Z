print("Encapsulation")


class student:

    def __init__ (self,name,rollname,age):

        self.name=name #public instance variable

        self._rollname=rollname #protected instance variable

        self.__age=age


    def get_age(self):

        return self.__age


    def set_age(self,age):

        if age>35:

            print("Invalid")

        else:

            self.__age=age


s1=student("Rutvik",23,20)

print(s1.get_age())

s1.set_age(18)

print(s1.get_age())


