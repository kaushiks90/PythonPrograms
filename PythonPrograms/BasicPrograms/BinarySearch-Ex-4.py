#Find the count of a given number in sorted array
#Step 1
def LinearSearch(inputArray,searchElement):
    count=0
    for x in range(0,len(inputArray)):
        if(searchElement==inputArray[x]):
            count=count+1
    return count
list=[11,12,13,13,13,15,18]
#list=[13,13,13,13,13,13,13]
print(LinearSearch(list,13))

#step2

def BinarySearchFirstOccurance(inputArray,searchElement):
    first=0
    last=len(inputArray)-1
    result=-1
    while(first<=last):
        mid=(first+last)//2
        if(searchElement==inputArray[mid]):
            result=mid 
            last=mid-1
        elif(searchElement<inputArray[mid]):
            last=mid-1
        elif(searchElement>inputArray[mid]):
            first=mid+1
    return result

def BinarySearchLastOccurance(inputArray,searchElement):
    first=0
    last=len(inputArray)-1
    result=-1
    while(first<=last):
        mid=(first+last)//2
        if(searchElement==inputArray[mid]):
            result=mid 
            first=mid+1
        elif(searchElement<inputArray[mid]):
            last=mid-1
        elif(searchElement>inputArray[mid]):
            first=mid+1
    return result



FirstOccur= BinarySearchFirstOccurance(list,13)   
LastOccur= BinarySearchLastOccurance(list,13)
print("Count",(LastOccur-FirstOccur)+1)



