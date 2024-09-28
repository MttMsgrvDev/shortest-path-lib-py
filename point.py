class Point:
    """Represents an x and y set of coordinates.

    Attributes
    ----------
    x : int
        The x coordinate.

    y : int
        The y coordinate.
    """

    x: int

    y: int

    def __init__(self, x: int, y: int):
        """Creates a new instance of Point

        :param x: The x coordinate.
        :type x: int

        :param y: The y coordinate.
        :type y: Point
        """
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, value: object) -> bool:
        if value == None:
            return False

        if not type(value) is Point:
            return False

        return self.x == value.x and self.y == value.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'
