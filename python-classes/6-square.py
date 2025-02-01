#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in position:
            if not isinstance(i, int) or i < 0:
                raise TypeError("position must be a tuple of 2 positive "
                                "integers")
        self.__position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError("position must be a tuple of \
2 positive "
                                "integers")
        self.__position = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError("position must be a tuple of 2 positive "
                                "integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return int(self.__size) ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size + self.__position[1]):
                if i < self.__position[1]:
                    print()
                    continue
                for j in range(0, self.__size + self.__position[0]):
                    if j < self.__position[0]:
                        print(' ', end='')
                        continue
                    print('#', end='')
                print()
