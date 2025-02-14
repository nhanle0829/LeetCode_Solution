from collections import deque

class MyStack:
    def __init__(self):
        self.main = deque()
        self.temp = deque()

    def push(self, x: int) -> None:
        self.temp.append(x)
        self.temp.extend(self.main)
        self.main, self.temp = self.temp, deque()

    def pop(self) -> int:
        return self.main.popleft()

    def top(self) -> int:
        return self.main[0]

    def empty(self) -> bool:
        return not self.main