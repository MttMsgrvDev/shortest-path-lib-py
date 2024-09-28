"""Shortest Path Finder

This script finds the shortest path between two points in a matrix.

Functions
---------

main(matrix: list[list[int]], origin: Point, destination: Point):

    Prints the shortest path between the origin and destination points.
"""

from point import Point
from shortest_path import find_shortest_path


def main(matrix: list[list[int]], origin: Point, destination: Point):
    """Finds the shortest path between the origin and destination
    points within the matrix and prints that path.

    :param matrix: A 2 dimensional matrix of integers that represent the elevation of that coordinate.
    :type matrix: list[list[int]]

    :param origin: The coordinate where the path should start.
    :type origin: Point

    :param destination: The coordinate where the path should end.
    :type destination: Point
    """
    path = find_shortest_path(matrix, origin, destination)

    print(f'{path}')


def __read_rows_columns() -> tuple[int, int]:
    line = input().split()
    return int(line[0]), int(line[1])


def __read_matrix() -> list[list[int]]:
    matrix = []

    (rows, columns) = __read_rows_columns()

    for _ in range(rows):
        matrix_row = []
        row_input = input().split()

        for y in range(columns):
            matrix_row.append(int(row_input[y]))

        matrix.append(matrix_row)

    return matrix


def __read_point() -> Point:
    values = input().split()
    return Point(int(values[0]), int(values[1]))


if __name__ == "__main__":
    matrix = __read_matrix()

    origin = __read_point()

    destination = __read_point()

    main(matrix, origin, destination)
