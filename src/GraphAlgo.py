import math
import random
from typing import List
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
import json
import matplotlib.pyplot as plt

from src.GraphInterface import GraphInterface
from src.NodeData import NodeData
from src.PriorityQueue import PriorityQueue


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=None):
        self.graph = graph
        self.time = 0

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name) as f:  # with= automatic file closing factor
                temp = json.load(f)

            graph = DiGraph()
            for node in temp["Nodes"]:
                try:
                    pos = tuple(float(x) for x in node["pos"].split(","))
                except:
                    pos = None
                graph.add_node(node["id"], pos)

            for edge in temp["Edges"]:
                graph.add_edge(edge["src"], edge["dest"], edge["w"])

            self.graph = graph
            return True

        except Exception as ex:
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            nodes = []
            edges = []
            for node in self.graph.get_all_v().values():
                pos = [str(node.pos[0]), str(node.pos[1]), str(node.pos[2])] if node.pos is not None else (
                    "0", "0", "0")
                nodes.append({"pos": ",".join(pos), "id": node.key})
                for dest, weight in self.graph.all_out_edges_of_node(node.key).items():
                    edges.append({"src": node.key, "w": weight, "dest": dest})

            with open(file_name, "w+") as file:
                json.dump({"Nodes": nodes, "Edges": edges}, file)
            return True

        except Exception as e:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.graph.v_size() == 0:
            return float('inf'), []

        if id1 not in self.graph.nodes or id2 not in self.graph.nodes:
            return float('inf'), []

        for node in self.graph.get_all_v().values():  # A loop that starts up
            node.weight = math.inf
            node.pred = -math.inf
            node.visited = False

        s = self.graph.nodes[id1]  # Holding the start node
        s.weight = 0  # The node from which we begin
        queue = PriorityQueue()
        for node in self.graph.nodes.values():  # Run on the nodes of the graph
            queue.push(
                node)  # Add to the priority queue all the vertices of the graph, when the distance of all of them is equal to infinity except the first vertex is zero

        while not queue.empty():
            u: NodeData = queue.pop()  # Pull out the node with the minimum value

            for key, weight in self.graph.all_out_edges_of_node(
                    u.key).items():  # Go through all the neighbors of u which is the node that removed
                nei: NodeData = self.graph.nodes[key]
                if not nei.visited:  # As long as we have not visited this node already
                    t = u.weight + weight  # holds the distance -Calculate the distance to the node where you are
                    if nei.weight > t:  # Checks whether to update the distance of the neighbors of the current vertex that is smaller
                        nei.weight = t
                        nei.pred = u.key  # Update where I got to the node

            u.visited = True

        sum_weight = self.graph.nodes[id2].weight
        if sum_weight == math.inf:  # f there is no track at all then the graph is not a link and I want to access something I can not
            return float('inf'), []

        path = []  # Start a new list
        path.append(id2)
        while id1 != id2:  # Go from the end to the beginning and add each time
            id2 = self.graph.nodes[id2].pred
            path.append(id2)

        if len(path) == 0:
            return float('inf'), []

        return sum_weight, path[::-1]  # Returns the length of the distance and the shortest path

    def connected_component(self, id1: int) -> list:
        def DFS(key):
            stack = [key]  # Create a stack for DFS

            while len(stack) != 0:
                key = stack.pop()  # Remove the first one from the stack

                if not visited1[key]:  # If not visit it
                    visited1[key] = True  # Mark the vertex we start with true, we visited it

                for v in self.graph.all_out_edges_of_node(
                        key):  # Go through all the outgoing edges of the current vertex
                    if not visited1[v]:  # If the neighbor of the current vertex has not visited it, then put it in the stack
                        stack.append(v)

        def reverseDFS(key):
            stack = [key]  # Create a stack for DFS

            while len(stack) != 0:
                key = stack.pop()  # Remove the first one from the stack

                if not visited2[key]:  # If not visit it
                    visited2[key] = True  # Mark the vertex we start with true, we visited it

                for v in self.graph.all_in_edges_of_node(key):  # Go through all the ingoing edges of the current vertex
                    if not visited2[v]:  # If the neighbor of the current vertex has not visited it, then put it in the stack
                        stack.append(v)
        # initialization the dictionaries to false
        visited1 = {}
        visited2 = {}
        for node in self.graph.nodes:
            visited1[node] = False
            visited2[node] = False

        DFS(id1)
        reverseDFS(id1)

        component = []  # A list that contains one component
        for node in visited1:
            if visited1[node] and visited2[node]:  # If in both they are TRUE
                component.append(node)
        return component

    def connected_components(self) -> List[list]:
        nodes = list(self.graph.nodes.keys())
        components = []
        while len(nodes) != 0: #As long as there are vertices in the list of vertices
            node = nodes[0] #Take the vertex in the first place

            #See to some vertices the current vertex is linked that they do not belong to a connected_components
            out_edges = 0
            for nei in self.graph.all_out_edges_of_node(node): #Going through the outgoing neighbors of the vertex
                if nei in nodes:
                    out_edges += 1
            in_edges = 0
            for nei in self.graph.all_in_edges_of_node(node): #Passing on the incoming neighbors of the vertex
                if nei in nodes:
                    in_edges += 1

            if in_edges == 0 or out_edges == 0: #If the vertex has only one inward side or one outward side
                components.append([node]) #Add the vertex directly to the list of components
                nodes.remove(node)   #Delete the current vertex from the list of vertices
            else:
                component = self.connected_component(node)
                for n in component: # Goes over the vertices that are in the only binding component we got from the function
                    nodes.remove(n)
                components.append(component)
        return components

    def plot_graph(self) -> None:
        fig, ax = plt.subplots()
        plt.title('Graph')
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')

        positions = {}
        max_pos = 0
        for node in self.graph.nodes:
            pos = self.graph.nodes[node].pos  # Takes all the locations of the vertices
            if pos is not None:  # A case where the vertices have a location
                positions[node] = [pos[0], pos[1]]
                max_pos = max(max_pos, pos[0], pos[1])
            else:  # A case where the vertices have no position
                positions[node] = None

        if max_pos == 0:
            max_pos = self.graph.v_size()

        for node in positions:
            if positions[node] is None:  # A case where the vertices have no position
                positions[node] = [random.uniform(0, max_pos),
                                   random.uniform(0, max_pos)]  # Gives them a random position at the maximum we set
            ax.text(positions[node][0] + 0.0001, positions[node][1] + 0.0001, str(node), size=11,
                    color="green")  # Gives a name to the vertices

        ax.plot(*zip(*positions.values()), marker='o', color='pink', ls='')  # Draws the vertices on the graph

        for node1 in self.graph.nodes:  # Draw the edges on the graph
            for node2 in self.graph.all_out_edges_of_node(node1):
                pos1 = positions[node1]
                pos2 = positions[node2]
                xyA = (pos1[0], pos1[1])
                xyB = (pos2[0], pos2[1])
                coordsA = "data"
                coordsB = "data"
                from matplotlib.patches import ConnectionPatch
                con = ConnectionPatch(xyA, xyB, coordsA, coordsB,
                                      arrowstyle="-|>", shrinkA=0, shrinkB=0,
                                      mutation_scale=20, fc="black")
                ax.add_artist(con)
        plt.show()
