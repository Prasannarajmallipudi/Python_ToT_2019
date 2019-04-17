print("Enter 3 Numbers:")
a = int(input("Enter Number"))
b = int(input("Enter Number"))
c = int(input("Enter Number"))
 
if a>b and a>c:
    print(a, " is Large")
elif b>a and b>c:
    print(b, " is Large")
else:
    print(c, " is Large")
