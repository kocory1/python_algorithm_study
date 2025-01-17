class Solution:
    def longestPalindrome(self, s: str) -> str:
        half = (len(s)-1)//2
        longest =  s[half:half+1]
        print(longest)
        for i in range(1,half):
            target = s[half-i:half+i+1]
            if target[::] == target[::-1]:
                longest = target
                print(f"longest chaged! {longest}")
        return longest

s = Solution()
print(s.longestPalindrome("babad"))