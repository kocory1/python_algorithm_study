# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# A = [int(i) for i in input().split()]
# count=0
# prefix = [[0] * (n + 1)]
# for i in range(1, n + 1):
#     prefix.append([0] * (n + 1))
#     for j in range(1, n + 1):
#         prefix[i][j] = prefix[1][j-1]+A[j-1]-prefix[1][i-1]
#         if prefix[i][j] % m == 0 and prefix[i][j]>0:
#             count+=1
# print(count)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m
S[0] = A[0]
answer = 0

for i in range(1, n):
    S[i] = S[i - 1] + A[i]

for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        answer += 1
    C[remainder] += 1

for i in range(m):
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1) // 2)

print(answer)