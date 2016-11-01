def addArrays(arr1,arr2):
    leng=max(len(arr1),len(arr2))
    result=[0 for j in range(0,leng)]
    i=len(arr1)-1
    j=len(arr2)-1
    c=0
    leng=leng-1
    newResult=[]
    while(i>=0 and j>=0):
        r=arr1[i]+arr2[j]+c
        i=i-1
        j=j-1
        result[leng]=r%10
        c=r//10
        leng=leng-1

    while(i>=0):
        r=arr1[i]+c
        i=i-1
        result[leng]=r%10
        c=r//10
        leng=leng-1

    while(j>=0):
        r=arr2[j]+c
        j=j-1
        result[leng]=r%10
        c=r//10
        leng=leng-1

    if(c!=0):
            newResult=[0 for x in range(len(result)+1)]
            t=len(newResult)-1

            while(t>=0):
                if t-1>=0:
                    newResult[t]=result[t-1]
                else:
                    newResult[t]=c
                t=t-1
                
    return newResult


#arr1 = [1, 1, 1]
#arr2 = [9, 2, 2]

arr1 = [9, 9, 9, 9, 9, 9, 9]
arr2 = [1, 6, 8, 2, 6, 7]
r=addArrays(arr1, arr2)
print(r)
