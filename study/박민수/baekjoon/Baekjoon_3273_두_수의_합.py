import sys
input = sys.stdin.readline

n = int(input())
nums = [int(n) for n in input().split()]
target = int(input())
nums_map = {}
count=0

for i, num in enumerate(nums):
    nums_map[num] = i
    if target-num in nums_map and target-num != num:
        count+=1
print(count)



