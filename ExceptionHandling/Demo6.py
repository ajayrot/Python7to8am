from requests.exceptions import ConnectionError
from firebase.firebase import FirebaseApplication

name = input("Enter Name : ")
cn = int(input("Enter Contact No : "))
try:
    fb = FirebaseApplication("https://djangoproduct.firebaseio.com/",None)
    fb.put("Employee",cn,{"Name":name})
    print("Data saved")
except ConnectionError as ce:
    print("Please Check Network")
finally:
    print("Firebase Process is Done")
