# main.py

from shapes import Rectangle, Square


def resize_rectangle(rect: Rectangle, new_width: float, new_height: float) -> Rectangle:
    """
    “Resizes” a Rectangle by constructing a brand‐new Rectangle with 
    the desired dimensions, leaving the original untouched. 
    """
    print(f"Resizing Rectangle {rect} to width={new_width}, height={new_height}")
    return Rectangle(new_width, new_height)


def resize_square(sq: Square, new_size: float) -> Square:
    """
    “Resizes” a Square by constructing a new Square of the given size. 
    """
    print(f"Resizing Square {sq} to size={new_size}")
    return Square(new_size)


def print_area(shape) -> None:
    """
    Single client function that only depends on the 'area()' contract 
    provided by Shape. It never attempts to mutate width/height.
    """
    print(f"Shape: {shape} → area = {shape.area()}")


if __name__ == "__main__":
    # 1) Work with a Rectangle
    rect = Rectangle(2, 3)
    print_area(rect)  # area = 6
    bigger_rect = resize_rectangle(rect, 4, 5)
    print_area(bigger_rect)  # area = 20

    print("---")

    # 2) Work with a Square
    sq = Square(5)
    print_area(sq)  # area = 25
    bigger_sq = resize_square(sq, 4)
    print_area(bigger_sq)  # area = 16

    print("---")

    # 3) Treat both uniformly as Shapes
    shapes = [Rectangle(3, 7), Square(6), Rectangle(10, 2), Square(2)]
    for s in shapes:
        # We never try to call set_width/set_height here—only area()
        print_area(s)
