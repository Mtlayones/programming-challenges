class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        length = len(self.stack)
        while length > 1:
            self.stack.append(self.stack.pop(0))
            length -= 1
        return self.stack.pop(0)

    def top(self) -> int:
        top = self.pop()
        self.stack.append(top)
        return top

    def empty(self) -> bool:
        return len(self.stack) == 0


if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
