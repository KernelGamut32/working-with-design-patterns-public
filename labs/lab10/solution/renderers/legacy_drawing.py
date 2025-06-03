class LegacyEllipse:
    """
    LegacyEllipse knows how to draw an ellipse given center (cx, cy) and radii (rx, ry).
    Its method signature does not match our Renderer interface directly.
    """

    def draw_ellipse(self, cx: float, cy: float, rx: float, ry: float) -> None:
        # In a real legacy library, this might push calls to a C/C++ backend.
        print(f"[LegacyEllipse] Drawing ellipse centered at ({cx}, {cy}) with radii ({rx}, {ry})")


class LegacyRectangle:
    """
    LegacyRectangle draws rectangles by specifying origin (x, y) and size (width, height).
    Again, the signature differs from our Renderer interface.
    """

    def draw_rectangle(self, x: float, y: float, width: float, height: float) -> None:
        print(f"[LegacyRectangle] Drawing legacy rectangle at ({x}, {y}) w={width}, h={height}")
        