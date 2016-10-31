#Search Element in Circular sorted Array
def BinarySearch(inputArray,searchElement):
    first = 0
    last = len(inputArray) - 1
    while(first <= last):
        mid = (first + last) // 2
        if(searchElement == inputArray[mid]):
            return mid 
        if(inputArray[mid] <= inputArray[last]):
            if(searchElement >= inputArray[mid] and searchElement <= inputArray[last]):
               first = mid + 1  
            else :              
                last = mid - 1  
        else:
            if(searchElement >= inputArray[mid] and searchElement <= inputArray[first]):
                last = mid - 1 
            else:
                first = mid + 1 

list = [99,96,95,23,1,3,5,7]
result = BinarySearch(list,0)   
print("Element pos",result)





