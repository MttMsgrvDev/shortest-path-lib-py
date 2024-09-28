
class GraphNode:
    """Represents a node in a graph.

    Attributes
    ----------

    value : any
        The "value" of the node. Should be of a type that is equatable and hashable.

    edges : list[GraphEdge]
        The edges that connect this node to other nodes in the graph.

    Methods
    -------

    add_edge(edge: GraphEdge)
        Adds the given edge to connect this node to the other node along the edge.

    remove_edge(edge: GraphEdge)
        Removes the given edge to disconnect it from the other node along the edge.

    """

    value: any = None

    edges: list = []

    def __init__(self, value):
        """Creates a new instance of GraphNode.

        :param value: The "value" of the node
        :type value: any
        """
        self.value = value
        self.edges = []

    def add_edge(self, edge):
        """Adds the given edge to connect this node to the other node along the edge.

        :param edge: The edge that connects the node to another node in the graph.
        :type edge: GraphEdge
        """

        self.edges.append(edge)

    def remove_edge(self, edge):
        """Removes the given edge to disconnect it from the other node along the edge.

        :param edge: The edge that connects the node to another node in the graph.
        :type edge: GraphEdge
        """

        remove_index = -1

        for index, self_edge in self.edges:
            if self_edge.node2.value == edge.node2.value:
                remove_index = index

        if remove_index >= 0:
            self.edges.pop(remove_index)

    def __str__(self) -> str:
        edges_str = ', '.join(map(lambda e: f'{e.node2.value}', self.edges))

        return f'({self.value}, [{edges_str}])'

    def __repr__(self) -> str:
        return f'({self.value}, {self.edges})'

    def __eq__(self, value: object) -> bool:
        if value == None:
            return False

        if not type(value) is GraphNode:
            return False

        return value.value == self.value

    def __hash__(self) -> int:
        return hash(self.value)
