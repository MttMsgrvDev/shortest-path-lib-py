from point import Point
from shortest_path import find_shortest_path


def main(matrix: list[list[int]], origin: Point, destination: Point):
    path = find_shortest_path(matrix, origin, destination)

    print(f'{path}')


def read_rows_columns() -> tuple[int, int]:
    line = input().split()
    return int(line[0]), int(line[1])


def read_matrix() -> list[list[int]]:
    matrix = []

    (rows, columns) = read_rows_columns()

    for _ in range(rows):
        matrix_row = []
        row_input = input().split()

        for y in range(columns):
            matrix_row.append(int(row_input[y]))

        matrix.append(matrix_row)

    return matrix


def read_point() -> Point:
    values = input().split()
    return Point(int(values[0]), int(values[1]))


if __name__ == "__main__":
    matrix = read_matrix()

    origin = read_point()

    destination = read_point()

    main(matrix, origin, destination)
