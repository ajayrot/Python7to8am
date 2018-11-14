
students = [{"idno":101,"marks":[45,90,91,80,16,35]},
{"idno":102,"marks":[46,99,95,8,36,13]},
{"idno":103,"marks":[47,97,98,18,61,45]},
{"idno":104,"marks":[48,95,95,89,14,85]},
{"idno":105,"marks":[49,95,95,15,44,25]}]

# Example to Print Total of a student

for x in students:
    print("IDNO = ",x["idno"],end="  ")
    print("TOTAL = ",sum(x["marks"]))
