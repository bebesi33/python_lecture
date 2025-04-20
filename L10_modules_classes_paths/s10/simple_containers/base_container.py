from abc import ABC, abstractmethod


class CustomContainer(ABC):
    """Egy egyszerű konténer a package-ek működésének szemléltetésére
    """
    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def remove(self):
        """Kivesz és visszaad egy adott elemet"""
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size(self):
        pass
