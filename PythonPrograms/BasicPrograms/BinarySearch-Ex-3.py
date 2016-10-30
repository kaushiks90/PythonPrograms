#Write Binary Search code to find the first and last occurance in the array

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


list = [1,3,10,45,45,45,45]
FirstOccur= BinarySearchFirstOccurance(list,45)   
LastOccur= BinarySearchLastOccurance(list,45)
print("First pos",FirstOccur)
print("Last pos",LastOccur)





