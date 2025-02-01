from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i+1:]:
                return [nums.index(n) , nums[i+1:].index(complement) + (i+1)]
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