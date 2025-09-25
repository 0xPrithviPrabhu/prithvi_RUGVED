from abc import ABC, abstractmethod

class Shape(ABC):
    """
    An abstract base class for a geometric shape.
    It defines the basic properties and methods that all shapes should have.
    """
    def __init__(self, c):
        self.color = c

    def get_color(self):
        """Returns the color of the shape."""
        return self.color

    @abstractmethod
    def get_area(self) -> float:
        """
        An abstract method to calculate the area of the shape.
        Subclasses must implement this method.
        """
        pass

class Square(Shape):
    """
    A class representing a square, which is a specific type of Shape.
    """
    def __init__(self, c, side):
        super().__init__(c)
        self.side = side

    def get_area(self) -> float:
        """
        Calculates and returns the area of the square.
        This method implements the abstract get_area() from the Shape class.
        """
        return self.side * self.side

if __name__ == "__main__":
    # Create an instance of the Square class
    s=input("Enter the color of the square: ")
    n=int(input("Enter the side length of the square: "))
    my_square = Square(s,n)

    # Call the get_color() method inherited from Shape
    print(f"The color of the square is: {my_square.get_color()}")

    # Call the get_area() method implemented in Square
    print(f"The area of the square is: {my_square.get_area()}")

    # --- Demonstrating Abstraction ---
    # You cannot create an object of an abstract class.
    # Uncommenting the line below would cause a TypeError.
    # invalid_shape = Shape("Blue")

