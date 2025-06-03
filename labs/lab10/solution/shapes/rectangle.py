from shapes.shape import Shape

class Rectangle(Shape):
    """
    Rectangle (RefinedAbstraction). Has an origin (x, y), width, and height.
    Delegates actual drawing to its Renderer.
    """

    def __init__(self, renderer, x: float, y: float, width: float, height: float):
        super().__init__(renderer)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self) -> None:
        print(f"[Rectangle] Requesting draw_rectangle at ({self.x}, {self.y}) w={self.width}, h={self.height}")
        self.renderer.draw_rectangle(self.x, self.y, self.width, self.height)
        