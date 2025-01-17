# 이건 내가 한 거 보단 낫네
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import collections
        strs: Deque = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True
s = Solution()

print(s.isPalindrome("race a car"))
