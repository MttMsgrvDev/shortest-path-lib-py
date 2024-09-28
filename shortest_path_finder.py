
from graph.graph_node import GraphNode


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
        and returns it as a list of the nodes that were traversed.

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
        returns it as a list of the nodes that were traversed.

        :returns: The shortest path as list of the nodes that were traversed.
        :rtype: list[GraphNode]
        """

        path = self.__do_find_shortest_path(self.origin)

        if path == None:
            return None

        path.insert(0, self.origin)

        return path

    def __do_find_shortest_path(self, node: GraphNode) -> list[GraphNode]:
        """Finds the shortest path between the given node and the destination.

        :param node: The node to start the path from.
        :type node: GraphNode

        :returns: A list of the nodes that represent the shortest path.
        :rtype: list[GraphNode]
        """

        self.traversed_path.append(node)

        neighbors = map(lambda e: e.node2, node.edges)

        possible_paths: list[list[GraphNode]] = []

        for neighbor in neighbors:

            if neighbor == self.destination:
                return [neighbor]

            if self.__already_traveled(neighbor):
                continue

            path = self.__do_find_shortest_path(neighbor)

            if path == None:
                continue

            path.insert(0, neighbor)

            possible_paths.append(path)

        if len(possible_paths) == 0:
            return None

        shortest_path = possible_paths[0]

        for path in possible_paths[1:]:
            if len(path) < len(shortest_path):
                shortest_path = path

        return shortest_path

    def __already_traveled(self, node: GraphNode) -> bool:
        """Determines if the given point has already been traversed.

        :param node: The node to be checked.
        :type node: GraphNode

        :returns: True if the node has already been traversed, false otherwise.
        :rtype: bool
        """
        for traversed_node in self.traversed_path:
            if traversed_node == node:
                return True

        return False
