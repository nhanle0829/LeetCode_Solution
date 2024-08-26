class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left_rate, right_rate = 1, max(piles)
        min_eat_rate = right_rate
        while left_rate <= right_rate:
            mid_rate = left_rate + (right_rate - left_rate) // 2
            hour_need = 0
            for pile in piles:
                hour_need += math.ceil(pile / mid_rate)
            if hour_need > h:
                left_rate = mid_rate + 1
            else:
                min_eat_rate = mid_rate
                right_rate = mid_rate - 1

        return min_eat_rate
