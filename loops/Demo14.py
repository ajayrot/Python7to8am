
no = int(input("Enter a No :"))

r = no%10
no= no//10

while no != 0:
    r1 = no%10
    no = no//10

print("The sum = ",r+r1)


