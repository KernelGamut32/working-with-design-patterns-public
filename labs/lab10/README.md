# Lab 10 - Adapter, Bridge, & Composite Patterns

## Overview

In this lab, you will explore a small Python application that demonstrates three essential design patterns—Adapter, Bridge, and Composite—working together in a single codebase. The application draws various shapes (Circle, Rectangle) using different rendering backends (vector, raster, and a legacy API), and groups shapes into composites.

---

## Learning Objectives

By the end of this lab, you should be able to:

1. Identify the roles of Abstraction, Implementor, and ConcreteImplementors in the Bridge pattern.
2. Understand how the Adapter pattern “wraps” a legacy interface so that it conforms to a modern interface.
3. Recognize how the Composite pattern lets you treat individual objects (leaves) and groups of objects uniformly.
4. Navigate a multi‐module Python project, run it, and trace through method calls.
5. Modify or extend the sample application (e.g., add a new shape or a new renderer).

---

## Prerequisites

Before you begin, ensure the following:

1. Python 3.8+ installed - Confirm by running `python --version` in your terminal.
2. An editor or IDE capable of editing multiple `.py` files (e.g., VS Code, PyCharm, Sublime Text).
3. Familiarity with basic OOP in Python - You should know what classes, methods, and imports/modules are.
4. Basic comfort with the command line - You’ll navigate directories and launch Python scripts.

---

## File Structure

Create a new folder on your local machine (e.g., `abc_patterns_demo/`). Inside that folder, create four files exactly as named below:

```text
abc_patterns_demo/
│
├── renderers/
│   ├── __init__.py
│   ├── renderer.py
│   ├── vector_renderer.py
│   ├── raster_renderer.py
│   ├── legacy_drawing.py
│   └── legacy_renderer_adapter.py
│
├── shapes/
│   ├── __init__.py
│   ├── shape.py
│   ├── circle.py
│   ├── rectangle.py
│   └── composite_shape.py
│
└── main.py
```

---

## Examine the Code

renderers/renderer.py

```python
from abc import ABC, abstractmethod

class Renderer(ABC):
    """
    Abstract Renderer interface (Bridge “Implementor”).
    Shapes will hold a reference to a Renderer and call its methods
    to perform drawing. Concrete subclasses know how to draw shapes
    in different ways (e.g., vector vs. raster).
    """

    @abstractmethod
    def draw_circle(self, x: float, y: float, radius: float) -> None:
        pass

    @abstractmethod
    def draw_rectangle(self, x: float, y: float, width: float, height: float) -> None:
        pass
```

renderers/vector_renderer.py

```python
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
```

renderers/raster_renderer.py

```python
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
```

renderers/legacy_drawing.py

```python
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
```

renderers/legacy_renderer_adapter.py

```python
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
```

shapes/shape.py

```python
from abc import ABC, abstractmethod
from renderers.renderer import Renderer

class Shape(ABC):
    """
    Abstract Shape (Bridge Abstraction). Each concrete Shape holds a reference to a Renderer
    and calls its methods when draw() is invoked. This decouples Shape hierarchies from Renderer hierarchies.
    """

    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self) -> None:
        pass
```

shapes/circle.py

```python
from shapes.shape import Shape

class Circle(Shape):
    """
    Circle (RefinedAbstraction). Holds a radius and a center (x, y).
    Delegates the actual drawing to its Renderer.
    """

    def __init__(self, renderer, x: float, y: float, radius: float):
        super().__init__(renderer)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self) -> None:
        print(f"[Circle] Requesting draw_circle at ({self.x}, {self.y}) with radius {self.radius}")
        self.renderer.draw_circle(self.x, self.y, self.radius)
```

shapes/rectangle.py

```python
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
```

shapes/composite_shape.py

```python
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
```

main.py

```python
from renderers.vector_renderer import VectorRenderer
from renderers.raster_renderer import RasterRenderer
from renderers.legacy_renderer_adapter import LegacyRendererAdapter

from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.composite_shape import CompositeShape

def main():
    print("=== DEMO: Bridge, Adapter, and Composite Patterns Combined ===\n")

    # ---------------------------------------------------------------------
    # 1) Bridge: Create individual shapes with concrete renderers.
    # ---------------------------------------------------------------------
    print("1) Bridge Pattern Demo (Vector vs. Raster):")
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    # Create two circles, one drawn by vector, one by raster.
    circle_vector = Circle(renderer=vector_renderer, x=5, y=5, radius=3)
    circle_raster = Circle(renderer=raster_renderer, x=15, y=15, radius=5)

    circle_vector.draw()
    circle_raster.draw()

    # Create two rectangles, one drawn by vector, one by raster.
    rectangle_vector = Rectangle(renderer=vector_renderer, x=2, y=2, width=10, height=4)
    rectangle_raster = Rectangle(renderer=raster_renderer, x=20, y=10, width=8, height=6)

    rectangle_vector.draw()
    rectangle_raster.draw()

    print("\n" + "-" * 60 + "\n")

    # ---------------------------------------------------------------------
    # 2) Adapter: Use a legacy drawing API to draw a shape.
    # ---------------------------------------------------------------------
    print("2) Adapter Pattern Demo (Legacy Renderer):")
    legacy_adapter = LegacyRendererAdapter()

    # We can now create shapes with a renderer that is actually the legacy API under the hood.
    legacy_circle = Circle(renderer=legacy_adapter, x=0, y=0, radius=7)
    legacy_rectangle = Rectangle(renderer=legacy_adapter, x=10, y=5, width=4, height=2)

    legacy_circle.draw()
    legacy_rectangle.draw()

    print("\n" + "-" * 60 + "\n")

    # ---------------------------------------------------------------------
    # 3) Composite: Group shapes (Bridge + Composite).
    # ---------------------------------------------------------------------
    print("3) Composite Pattern Demo (Grouping Shapes):")
    # Top-level composite
    picture = CompositeShape()

    # Add a mixture of shapes using different renderers
    picture.add(circle_vector)
    picture.add(rectangle_vector)

    # A sub-composite that uses raster rendering
    sub_group = CompositeShape()
    sub_group.add(circle_raster)
    sub_group.add(rectangle_raster)

    # Add the sub-group to the main composite
    picture.add(sub_group)

    # A nested composite that uses the legacy adapter
    legacy_group = CompositeShape()
    legacy_group.add(legacy_circle)
    legacy_group.add(legacy_rectangle)

    picture.add(legacy_group)

    # Draw the entire picture (Composite draws all children recursively)
    picture.draw()

    print("\n=== END OF DEMO ===")

if __name__ == "__main__":
    main()
```

To execute/test, run `python main.py`

---

## Additional Exercises (Time Permitting)

### Exercise 1: Add a New Shape (`Triangle`)

Create a `Triangle` class that fits into the existing Bridge + Composite framework.

### Exercise 2: Add a New Renderer (`OpenGLRenderer`)

Simulate an OpenGL-style renderer that logs "OpenGL calls" instead of "vector" or "raster".

### Exercise 3: Extend the Composite Concept to Include Nested Groups

Build deeper nesting of composites-e.g., a "scene" that contains multiple "layers", each of which contains multiple "groups" of shapes. **Hint:** The only change required is in `main.py`.
