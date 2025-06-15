class Bank:
    def __init__(self, bankName, location, minamount=0):
        self.bankName = bankName
        self.location = location
        self.amount = minamount
        self.employees = []
        self.customers = []
        self.branches = []
        self.services = []

    def ShowBankDetails(self):
        if self.bankName != "":
            print("Bank Name :", self.bankName)

        if self.location != "":
            print("Bank Location : ",self.location)

        if self.amount != 0:
            print("Bank Min Balance :",self.amount)

        if self.employees != []:
            print("-----------Employees-----------")
            for employee in self.employees:
                print(employee)

        if self.customers != []:
            print("-----------Customers-----------")
            for customer in self.customers:
                print(customer)

        if self.branches != []:
            print("-----------Branches-----------")
            for branch in self.branches:
                print(branch)

        if self.services != []:
            print("-----------Services-----------")
            for service in self.services:
                print(service)

    def addServices(self, service):
        self.services.append(service)
        print("Service added")


    def addBranches(self, branch):
        self.branches.append(branch)
        print("Branch added")


    def addEmployees(self, employee):
        self.employees.append(employee)
        print("Employee added")


    def addCustomers(self, customer):
        self.customers.append(customer)
        print("Customer added")



class Sbi(Bank):
    def __init__(self, bankName, location, minAmount):
        super().__init__(bankName, location, minAmount)
        self.rateOfInterest = 0

    def setRoi(self, roi):
        self.rateOfInterest = roi

    def getRoi(self):
        print("Rate Of Interest is :" , self.rateOfInterest)


    def addPerson(self, personName, role):
        if role == "employee":
            self.addEmployees(personName)
        elif role == "customer":
            self.addCustomers(personName)
        else:
            print("Provide valid role")

    def ShowBankDetails(self):
        print("==============-: State Bank Of India :-==============")
        super().ShowBankDetails()
        print("Rate Of Interest : ", self.rateOfInterest)
        print("=====================================================")

manager = Sbi("State Bank Of India", "Usmanpura", 2000)
manager.addServices("Account Opening")
manager.addServices("Home Loan")
manager.addServices("Education Loan")
manager.addBranches("Usmanpura")
manager.addBranches("Navrangpura")
manager.addBranches("Airport")
manager.addPerson("Rahul", "employee")
manager.setRoi(7)
manager.ShowBankDetails()


