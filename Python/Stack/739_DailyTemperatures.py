class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # (temp, index)
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                pre_temp, pre_index = stack.pop()
                result[pre_index] = index - pre_index
            stack.append((temp, index))
        return result
