list = [7,3,22,46,78,90]
def LinearSearch(input,searchKey):
    (index,found) = (1,False)
    for x in input:
        if x == searchKey and found==False:
            found=True
            break
        index = index + 1            
    if found==False:
        index=-1
    return index


result = LinearSearch(list,300)
if result != -1:
    print("Element found at pos",result)
else:
    print("Element not found")
    
