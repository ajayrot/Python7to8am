
students = {
    "10th":[
        {"idno":101,"marks":[45,90,91,80,16,35]},
        {"idno":102,"marks":[46,99,95,8,36,13]},
        {"idno":103,"marks":[47,97,98,18,61,45]},
        {"idno":104,"marks":[48,95,95,89,14,85]},
        {"idno":105,"marks":[49,95,95,15,44,25]}
            ],
    "9th":[
        {"idno":101,"marks":[45,90,91,80,16,35]},
        {"idno":102,"marks":[46,99,95,8,36,13]},
        {"idno":103,"marks":[47,97,98,18,61,45]}
            ],
          }

print("10th class Students are : ",len(students["10th"]))
print("9th class Students are : ",len(students["9th"]))

for x in students["9th"]:
    if x["idno"] == 103:
        print("Valid")
        break
else:
    print("invalid")