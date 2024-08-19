class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        return list(count.keys())[:k]
