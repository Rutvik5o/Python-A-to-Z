print("Method Overiding")

class father:

    def sleep(self):

        print("10:00 PM to 5:00 PM")

    def eat(self):

        print("Eating")



class son(father):

    def sleep(self):

        print("2:00 PM to 10:00 PM")

        super().sleep()

Royal=son()

Royal.sleep()