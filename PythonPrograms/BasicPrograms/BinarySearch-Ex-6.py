#Find the number of times the sorted array is rotated

def BinarySearch(a):
    first = 0
    last = len(list)-1
    mid = -1
    while(first <= last):
        if(a[first] <= a[last]):
            return first
        mid = (first + last) // 2
        next = (mid + 1) % len(list)
        prev = (mid - 1) % len(list)
        if(a[mid] <= a[next] and a[mid] <= a[prev]):
            return mid
        elif(a[mid] >= a[last]):
            first = mid + 1
        elif(a[mid] <= a[first]):
            last = mid - 1
#list = [1,3,45,46,56,89,96]              
#list = [99,96,1,2,3,4,5,6]
list = [99,96,95,93,83,4,5,6]
result = BinarySearch(list)   
print("rotated",result)

