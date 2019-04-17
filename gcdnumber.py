#from math import gcd
#print(gcd(20, 8))


a = int(input('Please input the First Number:'))
b = int(input('Please input the Second Number:'))
while b != 0:
    gcd = b
    b = a % b
    a = gcd
print(gcd)

'''
for i in range(1,b+1):
    if a % i == 0 and b % i == 0:
        gcd = i
print(gcd)'''
