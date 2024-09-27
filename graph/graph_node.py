class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edges: list[GraphEdge] = []

    def add_edge(self, edge):
        self.edges.append(edge)

    def remove_edge(self, edge):
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
