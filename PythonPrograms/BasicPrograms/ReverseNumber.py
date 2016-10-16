def ReverseNumber(number):
    result=0
    sum=0
    while(number>0):
        result=number%10
        number=number//10
        sum=result+(sum*10)
    return sum
print(ReverseNumber(1238))

