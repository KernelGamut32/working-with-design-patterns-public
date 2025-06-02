# geometry_violation.py

class Rectangle:
    """
    A simple rectangle with mutable width and height.
    """
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    def set_width(self, width: float) -> None:
        self._width = width

    def set_height(self, height: float) -> None:
        self._height = height

    def get_width(self) -> float:
        return self._width

    def get_height(self) -> float:
        return self._height

    def area(self) -> float:
        return self._width * self._height

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(width={self._width}, height={self._height})"


class Square(Rectangle):
    """
    A square “is a” rectangle, but enforces width == height. 
    This override of set_width/set_height will break LSP in many clients.
    """
    def __init__(self, size: float):
        # Initialize both width and height to the same size
        super().__init__(size, size)

    def set_width(self, width: float) -> None:
        # Whenever someone sets width, force height to match
        self._width = width
        self._height = width

    def set_height(self, height: float) -> None:
        # Whenever someone sets height, force width to match
        self._width = height
        self._height = height

    # get_width, get_height, area(), __str__ are inherited from Rectangle


def resize_and_report(rect: Rectangle, new_width: float, new_height: float) -> None:
    """
    Client code that expects any Rectangle-like object to behave “normally.”
    It sets width and height independently, then prints the actual area versus expected area.
    """
    print(f"Before resize: {rect} → area = {rect.area()}")
    print(f"Resizing to width={new_width}, height={new_height}...")
    rect.set_width(new_width)
    rect.set_height(new_height)
    actual = rect.area()
    expected = new_width * new_height
    print(f"After resize: {rect} → area = {actual} (expected {expected})")
    if abs(actual - expected) > 1e-6:
        print("❌ LSP VIOLATION: actual area does not match expected!\n")
    else:
        print("✅ All good (no LSP violation for this instance).\n")


if __name__ == "__main__":
    # 1) Using a plain Rectangle:
    rect = Rectangle(2, 3)
    resize_and_report(rect, 4, 5)
    #    → width=4, height=5  ⇒ area=20, expected=20

    # 2) Using a Square, but treating it like a Rectangle:
    sq = Square(5)
    resize_and_report(sq, 4, 5)
    #    → The Square’s set_width(4) sets both sides to 4, then set_height(5) sets both sides to 5.
    #    → After these calls, width=5, height=5, so area=25, but client expected area=4*5=20.
