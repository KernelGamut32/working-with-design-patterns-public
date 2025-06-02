# shapes.py

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for any 2D shape. 
    Only requires that subclasses implement 'area()'.
    """
    @abstractmethod
    def area(self) -> float:
        """
        Compute the area of this shape. 
        """
        pass

    def __str__(self) -> str:
        """
        Provide a printable representation. 
        Subclasses may override for more detail.
        """
        return f"{self.__class__.__name__}"


class Rectangle(Shape):
    """
    Rectangle is defined by width and height passed at construction time.
    Immutable once created—no setters. 
    """
    def __init__(self, width: float, height: float):
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative")
        self._width = width
        self._height = height

    @property
    def width(self) -> float:
        return self._width

    @property
    def height(self) -> float:
        return self._height

    def area(self) -> float:
        return self._width * self._height

    def __str__(self) -> str:
        return f"Rectangle(width={self._width}, height={self._height})"


class Square(Shape):
    """
    Square is defined by a single size passed at construction time.
    Immutable once created. 
    """
    def __init__(self, size: float):
        if size < 0:
            raise ValueError("Size must be non-negative")
        self._size = size

    @property
    def size(self) -> float:
        return self._size

    def area(self) -> float:
        return self._size * self._size

    def __str__(self) -> str:
        return f"Square(size={self._size})"
