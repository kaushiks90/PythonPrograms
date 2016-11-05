# Python program to find the element occurring odd number of times
#Xor 
#  1 1->0
#  0 0->0
#  0 1->1
#  1 0->1

#  Xor 5, 5,3

#  101
#  101
#res=000
#  110
#result=  110

def getOddOccurrence(arr):
 res = 0
 for x in range(0,len(arr)):
        res = res ^ arr[x]
 return res
arr = [2,3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
print(getOddOccurrence(arr))
