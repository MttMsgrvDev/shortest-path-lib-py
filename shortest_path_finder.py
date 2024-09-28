from graph.graph_node import GraphNode
from point import Point


class ShortestPathFinder:
    """An object that can find the shortest path between two nodes in a graph.

    Attributes
    ----------

    origin : GraphNode
        The node where the path begins.

    destination : GraphNode
        The node where the path should end.

    traversed_path : list[GraphNode]
        The path that has been traversed so far on the way to finding the
        shortest path.


    Methods
    -------

    find_shortest_path() -> list[GraphNode]

        Finds the shortest path between the origin and the destination
        and returns it as a list of the points that were traversed.

    """

    origin: GraphNode = None

    destination: GraphNode = None

    traversed_path: list[GraphNode] = []

    def __init__(self, origin: GraphNode, destination: GraphNode):
        """Creates a new instance of ShortestPathFinder.

        :param origin: The node where the path begins.
        :type origin: GraphNode

        :param destination: The node where the path should end.
        :type destination: GraphNode
        """
        self.origin = origin
        self.destination = destination

    def find_shortest_path(self) -> list[GraphNode]:
        """Finds the shortest path between the origin and the destination and
        returns it as a list of the points that were traversed.

        :returns: a list of the points that were traversed.
        :rtype: list[GraphNode]
        """

        path = self.__do_find_shortest_path(self.origin)

        if path == None:
            return None

        path.insert(0, self.origin.value)

        return path

    def __do_find_shortest_path(self, node: GraphNode) -> list[Point]:
        """Finds the shortest path between the given node and the destination.

        :param node: The node to start the path from.
        :type node: GraphNode

        :returns: A list of the points that represent the shortest path.
        :rtype: list[Point]
        """
        self.traversed_path.append(node.value)

        neighbors = map(lambda e: e.node2, node.edges)

        possible_paths: list[list[Point]] = []

        for neighbor in neighbors:
            if neighbor.value == self.destination:
                return [neighbor.value]

            if self.__already_traveled(neighbor.value):
                continue

            path = self.__do_find_shortest_path(neighbor)

            if path == None:
                continue

            path.insert(0, neighbor.value)

            possible_paths.append(path)

        if len(possible_paths) == 0:
            return None

        shortest_path = possible_paths[0]

        for path in possible_paths[1:]:
            if len(path) < len(shortest_path):
                shortest_path = path

        return shortest_path

    def __already_traveled(self, point: Point) -> bool:
        """Determines if the given point has already been traversed.

        :param point: The point to be checked.
        :type point: Point

        :returns: True if the point has already been traversed, false otherwise.
        :rtype: bool
        """
        for traversed_point in self.traversed_path:
            if traversed_point == point:
                return True

        return False
