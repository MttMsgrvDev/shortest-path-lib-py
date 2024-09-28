from graph import GraphNode


class GraphEdge:
    def __init__(self, node1: GraphNode, node2: GraphNode, weight=None):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def __str__(self) -> str:
        weight_str = '<---->'

        if self.weight != None:
            weight_str = f'<-- {self.weight} -->'

        return f'({self.node1.value}) {weight_str} {self.node2.value}'
