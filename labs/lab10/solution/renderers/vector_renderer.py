from renderers.renderer import Renderer

class VectorRenderer(Renderer):
    """
    A concrete Renderer that “draws” shapes as vector commands.
    In a real application, this might generate SVG or some vector-graphics output.
    Here, we simply print descriptive messages.
    """

    def draw_circle(self, x: float, y: float, radius: float) -> None:
        print(f"[VectorRenderer] Drawing CIRCLE (vector) at ({x}, {y}) with radius {radius}")

    def draw_rectangle(self, x: float, y: float, width: float, height: float) -> None:
        print(f"[VectorRenderer] Drawing RECTANGLE (vector) at ({x}, {y}) w={width}, h={height}")

    def draw_triangle(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float):
        print(f"[VectorRenderer] Drawing TRIANGLE (vector) with points "
            f"({x1},{y1}), ({x2},{y2}), ({x3},{y3})")
        