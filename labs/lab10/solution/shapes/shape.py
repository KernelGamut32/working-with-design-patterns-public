from abc import ABC, abstractmethod
from renderers.renderer import Renderer

class Shape(ABC):
    """
    Abstract Shape (Bridge Abstraction). Each concrete Shape holds a reference to a Renderer
    and calls its methods when draw() is invoked. This decouples Shape hierarchies from Renderer hierarchies.
    """

    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self) -> None:
        pass
    