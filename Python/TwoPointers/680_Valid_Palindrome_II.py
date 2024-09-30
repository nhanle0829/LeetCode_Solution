class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.checkPalindrome(l + 1, r, s) or self.checkPalindrome(l, r - 1, s)
            l += 1;
            r -= 1
        return True

    def checkPalindrome(self, left, right, s):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1;
            right -= 1
        return True