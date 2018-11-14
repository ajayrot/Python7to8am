class Employee:
    def __init__(self):
        print("Constructor")

    def display(self):
        print("Method")

    def __del__(self):
        print("des")

e1 = Employee()
e1.display()
del e1  # deleting

