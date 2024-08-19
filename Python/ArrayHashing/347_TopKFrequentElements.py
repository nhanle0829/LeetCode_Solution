class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for n, f in count.items():
            freq[f].append(n)

        for i in range(len(nums), 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
