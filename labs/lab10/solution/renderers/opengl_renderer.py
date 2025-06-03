from renderers.renderer import Renderer

class OpenGLRenderer(Renderer):
    def draw_circle(self, x: float, y: float, radius: float) -> None:
        print(f"[OpenGLRenderer] glBegin(GL_TRIANGLE_FAN); // Simulating circle at "
              f"({x},{y}) radius {radius} … glEnd();")

    def draw_rectangle(self, x: float, y: float, width: float, height: float) -> None:
        print(f"[OpenGLRenderer] glBegin(GL_QUADS); // Simulating rectangle at "
              f"({x},{y}) w={width}, h={height} … glEnd();")

    # If you added draw_triangle(...) above in Exercise 1, implement it here too:
    def draw_triangle(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> None:
        print(f"[OpenGLRenderer] glBegin(GL_TRIANGLES); // Simulating triangle at "
              f"({x1},{y1}), ({x2},{y2}), ({x3},{y3}) … glEnd();")
