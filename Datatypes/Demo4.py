
l1 = [10,20,30,40,50,40,50,40]
print("Before :",l1)

for x in l1:
    if x == 40:
        l1.remove(40)

print("After :",l1)

print("-----------------------")

l1 = [10,20,30,40,50,40,50,40]
print("Before :",l1)

#Converting list to set and set to list
l1 = list(set(l1))
l1.remove(40)

print("After :",l1)
