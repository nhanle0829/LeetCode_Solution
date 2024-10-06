class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        counter = [0, 0]
        for student in students:
            counter[student] += 1

        for sandwich in sandwiches:
            if counter[sandwich] == 0:
                break
            counter[sandwich] -= 1
        return sum(counter)
