from numpy import *

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
sum=0
#algo to matrix multiplication
rowsm1 = len(X)
columnsm1 = len(X[0])
rowsm2=len(Y)
columnm2 =len(Y[0])
print(rowsm1,columnsm1)
print(rowsm2,columnm2)
for i in range(0,rowsm1):
    for j in range(0,columnm2):
        for k in range(0,columnsm1):
            sum+=X[i][k] *Y[k][j]
            k+=1

        result[i][j]=sum
        j+=1
        sum=0
    i+=1

print(result)