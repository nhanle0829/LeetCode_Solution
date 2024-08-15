from operator import truediv


class Solution(object):
    def containsDuplicate(self, nums):
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        return False


if __name__ == "__main__":
    testObj = Solution()
    assert testObj.containsDuplicate([1, 2, 3, 1]) is True
    assert testObj.containsDuplicate([1, 2]) is False
    assert testObj.containsDuplicate([1, 2, 3, 4]) is False
    assert testObj.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True