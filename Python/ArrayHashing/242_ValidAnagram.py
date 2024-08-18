class Solution():
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        letter_hash = [0] * 26
        for char in s:
            letter_hash[ord(char) - ord('a')] += 1
        for char in t:
            letter_hash[ord(char) - ord('a')] -= 1
        for i in range(26):
            if letter_hash[i] != 0:
                return False
        return True

if __name__ == "__main__":
    test_obj = Solution()
    assert test_obj.isAnagram("anagram", "nagaram") == True
    assert test_obj.isAnagram("rat", "car") == False
    assert test_obj.isAnagram("racecar", "car") == False