class Cars:

    total = 0 #class variable

    def __init__(self,model,brand,year,price,description):
        self.model = model
        self.brand = brand
        self.year = year
        self.price = price
        self.description = description
        Cars.total += 1


    def showCarDetails(self):
        print("------Cars Details-----------")
        print("Model:",self.model)
        print("Brand:",self.brand)
        print("Year:",self.year)
        print("Description:",self.description)
        print("----------------------------")


    @classmethod #class method
    def ShowTotalCount(cls):
        print("Total Cars:",cls.total)

    @staticmethod #static method

    def ApprovalLoan(salary):
        if (salary > 50000):
            print("You can take loan")
        else:
            print("You can not take loan")

tata = Cars("Tata Suv","tata",2022,18,"Tata suv")
tata.showCarDetails()

Cars.ShowTotalCount()
Cars.ApprovalLoan(7070000)




