from collections import deque
from .base_container import CustomContainer


class Queue(CustomContainer):
    def __init__(self):
        self._queue = deque()

    def add(self, item):
        self._queue.append(item)  # FIFO

    def remove(self):
        if self.is_empty():
            raise IndexError("We cannot remove from an empty Queue!")
        return self._queue.popleft()

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)

    def __str__(self):
        return f"Queue({list(self._queue)})"
