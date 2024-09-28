class Point:
    def __init__(self, x, y):
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
