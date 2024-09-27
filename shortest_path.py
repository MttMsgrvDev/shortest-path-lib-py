from graph.graph_node import GraphEdge, GraphNode
from point import Point
from shortest_path_finder import ShortestPathFinder

TRAVERSABLE_THRESHOLD = 5


def find_shortest_path(map: list[list[int]], origin: Point, destination: Point) -> list[Point]:
    width = len(map[0])
    height = len(map)

    graph = __convert_to_graph(map, width, height)

    start = None
    for node in graph.values():
        if node.value == origin:
            start = node
            break

    path_finder = ShortestPathFinder(start, destination)

    return path_finder.find_shortest_path()


def __convert_to_graph(map: list[list[int]], width: int, height: int) -> dict[Point, GraphNode]:
    graph_nodes = __create_edgeless_graph(width, height)

    for graph_node in graph_nodes.values():
        point = graph_node.value

        for neighbor_point in __get_neighbors(point, width, height):
            if __is_traversable(map, point, neighbor_point):
                graph_node.add_edge(
                    GraphEdge(graph_node, graph_nodes[neighbor_point], 1))

    return graph_nodes


def __create_edgeless_graph(width: int, height: int) -> dict[Point, GraphNode]:
    graph_nodes: dict[Point, GraphNode] = dict()

    for x in range(width):
        for y in range(height):
            point = Point(x, y)
            graph_nodes[point] = GraphNode(point)

    return graph_nodes


def __is_traversable(map: list[list[int]], point_from: Point, point_to: Point):

    height_from = map[point_from.y][point_from.x]

    height_to = map[point_to.y][point_to.x]

    return abs(height_from - height_to) <= TRAVERSABLE_THRESHOLD


def __get_neighbors(point: Point, width: int, height: int) -> list[Point]:
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
