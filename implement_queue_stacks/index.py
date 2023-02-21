class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        newQueue = []
        lastPop = 0
        while len(self.queue) > 0:
            lastPop = self.queue.pop()
            if len(self.queue) == 0:
                self.queue = newQueue
                return lastPop
            newQueue.insert(0, lastPop)
        self.queue = newQueue
        return lastPop

    def peek(self) -> int:
        newQueue = []
        lastPop = 0
        while len(self.queue) > 0:
            lastPop = self.queue.pop()
            newQueue.insert(0, lastPop)
        self.queue = newQueue
        return lastPop

    def empty(self) -> bool:
        return len(self.queue) == 0
