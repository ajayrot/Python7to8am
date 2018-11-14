class Address:
    def __init__(self,hno=0,street=None,city=None):
        self.hno = hno
        self.street = street
        self.city = city

    def displayAddress(self):
        print("House No : ",self.hno)
        print("Street : ",self.street)
        print("City : ",self.city)


class Employee:
    def __init__(self,idno=0,name=None):
        self.idno = idno
        self.name = name
    def display(self):
        print("IDNO = ",self.idno)
        print("NAME = ",self.name)
        b = 100
        a = Address(123,"Shanthi Nagar","Hyderabad")
        a.displayAddress()
       

e1 = Employee(101,"Ravi")
e1.display()
