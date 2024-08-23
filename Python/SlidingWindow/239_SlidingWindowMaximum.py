class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        max_queue = collections.deque()
        left = 0
        for right in range(len(nums)):
            if max_queue and max_queue[0] < left:
                max_queue.popleft()

            while max_queue and nums[max_queue[-1]] < nums[right]:
                max_queue.pop()
            max_queue.append(right)

            if right + 1 >= k:
                res.append(nums[max_queue[0]])
                left += 1

        return res
