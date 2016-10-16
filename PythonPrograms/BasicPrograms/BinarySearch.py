list = [1,3,5,45,76,89,96]
def BinarySearch(inputList,searchKey):
    first=0
    last=len(list)
    mid=-1
    while(first<=last):
        mid=(first+last)//2
        if inputList[mid]==searchKey:
            return mid+1
        elif searchKey<inputList[mid]:
            last=mid-1;
        elif searchKey>inputList[mid]:
            first=mid+1;

result = BinarySearch(list,1)   
print("Element pos",result)

