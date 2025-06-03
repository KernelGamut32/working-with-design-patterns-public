from renderers.vector_renderer import VectorRenderer
from renderers.raster_renderer import RasterRenderer
from renderers.opengl_renderer import OpenGLRenderer
from renderers.legacy_renderer_adapter import LegacyRendererAdapter

from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.composite_shape import CompositeShape
from shapes.triangle import Triangle

def main():
    print("=== DEMO: Bridge, Adapter, and Composite Patterns Combined ===\n")

    # ---------------------------------------------------------------------
    # 1) Bridge: Create individual shapes with concrete renderers.
    # ---------------------------------------------------------------------
    print("1) Bridge Pattern Demo (Vector vs. Raster):")
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()
    opengl_renderer = OpenGLRenderer()

    # Create two circles, one drawn by vector, one by raster.
    circle_vector = Circle(renderer=vector_renderer, x=5, y=5, radius=3)
    circle_raster = Circle(renderer=raster_renderer, x=15, y=15, radius=5)
    circle_opengl = Circle(renderer=opengl_renderer, x=10, y=10, radius=4)

    circle_vector.draw()
    circle_raster.draw()
    circle_opengl.draw()

    # Create two rectangles, one drawn by vector, one by raster.
    rectangle_vector = Rectangle(renderer=vector_renderer, x=2, y=2, width=10, height=4)
    rectangle_raster = Rectangle(renderer=raster_renderer, x=20, y=10, width=8, height=6)
    rectangle_opengl = Rectangle(renderer=opengl_renderer, x=12, y=12, width=5, height=3)

    rectangle_vector.draw()
    rectangle_raster.draw()
    rectangle_opengl.draw()

    print("\n" + "-" * 60 + "\n")

    triangle_vector = Triangle(renderer=vector_renderer,
                            x1=0, y1=0, x2=5, y2=5, x3=10, y3=0)
    triangle_raster = Triangle(renderer=raster_renderer,
                            x1=2, y1=1, x2=6, y2=7, x3=9, y3=2)
    triangle_opengl = Triangle(renderer=opengl_renderer,
                            x1=3, y1=3, x2=8, y2=8, x3=12, y3=4)

    triangle_vector.draw()
    triangle_raster.draw()    
    triangle_opengl.draw()

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

    print("\n" + "-" * 60 + "\n")

    layer1 = CompositeShape()
    layer1.add(Circle(renderer=vector_renderer, x=1, y=1, radius=1))
    layer1.add(Rectangle(renderer=raster_renderer, x=2, y=2, width=2, height=1))

    layer2 = CompositeShape()
    layer2.add(Circle(renderer=legacy_adapter, x=5, y=5, radius=3))
    layer2.add(Rectangle(renderer=opengl_renderer, x=6, y=1, width=1, height=2))

    scene = CompositeShape()
    scene.add(layer1)
    scene.add(layer2)

    # Finally draw the scene
    scene.draw()

    print("\n=== END OF DEMO ===")

if __name__ == "__main__":
    main()
    