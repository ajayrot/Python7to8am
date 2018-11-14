class Employee:
    def __init__(self,idno=0,name=None):
        self.idno = idno
        self.name = name

    def display(self):
        print("IDNO = ",self.idno)
        print("NAME = ",self.name)

emp = [] # Empty List
for x in range(5):
    id = int(input("Enter IDNO : "))
    na = input("Enter Name : ")
    e = Employee(id,na)
    emp.append(e)


for x in range(5):
    emp[x].display()