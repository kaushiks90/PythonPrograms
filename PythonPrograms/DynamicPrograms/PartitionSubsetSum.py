#Given an array is it possible to split it up into 2 equal sum partitions. Partition need not be equal sized. Just equal sum.

def PartitionSubsetSum(inputArray,length):

    sum=0
   
    for x in range(len(inputArray)):
        sum=sum+inputArray[x]
    if(sum%2!=0):
        return False
    sum=sum//2
    T=[[0 for col in range(sum+1)]for row in range(length)]
    for x in range(0,len(inputArray)):
        T[x][0] = True

    for i in range(length):
        for j in range(0,(sum+1)):
            if(j-inputArray[i-1]>=0):
                T[i][j]=T[i-1][j] or T[i-1] [j-inputArray[i-1]]
            else:
                T[i][j]=T[i-1][j]  
    return T[length-1][sum]
     
inputArray=[1, 3, 5, 5, 2, 1, 1, 6]
print(PartitionSubsetSum(inputArray,len(inputArray)))
