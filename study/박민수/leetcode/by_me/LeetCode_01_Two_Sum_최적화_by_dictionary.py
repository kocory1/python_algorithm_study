from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map={}
        for i, n in enumerate(nums):
            if target - n in nums_map:
                return [nums_map[target-n],i]
            nums_map[n] = i






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