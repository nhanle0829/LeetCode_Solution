class Solution:
    def groupAnagrams(self, strs):
        pass

if __name__ == "__main__":
    test_obj = Solution()
    assert test_obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["tan","nat"],["bat"],["eat","tea","ate"]]
    assert test_obj.groupAnagrams([""]) == [[""]]
    assert test_obj.groupAnagrams(["a"]) == [["a"]]