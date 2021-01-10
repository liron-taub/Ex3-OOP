import math


class NodeData:
    id_counter = 0

    def __init__(self, key=id_counter, pos=None):
        self.key = key
        self.pos = pos
        self.weight = math.inf
        self.pred = -math.inf
        self.visited = False
        self.in_edges = 0
        self.out_edges = 0
        if key == NodeData.id_counter:
            NodeData.id_counter += 1

    def __gt__(self, other):
        return self.weight > other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self) -> str:
        return str(self.key) + ": |edges out| " + str(self.out_edges) + " |edges in| " + str(self.in_edges)

    def __eq__(self, o: object) -> bool:
        if o == None or type(self).__name__ != type(o).__name__:
            return False
        if self.in_edges != o.in_edges:
            return False

        if self.out_edges != o.out_edges:
            return False

        if self.key != o.key:
            return False

        return self.pos != o.pos




