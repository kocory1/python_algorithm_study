from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
#
#
# s = Solution()
# result = s.twoSum([2, 7, 11, 15], 9)
# print(result)
#
# result = s.twoSum([3,2,4], 6)
# print(result)
#
# result = s.twoSum([3,3], 6)
#
# print(result)