def MajorityElementIterative(inputArray):
    count=1
    for x in range(0,len(inputArray)):
        for y in range(x+1,len(inputArray)):
            if inputArray[x]==inputArray[y]:
                count=count+1
        if count>len(inputArray)//2:
            return inputArray[x]
        count=1

#list=[1,7,6,1,0]
#list=[0,0,0,0,0]
list=[1,2,2,2,3]
result=MajorityElementIterative(list)
print(result)

def MajorityBoyerMoore(inputArray):
    count=0
    majorityElement=0
    for x in range(0,len(inputArray)):
        if count==0:
            majorityElement=inputArray[x]
            count=1;
            continue
        else:
            if majorityElement==inputArray[x]:
                count=count+1
            else:
                count=count-1
    if count>0:
       return majorityElement


def ValidateMajorityElement(inputArray):
    output=False
    result=MajorityBoyerMoore(inputArray)
    count=0
    for x in range(0,len(inputArray)):
        if result==inputArray[x]:
            count=count+1
        if (count>len(inputArray)//2):
            output= True
    if output==True:
        print(result)
    else:
        print("None")
        
ValidateMajorityElement(list)




                
    