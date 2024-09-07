class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        max_freq = max(counter.values())

        max_freq_tasks = 0
        for freq in counter.values():
            if max_freq == freq:
                max_freq_tasks += 1

        min_time = (max_freq - 1) * (n + 1) + max_freq_tasks
        return max(min_time, len(tasks))
