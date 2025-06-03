from abc import ABC, abstractmethod

class Renderer(ABC):
    """
    Abstract Renderer interface (Bridge “Implementor”).
    Shapes will hold a reference to a Renderer and call its methods
    to perform drawing. Concrete subclasses know how to draw shapes
    in different ways (e.g., vector vs. raster).
    """

    @abstractmethod
    def draw_circle(self, x: float, y: float, radius: float) -> None:
        pass

    @abstractmethod
    def draw_rectangle(self, x: float, y: float, width: float, height: float) -> None:
        pass

    @abstractmethod
    def draw_triangle(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> None:
        pass
