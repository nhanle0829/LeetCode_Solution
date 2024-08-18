class Solution(object):
    def twoSum(self, nums, target):
        hash_table = {}
        for index, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target - num], index]
            hash_table[num] = index

if __name__ == "__main__":
    test_obj = Solution()
    assert test_obj.twoSum([2,7,11,15], 9) == [0,1]
    assert test_obj.twoSum([3,2,4], 6) == [1,2]
    assert test_obj.twoSum([3,3], 6) == [0,1]
