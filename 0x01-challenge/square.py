#!/usr/bin/python3
"""A square class."""


class square():
    """A square class."""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize a square."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        if self.width != self.height:
            self.width = self.height

    def area_of_my_square(self):
        """Return the area of the square."""
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Return the perimeter of the square."""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Return the string representation of the square."""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
