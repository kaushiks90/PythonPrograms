def fibonacci(num):
    a=0
    b=1
    print(a)
    print(b)
    c=0
    for x in range(2,num+1):
        c=a+b
        a=b
        b=c
        print(c)
   
fibonacci(10)


    