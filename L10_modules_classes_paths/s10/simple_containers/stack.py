from .base_container import CustomContainer

# TODO - ez az órai feladat


class Stack(CustomContainer):
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def remove(self):
        """Kivesz és visszaad egy adott elemet"""
        if self.is_empty():
            raise IndexError("We cannot remove from an empty Stack!")
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __str__(self):
        if self.is_empty():
            return "Empty Stack"
        else:
            return f"""Stack({''.join([str(c) for c in self._items])})"""

    def check_last_elemt(self):
        return self._items[-1]
