#Find the common elements in 
def common_elements(arr1,arr2,arr3):
    i=0
    j=0
    k=0
    result=[]
    while(i<len(arr1) and j<len(arr2) and k<len(arr3)):
        if(arr1[i]==arr2[j] and arr2[j]==arr3[k]):
            result.append(arr1[i])
            i=i+1
            j=j+1
            k=k+1
        elif(arr1[i]<arr2[j]):
            i=i+1
        elif(arr2[j]<arr3[k]):
            j=j+1
        else:
            k=k+1
    return result

input1 = [1, 5, 10, 20, 40, 80,120]
input2 = [6, 7, 20, 80, 100,120]
input3 = [3, 4, 15, 20, 30, 70, 80, 120]
print(common_elements(input1, input2, input3))