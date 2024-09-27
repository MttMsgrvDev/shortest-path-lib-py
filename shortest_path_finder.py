from graph.graph_node import GraphNode
from point import Point


class ShortestPathFinder:
    def __init__(self, origin: GraphNode, destination: Point):
        self.origin = origin
        self.destination = destination
        self.traversed_path: list[Point] = []

    def find_shortest_path(self) -> list[Point]:

        path = self.__do_find_shortest_path(self.origin)

        if path == None:
            return None

        path.insert(0, self.origin.value)

        return path

    def __do_find_shortest_path(self, node: GraphNode) -> list[Point]:
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
        for traversed_point in self.traversed_path:
            if traversed_point == point:
                return True

        return False
