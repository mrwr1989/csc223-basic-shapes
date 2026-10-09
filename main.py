
"""Demonstrate inheritance and polymorphism with shapes."""

from circle import Circle
from rectangle import Rectangle
from square import Square


def show_shape(shape):
    """Display a shape's name, dimensions, and area."""
    print(f"\nShape: {shape.name}")

    if isinstance(shape, Circle):
        print(f"Center: ({shape.x_center}, {shape.y_center})")
        print(f"Radius: {shape.radius}")
    elif isinstance(shape, Square):
        print(f"Side: {shape.side}")
    elif isinstance(shape, Rectangle):
        print(f"Length: {shape.length}")
        print(f"Width: {shape.width}")

    print(f"Area: {shape.area:.2f}")


def main():
    """Create shapes and demonstrate automatic area updates."""
    shapes = [
        Circle(0, 0, 3),
        Circle(2, 4, 5),
        Rectangle(4, 6),
        Rectangle(8, 3),
        Square(4)
    ]

    print("BASIC SHAPES PROJECT")
    print("Initial shapes and areas:")

    # Polymorphism: all shapes use the same interface.
    for shape in shapes:
        print(f"{shape.name}: {shape.area:.2f}")

    print("\nDIMENSION CHANGE DEMONSTRATIONS")

    circle = shapes[0]
    print("\nBefore changing circle radius:")
    show_shape(circle)
    circle.radius = 6
    print("After changing circle radius:")
    show_shape(circle)

    rectangle = shapes[2]
    print("\nBefore changing rectangle dimensions:")
    show_shape(rectangle)
    rectangle.length = 10
    rectangle.width = 5
    print("After changing rectangle dimensions:")
    show_shape(rectangle)

    square = shapes[4]
    print("\nBefore changing square side:")
    show_shape(square)
    square.side = 7
    print("After changing square side:")
    show_shape(square)


if __name__ == "__main__":
    main()
