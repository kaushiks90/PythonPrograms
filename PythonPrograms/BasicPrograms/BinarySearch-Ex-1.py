#Write Binary Search code to find the first occurance in the array

def BinarySearch(inputArray,searchElement):
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

list = [1,3,45,45,56,89,96]
result = BinarySearch(list,45)   
print("Element pos",result)





