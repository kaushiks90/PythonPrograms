def PrimeNumber(num):
    isprime = False
    for x in range(2,num):
        if num % x == 0:
            isprime = True
        if isprime == True:
            break
    if isprime == False:
        print(num)
    

def firstHundredPrimeNum():
    for x in range(2,100):
        PrimeNumber(x)

firstHundredPrimeNum()

