
class SathyaException(Exception):
    def __init__(self,message="Sorry"):
        super().__init__(message)
        self.message = message

# def checkAge(age=0):
#     if age >= 23:
#         return "Valid Age"
#     elif age < 0:
#         raise SathyaException("Invalid Age")
#     else:
#         raise SathyaException()
#
#
# try:
#     age = int(input("Enter Age : "))
#     result = checkAge(age)
#     print(result)
# except SathyaException as se:
#     print(se)
# except ValueError:
#     print("Invalid Input")
# print("Thanks")
