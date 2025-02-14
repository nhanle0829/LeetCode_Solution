class MyQueue:
    def __init__(self):
        self.main = []
        self.temp = []

    def push(self, x: int) -> None:
        self.temp.append(x)
        self.temp.extend(self.main)
        self.main, self.temp = self.temp, []

    def pop(self) -> int:
        return self.main.pop()

    def peek(self) -> int:
        return self.main[-1]

    def empty(self) -> bool:
        return not self.main