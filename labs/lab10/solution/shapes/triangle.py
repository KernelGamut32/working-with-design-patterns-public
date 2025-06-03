from shapes.shape import Shape

class Triangle(Shape):
    def __init__(self, renderer, x1: float, y1: float,
                              x2: float, y2: float,
                              x3: float, y3: float):
        super().__init__(renderer)
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

    def draw(self) -> None:
        print(f"[Triangle] Requesting draw_triangle at points "
              f"({self.x1},{self.y1}), ({self.x2},{self.y2}), ({self.x3},{self.y3})")
        # **Assume** we want a new method on Renderer: draw_triangle(...)
        self.renderer.draw_triangle(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)
        