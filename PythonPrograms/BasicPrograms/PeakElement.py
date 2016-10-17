#Peak Element using Linear search
def PeakElementLinearSearch(inputArray):
    peakElement = -1
    for x in range(0,len(inputArray)):
        if(len(inputArray) == 1):
           peakElement = inputArray[x]
           break
        if(x + 1 < len(inputArray)):
            if(inputArray[x] > inputArray[x + 1] and inputArray[x] > inputArray[x - 1]):
                peakElement = inputArray[x]
                break
        if(peakElement == -1 and x + 1 == len(inputArray)):
            peakElement = inputArray[x]


    return peakElement
#list=[7,3,4,5,10]
list = [2,2,2,2]
result = PeakElementLinearSearch(list)
if result == -1:
    print("Peak Element Not found")
else:
    print("Peak Element is",result)

def PeakElementBinarySearch(inputArray):
    first = 0
    last = len(inputArray)-1
    pk=-1;
    while(first <= last):
       mid = (first + last) // 2
       if((mid==0 or inputArray[mid] >= inputArray[mid - 1]) and (mid==len(inputArray)-1 or inputArray[mid] >= inputArray[mid + 1])):
        pk= inputArray[mid]
        break
       elif(inputArray[mid] <= inputArray[mid - 1]):
           last = mid - 1
       elif(inputArray[mid] >= inputArray[mid - 1]):
           first = mid + 1
    return pk
#list=[7,3,4,5,10]
list = [2,2,2,2]
Pk = PeakElementBinarySearch(list)
if Pk == -1:
    print("Peak Element Not found")
else:
    print("Peak Element is",Pk)

       







