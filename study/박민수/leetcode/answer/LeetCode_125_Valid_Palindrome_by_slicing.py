# 이건 내가 한 거 보단 낫네
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s)
        return s == s[::-1]

print(s.isPalindrome("race a car"))
