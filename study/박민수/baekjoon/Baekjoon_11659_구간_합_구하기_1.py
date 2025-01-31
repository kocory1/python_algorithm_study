# num_and_sum=list(map(int, input().split()))
# number=list(map(int,input().split()))
# prefix=[0]
# temp=0
# for i in number:
#     temp=temp+i
#     prefix.append(temp)
#
# for i in range(num_and_sum[1]):
#     start_end=list(map(int,input().split()))
#     end=start_end[1]
#     start=start_end[0]-1
#     print(prefix[end]-prefix[start])

import sys
input = sys.stdin.readline
suNo, quizNo= map(int, input().split())
numbers=list(map(int,input().split()))
prefix_sum=[0]
temp=0

for i in numbers:
    temp = temp+i
    prefix_sum.append(temp)

for i in range(quizNo):
    s, e =map(int,input().split())
    print(prefix_sum[e] - prefix_sum[s-1])


