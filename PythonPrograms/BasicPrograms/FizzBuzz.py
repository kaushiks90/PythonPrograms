#Given an positive number find the total FizzBuzz in the number
#If the number is divisible by 3 then fizz.If divisible by 5 then Buzz .If the number is divisible by both 3 and 5 then FizzBuzz

def FizzBuzz(x):
    for i in range(1,x+1):
        if(i%3==0 and i%5==0):
            print("Fizz Buzz")
        elif(i%3==0):
            print("Fizz");
        elif(i%5==0):
            print("Buzz");
        else:
            print(i)
FizzBuzz(16)
