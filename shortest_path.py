"""Shortest path driver functions.

This Module contains functions execute the shortest path algorithm
against a graph whose nodes represent coordinates within a matrix.

Functions
---------

find_shortest_path(matrix: list[list[int]], origin: Point, destination: Point) -> list[Point]

    Finds the shortest path between two points within a matrix.
"""

from graph.graph_edge import GraphEdge
from graph.graph_node import GraphNode
from point import Point
from shortest_path_finder import ShortestPathFinder

__TRAVERSABLE_THRESHOLD = 5


def find_shortest_path(matrix: list[list[int]], origin: Point, destination: Point) -> list[Point]:
    """Finds the shortest path between two points within a matrix.

    :param matrix: A 2 dimensional matrix of integers that represent the elevation of that coordinate.
    :type matrix: list[list[int]]

    :param origin: The coordinate where the path should start.
    :type origin: Point

    :param destination: The coordinate where the path should end.
    :type destination: Point

    :returns: A list of points that represent the shortest path from the origin to the destination.
    :rtype: list[Point]
    """

    width = len(matrix[0])
    height = len(matrix)

    graph = __convert_to_graph(matrix, width, height)

    path_finder = ShortestPathFinder(graph[origin], graph[destination])

    return list(map(lambda n: n.value, path_finder.find_shortest_path()))


def __convert_to_graph(matrix: list[list[int]], width: int, height: int) -> dict[Point, GraphNode]:
    """Converts the given matrix into a graph where each node represents a
    coordinate in that matrix. Each node will have an edge to neighboring coordinates if the elevation difference is less than 5.

    :param matrix: A 2 dimensional matrix of integers that represent the elevation of that coordinate.
    :type matrix: list[list[int]]

    :param width: The number of columns in the matrix.
    :type width: int

    :param height: The number of rows in the matrix.
    :type height: int

    :returns: A dictionary where the key is a coordinate and the value is the GraphNode for that coordinate.
    :rtype: dict[Point, GraphNode]
    """
    graph_nodes = __create_edgeless_graph(width, height)

    for graph_node in graph_nodes.values():
        point = graph_node.value

        for neighbor_point in __get_neighbors(point, width, height):
            if __is_traversable(matrix, point, neighbor_point):
                graph_node.add_edge(
                    GraphEdge(graph_node, graph_nodes[neighbor_point], 1))

    return graph_nodes


def __create_edgeless_graph(width: int, height: int) -> dict[Point, GraphNode]:
    """Converts the given matrix into a graph where each node represents a
    coordinate in that matrix. None of the nodes are connected.

    :param width: The number of columns in the matrix.
    :type width: int

    :param height: The number of rows in the matrix.
    :type height: int

    :returns: A dictionary where the key is a coordinate and the value is the GraphNode for that coordinate.
    :rtype: dict[Point, GraphNode]
    """

    graph_nodes: dict[Point, GraphNode] = dict()

    for x in range(width):
        for y in range(height):
            point = Point(x, y)
            graph_nodes[point] = GraphNode(point)

    return graph_nodes


def __is_traversable(matrix: list[list[int]], point_from: Point, point_to: Point):
    """Determines whether a path from one point to its neighbor is traversable.

    :param matrix: A 2 dimensional matrix of integers that represent the elevation of that coordinate.
    :type matrix: list[list[int]]

    :param point_from: The point we would be traveling from.
    :type point_from: Point

    :param point_to: The neighbor we would be traveling to.
    :type point_to: Point

    :returns: True if the difference in elevation is less than or equal to the preconfigured threshold.
    :rtype: bool
    """

    height_from = matrix[point_from.y][point_from.x]

    height_to = matrix[point_to.y][point_to.x]

    return abs(height_from - height_to) <= __TRAVERSABLE_THRESHOLD


def __get_neighbors(point: Point, width: int, height: int) -> list[Point]:
    """Gets all the nieghbors for the given point.

    :param point: The point to retrieve neighbors for.
    :type point: Point

    :param width: The number of columns in the matrix.
    :type width: int

    :param height: The number of rows in the matrix.
    :type height: int

    :returns: A list of the neighbors of the given point.
    :rtype: list[Point]
    """

    neighbors = []

    if point.x < width - 1:
        neighbors.append(Point(point.x + 1, point.y))

    if point.x > 0:
        neighbors.append(Point(point.x - 1, point.y))

    if point.y < height - 1:
        neighbors.append(Point(point.x, point.y + 1))

    if point.y > 0:
        neighbors.append(Point(point.x, point.y - 1))

    return neighbors
