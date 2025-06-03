from shapes.shape import Shape

class CompositeShape(Shape):
    """
    CompositeShape (Composite Leaf). Allows grouping multiple Shape instances
    and drawing them as a unit. Implements the same draw() interface.
    """

    def __init__(self):
        # Note: CompositeShape does not need its own Renderer; each child has its renderer.
        super().__init__(renderer=None)
        self.children = []

    def add(self, shape: Shape) -> None:
        self.children.append(shape)

    def remove(self, shape: Shape) -> None:
        self.children.remove(shape)

    def draw(self) -> None:
        print(f"[CompositeShape] Drawing CompositeShape with {len(self.children)} child(ren).")
        for child in self.children:
            child.draw()
            