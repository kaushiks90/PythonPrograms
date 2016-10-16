def ReverseString(originalString,n):
    for x in range(n,0,-1):
        print(originalString[x-1])

strRev="Kaushik"
ReverseString(strRev,len(strRev))