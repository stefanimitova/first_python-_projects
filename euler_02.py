import math


a = 1
b = 2
sum = 0
while a < 4000000 and b < 4000000:
    if a%2==0:
        sum += a
    if b%2==0:
        sum = sum + b
    a = a + b
    b = b + a
    print (sum,a,b)
    



