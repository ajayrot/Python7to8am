
d1 = {
    "idno":101,
    "name":"Ravi",
    "salary":125000.00,
    "designation":"Manager"
}

# will display only keys
for x in d1:
    print(x)

print("====================================")

# will display only values
for x in d1:
    print(d1[x])

print("====================================")

# will display only keys and values
for x in d1:
    print(x," -- ",d1[x])

print("====================================")

# will display only keys and values in tuple format
for x in d1.items():
    print(x)

print("====================================")

# will display only keys and values
for x,y in d1.items():
    print(x,"---",y)

print("====================================")

# will display only keys
for x in d1.keys():
    print(x)

print("====================================")

# will display only values
for x in d1.values():
    print(x)