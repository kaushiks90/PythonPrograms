def Factorial(n):
    result=1
    for x in range(1,n+1):
        result=result*x
    return result
print(Factorial(3))
