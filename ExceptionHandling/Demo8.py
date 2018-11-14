def checkAge(age=0):
    if age >= 23:
        return "Valid Age"
    else:
        raise ValueError("Invalid Age")

try:
    age = int(input("Enter Age : "))
    result = checkAge(age)
    print(result)
except ValueError as ve:
    print(ve)

print("Thanks")