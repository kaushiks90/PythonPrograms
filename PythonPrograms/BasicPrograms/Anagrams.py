#Given 2 strings find whether the string is Anagram 
#Example NAB and BAN 
def ReverseString(originalString,n):
    reversedString=""
    for x in range(n,0,-1):
        reversedString=reversedString+originalString[x-1]
    return reversedString


def FindIsAnagram(string1,string2):
    isAnagram=False
    if(len(string1)!=len(string2)):
        return isAnagram
    else:
        revstring1=ReverseString(string1,len(string1))
        for x in range(0,len(revstring1)):
            if(revstring1[x]!=string2[x]):
                return isAnagram
        isAnagram=True;
        return isAnagram
print("IsAnagram?",FindIsAnagram("NAB","BAN"))