fname = input("Enter File Name : ")
try:
    file = open(fname)
    text = file.read()
    print(text)
    file.close()
except FileNotFoundError as f:
    print(f)
else:
    print("Data Reading From File")
print("Thanks")