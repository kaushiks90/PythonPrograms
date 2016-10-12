def GCD(m,n):
    fm=[]
    for x in range(1,m+1):
        if m%x==0:
            fm.append(x)
    fn=[]
    for x in range(1,n+1):
        if n%x==0:
            fn.append(x)
    fr=[]
    for x in fm:
        if x in fn:
            fr.append(x)
    return fr[-1]

print(GCD(14,28))

    


          