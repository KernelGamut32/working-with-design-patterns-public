from renderers.renderer import Renderer

class RasterRenderer(Renderer):
    """
    A concrete Renderer that “draws” shapes by simulating pixels.
    In a real GUI library, this might push pixels to a framebuffer.
    Here, we print descriptive messages indicating a raster approach.
    """

    def draw_circle(self, x: float, y: float, radius: float) -> None:
        print(f"[RasterRenderer] Drawing CIRCLE (raster) at ({x}, {y}) with radius {radius} "
              f"→ plotting pixels in a circular pattern")

    def draw_rectangle(self, x: float, y: float, width: float, height: float) -> None:
        print(f"[RasterRenderer] Drawing RECTANGLE (raster) at ({x}, {y}) w={width}, h={height} "
              f"→ filling pixels row by row")
        
    def draw_triangle(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float):
        print(f"[RasterRenderer] Drawing TRIANGLE (raster) with points "
            f"({x1},{y1}), ({x2},{y2}), ({x3},{y3}) → plotting pixels along edges")
        