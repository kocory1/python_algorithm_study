class Solution:
    def isPalindrome(self, s: str) -> bool:
        original = []
        reverse = []
        for char in s :
            if char.isalnum(): # 시발 이걸 내가 어케 알아
                original.append(char.lower())
        for i in range(len(original)-1,-1,-1):
            reverse.append(original[i])
        print(original)
        print(reverse)
        if original == reverse:
            return True
        return False

solution = Solution()
result = solution.isPalindrome("A man, a plan, a canal: Panama")
print(result)

print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(" "))

