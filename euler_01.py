import  math

number = 1
sum = 0
while number < 1000:
    if (number % 3 == 0 or number % 5 == 0):
        sum=sum+number
    number=number+1

print(sum)
