
while True:
    name = input("Enter Name : ")
    print("Welcome Mr/Miss : ",name)
    print("Name Length = ",len(name))
    ans = input("To Continue Press Y/y : ")
    if ans == "Y" or ans == "y":
        continue
    else:
        break
print("Thanks")