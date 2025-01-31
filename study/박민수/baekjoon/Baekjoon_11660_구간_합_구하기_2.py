import sys
input = sys.stdin.readline

n,m=map(int,input().split())
square=[[0]*(n+1)]
prefix=[[0] * (n+1) for _ in range (n+1)]
for i in range(n):
    row = [0] + [int(x) for x in input().split()]
    square.append(row)


for i in range(1,n+1):
    for j in range(1,n+1):
        prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + square[i][j]

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split()) #2,2,3,4
    result = prefix[x2][y2] - prefix[x1-1][y2] - prefix [x2][y1-1] + prefix[x1-1][y1-1]
    print(result)



















# import sys
# input = sys.stdin.readline
# n,m = map(int,input().split())
# A = [[0]* (n+1)]
# D = [[0] * (n+1) for _ in range(n+1)]
#
# for i in range(n):
#     A_row = [0] + [int(x) for x in input().split()]
#     A.append(A_row)
# print(A)
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         D[i][j] = D[i][j-1]+D[i-1][j]-D[i-1][j-1]+A[i][j]
# print(D)
# for _ in range(m):
#     x1, y1, x2, y2 =map(int,input().split())
#     result = D[x2][y2]-D[x1-1][y2]-D[x2][y1-1]+D[x1-1][y1-1]
#     print(result)