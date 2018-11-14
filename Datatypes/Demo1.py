
l1 = [10,20,30,40,50]
print(l1)
l1.append(60)
print(l1)
print("-------------------------")

marks = [] # empty list
for x in range(6):
    print("Enter Subject ",x+1," Marks : ")
    marks.append(int(input()))

print("Total marks = ",sum(marks))
print("Average = ",sum(marks)/len(marks))
