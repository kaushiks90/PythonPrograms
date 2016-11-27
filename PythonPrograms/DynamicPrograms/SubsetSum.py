# Given an array of non negative numbers and a total, is there subset of numbers in this array which adds up to given total

def SubSetSumProblem(input,total):
  
    T = [[0 for col in range(total+1)] for row in range(len(input))]
    for x in range(0,len(input)):
        T[x][0] = True
    for i in range(1,len(input)):
        for j in range(1,total+1):
            if (j - input[i - 1] >= 0): 
                    T[i][j] = T[i - 1][j] or T[i - 1][j - input[i - 1]];
            else :
                    T[i][j] = T[i-1][j];
    return T[len(input)-1][total];
              

input=[2,3,7,8,10]
sum = 13
print(SubSetSumProblem(input,sum))

    