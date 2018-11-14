s1 = {"idno":101,
      "name":"Ravi",
      "class":10,
      "marks":[45,90,95,80,16,35]}

for x,y in s1.items():
    print(x," --- ",y)

print("Total = ",sum(s1["marks"]))
print("Average = ",sum(s1["marks"])/len(s1["marks"]))
print("High subject = ",max(s1["marks"]))

# for a in s1["marks"]:
#     if a >= 35:
#         print("Pass")
#     else:
#         print("Fail")



for x in range(len(s1["marks"])):
    if s1["marks"][x] >= 35:
        print("Subject : ",(x+1)," : Pass")
    else:
        print("Subject : ",(x+1)," : Fail")
