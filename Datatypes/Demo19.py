
d1 = {"idno":101,"name":"Ravi","salary":125000}
print(d1)

d1.clear()
print(d1)


d1 = {"idno":101,"name":"Ravi","salary":125000}
val = d1.get("Salary")
print(val)

v1 = d1.items()
print(v1)
print(type(v1))

v2 = d1.keys()
print(v2) # dict_keys(['idno', 'name', 'salary'])
print(type(v2))

v3 = d1.values()
print(v3) # dict_values([101, 'Ravi', 125000])
print(type(v3))



print(d1)
val = d1.pop("name")
print("Removed value : ",val)
print(d1)


d1.popitem()
print(d1)


d1.setdefault("name")
print(d1)
