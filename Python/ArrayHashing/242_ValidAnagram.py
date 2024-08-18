class Solution():
    def isAnagram(self, s, t):
        pass


if __name__ == "__main__":
    test_obj = Solution()
    assert test_obj.isAnagram("anagram", "nagaram") == True
    assert test_obj.isAnagram("rat", "car") == False
    assert test_obj.isAnagram("racecar", "car") == False