class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        heap_size = len(nums)
        self.build_max_heap(nums, heap_size)

        left, right = 0, heap_size - 1
        while right > left:
            nums[left], nums[right] = nums[right], nums[left]
            self.max_heapify(nums, right, left)
            right -= 1
        return nums

    def max_heapify(self, array, size, root_index):
        largest = root_index
        left = root_index * 2 + 1
        right = root_index * 2 + 2
        if left < size and array[largest] < array[left]:
            largest = left
        if right < size and array[largest] < array[right]:
            largest = right

        if largest != root_index:
            array[largest], array[root_index] = array[root_index], array[largest]
            self.max_heapify(array, size, largest)

    def build_max_heap(self, array, size):
        start = size // 2 - 1
        for i in range(start, -1, -1):
            self.max_heapify(array, size, i)
