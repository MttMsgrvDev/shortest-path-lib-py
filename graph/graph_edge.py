
class GraphEdge:
    """Represents an edge between two nodes in a graph.

    Attributes
    ----------

    node1 : GraphNode
        The first node.

    node2 : GraphNode
        The second node.

    weight : any
        The weight value of the edge.

    """

    node1 = None

    node2 = None

    weight: any = None

    def __init__(self, node1, node2, weight=None):
        """Creates a new instance of GraphEdge.

        :param node1: The first node of the edge.
        :type node1: GraphNode

        :param node2: The second node of the edge.
        :type node2: GraphNode

        :param weight: The weight associated with the edge.
        :type weight: any
        """

        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def __str__(self) -> str:
        """Returns a string representation of the GraphEdge object.

        :returns: a string representation of the GraphEdge object.
        :rtype: str
        """

        weight_str = '<---->'

        if self.weight != None:
            weight_str = f'<-- {self.weight} -->'

        return f'({self.node1.value}) {weight_str} {self.node2.value}'
