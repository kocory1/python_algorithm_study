from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        # print(s)

solution = Solution()
solution.reverseString(["h","e","l"])
