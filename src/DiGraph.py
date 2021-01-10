from src.GraphInterface import GraphInterface
from src.NodeData import NodeData


class DiGraph(GraphInterface):
    def __init__(self):
        self.nodes = dict()
        self.edges = dict()
        self.edgeSize = 0
        self.modeCount = 0

    def v_size(self) -> int: # Returns the amount of vertices
        return len(self.nodes)

    def e_size(self) -> int:# Returns the amount of edges
        return self.edgeSize

    def get_all_v(self) -> dict: #Returns a dictionary of the entire vertex
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:# Returns a dictionary of all incoming edges of a particular vertex if any
        try:
            return self.edges[id1]["IN"] #Turning to the edge of a particular vertex instead of id and instead of in.
                                         #We will get the dictionary of incoming edges and their weight
        except:
            return dict()

    def all_out_edges_of_node(self, id1: int) -> dict:# Returns a dictionary of all outgoing ribs of a particular vertex if any
        try:
            return self.edges[id1]["OUT"]#Facing the rib of a particular vertex instead of id and instead of out.
                                          #We will get the dictionary of the outgoing ribs and their weight
        except:
            return dict()

    def get_mc(self) -> int:
        return self.modeCount

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if weight < 0:
            print("the Weight of edge must be positive")
            return False

        if id1 == id2:
            print(" There is no edge between a node and itself ")
            return False

        if id1 not in self.nodes or id2 not in self.nodes:
            print("one of the nodes are not exist")
            return False

        if id2 in self.edges[id1]["OUT"]: #If id2 = dest is in the list on the outgoing sides of id1. (Checks if there is a edge at all between the two vertices)
            if self.edges[id1]["OUT"][id2] == weight: # If there is a edge and the weight is the same then do nothing
                return False
            else:
                self.edgeSize -= 1
        # A case where there is no edge or there is a edge but the weight needs to be updated
        self.edges[id1]["OUT"][id2] = weight
        self.edges[id2]["IN"][id1] = weight
        self.nodes[id1].out_edges += 1
        self.nodes[id2].in_edges += 1
        self.modeCount += 1
        self.edgeSize += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:

        if node_id not in self.nodes: #If the vertex you want to add is not found at all
            self.nodes[node_id] = NodeData(node_id, pos) #Create a new vertex and add it to the list of vertices
            self.edges[node_id] = {"IN": {}, "OUT": {}} # Adding the outgoing and incoming edges of the vertex we added
            self.modeCount += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes:
            return False

        for node in self.edges[node_id]["IN"]: # Update of the incoming neighbors of the vertex it deletes that it is deleted
            del self.edges[node]["OUT"][node_id]# Erasing the edge between the deleted vertex and its neighbors
            self.nodes[node].out_edges -= 1
            self.edgeSize -= 1

        for node in self.edges[node_id]["OUT"]: # Update of the outgoing neighbors of the vertex it deletes that it has been deleted
            del self.edges[node]["IN"][node_id] # Erasing the rib between the deleted vertex and its neighbors
            self.nodes[node].in_edges -= 1
            self.edgeSize -= 1

        self.modeCount += 1
        # Deleting the vertex itself
        del self.nodes[node_id]
        del self.edges[node_id]
        return True



    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self.nodes or node_id2 not in self.nodes:
            print(" one of the nodes not in the graph")
            return False

        if node_id1 not in self.edges[node_id2]["IN"]:
            print(" there is no edge between nodes")
            return False
        # Erasing the edge from both whoever is an incoming rib and whoever is an outgoing rib
        del self.edges[node_id1]["OUT"][node_id2]
        del self.edges[node_id2]["IN"][node_id1]
        self.nodes[node_id1].out_edges -= 1
        self.nodes[node_id2].in_edges -= 1

        self.modeCount += 1
        self.edgeSize -= 1
        return True



    def __repr__(self) -> str:
        return "Graph: |V|=" + str(self.v_size()) + " , |E|=" + str(self.e_size())

    def __eq__(self, o: object) -> bool:
        if o == None or type(self).__name__ != type(o).__name__:
            return False
        if self.edgeSize != o.edgeSize:
            return False
        if self.modeCount != o.modeCount:
            return False
        if self.nodes != o.nodes:
            return False
        return self.edges == o.edges


