
l1 = [10,20,30,40,50]

for x in l1:
    print(x)

print("============================")

my_friends = ["Ravi","kumar","mohan","murali","prasad","krishna"]
ur_friends = ["Rama","kumar","Kapil","Srikanth","prasad","krishna","Ravi"]

comm_friends = [] # empty list

for x in my_friends:
    if x in ur_friends:
        comm_friends.append(x)

print("Common Friends are :",comm_friends)
print("Total ",len(comm_friends)," are common Friends")


print("============================")


def common_end(l1,l2):
    if l1[0] == l2[0]:
        return True
    elif l1[-1] == l2[-1]:
        return True
    else:
        return False

print(common_end([1,2,3],[7,3]))
print(common_end([1,2,3],[7,3,2]))
print(common_end([1,2,3],[1,3]))

print("===============================")

def sum3(l1):
    return sum(l1)

print(sum3([1,2,3]))
print(sum3([5,11,2]))
print(sum3([7,0,0]))

print("===============================")

def sum5(l1):
    sum = 0
    for x in l1:
        sum = sum+x

    return sum


print(sum5([1,2,3]))
print(sum5([5,11,2]))
print(sum5([7,0,0]))

print("===============================")