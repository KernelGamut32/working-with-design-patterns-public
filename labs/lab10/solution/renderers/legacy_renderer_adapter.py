from renderers.renderer import Renderer
from renderers.legacy_drawing import LegacyEllipse, LegacyRectangle

class LegacyRendererAdapter(Renderer):
    """
    Adapter that wraps the legacy drawing API (LegacyEllipse & LegacyRectangle)
    and exposes the modern Renderer interface. This allows existing shape code
    to use the legacy library without modification.
    """

    def __init__(self):
        # Instantiate legacy objects internally
        self.legacy_ellipse = LegacyEllipse()
        self.legacy_rectangle = LegacyRectangle()

    def draw_circle(self, x: float, y: float, radius: float) -> None:
        # LegacyEllipse’s draw_ellipse takes two radii. We pass radius for both rx and ry.
        print("[LegacyRendererAdapter] Adapting draw_circle → draw_ellipse")
        self.legacy_ellipse.draw_ellipse(cx=x, cy=y, rx=radius, ry=radius)

    def draw_rectangle(self, x: float, y: float, width: float, height: float) -> None:
        print("[LegacyRendererAdapter] Adapting draw_rectangle → legacy rectangle draw")
        self.legacy_rectangle.draw_rectangle(x=x, y=y, width=width, height=height)

    def draw_triangle(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float):
        print(f"[LegacyRendererAdapter] Does not support TRIANGLE")
