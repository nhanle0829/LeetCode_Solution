class Solution(object):
    def twoSum(self, nums, target):
        pass

if __name__ == "__main__":
    test_obj = Solution()
    assert test_obj.twoSum([2,7,11,15], 9) == [0,1]
    assert test_obj.twoSum([3,2,4], 6) == [1,2]
    assert test_obj.twoSum([3,3], 6) == [0,1]
