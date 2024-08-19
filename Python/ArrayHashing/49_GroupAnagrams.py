class Solution:
    def groupAnagrams(self, strs):
        hash_map = {}
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in hash_map:
                hash_map[tuple(count)] = []
            hash_map[tuple(count)].append(str)
        return list(hash_map.values())

if __name__ == "__main__":
    test_obj = Solution()
    print(test_obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    assert test_obj.groupAnagrams([""]) == [[""]]
    assert test_obj.groupAnagrams(["a"]) == [["a"]]