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
    def __init__(self,idno=0,name=None,hno=0,street=None,
                                        city=None):
        self.idno = idno
        self.name = name
        # Has a
        # Employee has-a Address
        self.a = Address(hno,street,city)

    def display(self):
        print("IDNO = ", self.idno)
        print("NAME = ", self.name)
        self.a.displayAddress()

e = Employee(name="Ravi",street="Shanthi Nagar",idno=101,hno=184,city="HYD")
e.display()


