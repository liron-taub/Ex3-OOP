import json
import unittest
from datetime import datetime
import networkx as nx

from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):

    def test_time(self):
        path = "../data/G_100_800_0.json"  # change the path to the desired json file
        with open(path) as f:  # with= automatic file closing factor
            temp = json.load(f)
        graph = nx.DiGraph()
        for node in temp["Nodes"]:
            graph.add_node(node["id"])
        for edge in temp["Edges"]:
            graph.add_edge(edge["src"], edge["dest"], weight=edge["w"])

        start = datetime.now()
        nx.shortest_path(graph, 1, 10)
        finish = datetime.now()
        dif = finish - start
        print("python shortest_path:", dif)

        start = datetime.now()
        nx.strongly_connected_components(graph)
        finish = datetime.now()
        dif = finish - start
        print("python connected_components:", dif)

        algo = GraphAlgo()
        self.assertTrue(algo.load_from_json(path))

        start = datetime.now()
        algo.shortest_path(1, 10)
        finish = datetime.now()
        dif = finish - start
        print("python shortest_path:", dif)

        start = datetime.now()
        algo.connected_components()
        finish = datetime.now()
        dif = finish - start
        print("python connected_components:", dif)

        start = datetime.now()
        algo.connected_component(9)
        finish = datetime.now()
        dif = finish - start
        print("python connected_component:", dif)


if __name__ == '__main__':
    unittest.main()
