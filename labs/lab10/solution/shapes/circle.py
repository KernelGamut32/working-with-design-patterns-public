from shapes.shape import Shape

class Circle(Shape):
    """
    Circle (RefinedAbstraction). Holds a radius and a center (x, y).
    Delegates the actual drawing to its Renderer.
    """

    def __init__(self, renderer, x: float, y: float, radius: float):
        super().__init__(renderer)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self) -> None:
        print(f"[Circle] Requesting draw_circle at ({self.x}, {self.y}) with radius {self.radius}")
        self.renderer.draw_circle(self.x, self.y, self.radius)
        