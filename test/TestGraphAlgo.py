import unittest
from datetime import datetime

import networkx as nx

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_path(self):
        graph = DiGraph()
        for i in range(1, 11):
            graph.add_node(i)
        graph.add_edge(1, 2, 5)
        graph.add_edge(1, 8, 4)
        graph.add_edge(9, 10, 0)
        graph.add_edge(5, 2, 3)
        graph.add_edge(1, 5, 7)
        graph.add_edge(2, 10, 10)
        algo = GraphAlgo()
        algo.graph = graph
        self.assertEqual((4, [1, 8]), algo.shortest_path(1, 8))
        self.assertEqual((15, [1, 2, 10]), algo.shortest_path(1, 10))
        self.assertEqual((float('inf'), []), algo.shortest_path(1, 9))
        self.assertEqual((float('inf'), []), algo.shortest_path(1, 11))
        self.assertEqual((5, [1, 2]), algo.shortest_path(1, 2))
        self.assertTrue(graph.remove_edge(1, 2))
        self.assertEqual((7, [1, 5]), algo.shortest_path(1, 5))
        self.assertEqual((10, [1, 5, 2]), algo.shortest_path(1, 2))
        self.assertEqual((20, [1, 5, 2, 10]), algo.shortest_path(1, 10))
        self.assertEqual((0, [9, 10]), algo.shortest_path(9, 10))
        self.assertTrue(graph.remove_node(2))
        self.assertFalse(graph.add_edge(5, 10, -1))
        self.assertTrue(graph.add_edge(5, 10, 1))
        self.assertEqual((8, [1, 5, 10]), algo.shortest_path(1, 10))

    def test_components(self):
        graph = DiGraph()
        for i in range(1, 5):
            graph.add_node(i)
        graph.add_edge(1, 2, 5)
        graph.add_edge(2, 3, 4)
        graph.add_edge(3, 1, 0)

        algo = GraphAlgo()
        algo.graph = graph

        self.assertEqual([[1, 2, 3], [4]], algo.connected_components())
        print(algo.connected_components())
        self.assertEqual([1, 2, 3], algo.connected_component(1))
        self.assertEqual([1, 2, 3], algo.connected_component(2))
        self.assertEqual([4], algo.connected_component(4))

        graph.add_edge(4, 3, 9)
        self.assertEqual([[1, 2, 3], [4]], algo.connected_components())
        print(algo.connected_components())

        graph.add_edge(1, 4, 19)
        self.assertEqual([[1, 2, 3, 4]], algo.connected_components())
        print(algo.connected_components())

    def test_complex_components(self):
        graph = DiGraph()
        graph2 = nx.DiGraph()

        algo = GraphAlgo()
        algo.graph = graph

        self.assertEqual([], algo.connected_components())
        print(algo.connected_components())
        print(list(nx.strongly_connected_components(graph2)))

        for i in range(1, 7):
            graph.add_node(i)
            graph2.add_node(i)

        self.assertEqual([[1], [2], [3], [4], [5], [6]], algo.connected_components())
        print(algo.connected_components())
        print(list(nx.strongly_connected_components(graph2)))

        graph.add_edge(1, 2, 1)
        graph.add_edge(2, 3, 1)
        graph.add_edge(3, 1, 1)
        graph.add_edge(5, 6, 1)
        graph.add_edge(6, 5, 1)

        graph2.add_edge(1, 2, weight=1)
        graph2.add_edge(2, 3, weight=1)
        graph2.add_edge(3, 1, weight=1)
        graph2.add_edge(5, 6, weight=1)
        graph2.add_edge(6, 5, weight=1)

        self.assertEqual([[1, 2, 3], [4], [5, 6]], algo.connected_components())
        print(algo.connected_components())
        print(list(nx.strongly_connected_components(graph2)))

        print(algo.shortest_path(1, 3))
        print([nx.shortest_path_length(graph2, 1, 3), nx.shortest_path(graph2, 1, 3)])

        graph.remove_edge(5, 6)
        graph2.remove_edge(5, 6)
        self.assertEqual([[1, 2, 3], [4], [5], [6]], algo.connected_components())
        print(algo.connected_components())
        print(list(nx.strongly_connected_components(graph2)))

        graph.add_edge(3, 4, 1)
        graph.add_edge(5, 6, 1)
        graph.add_edge(4, 5, 1)
        graph.add_edge(5, 6, 1)
        graph.add_edge(6, 1, 1)

        graph2.add_edge(3, 4, weight=1)
        graph2.add_edge(5, 6, weight=1)
        graph2.add_edge(4, 5, weight=1)
        graph2.add_edge(5, 6, weight=1)
        graph2.add_edge(6, 1, weight=1)
        self.assertEqual([[1, 2, 3, 4, 5, 6]], algo.connected_components())
        print(algo.connected_components())
        print(list(nx.strongly_connected_components(graph2)))

    def test_complex_components2(self):
        start = datetime.now()
        graph = DiGraph()

        algo = GraphAlgo()
        algo.graph = graph
        
        limit = 10**4

        for i in range(limit):
            graph.add_node(i)

        for i in range(limit):
            graph.add_edge(i, (i+1) % limit, 1)

        comp = algo.connected_components()
        self.assertEqual(1, len(comp))
        self.assertEqual(limit, len(comp[0]))

        graph.remove_edge(0, 1)
        self.assertEqual(limit, len(algo.connected_components()))
        finish = datetime.now()
        print(finish-start)


    def test_plot(self):
        graph = DiGraph()
        graph.add_node(1, (1, 2))
        graph.add_node(2, (1.5, 4))
        graph.add_node(3, (2, 2))
        graph.add_node(4, (3, 4))
        graph.add_node(5, (5, 2))
        graph.add_node(6, (6, 1))
        graph.add_edge(1, 2, 5)
        graph.add_edge(2, 3, 4)
        graph.add_edge(3, 1, 0)
        graph.add_edge(5, 6, 6)

        algo = GraphAlgo()
        algo.graph = graph

        algo.plot_graph()

        graph.add_edge(3, 2, 4)
        algo.plot_graph()

    def test_plot_ranom(self):
        graph = DiGraph()
        graph = DiGraph()
        for i in range(1, 10):
            graph.add_node(i)

        graph.add_edge(1, 4, 6)
        graph.add_edge(4, 1, 6)
        graph.add_edge(7, 4, 5)
        graph.add_edge(4, 7, 5)
        graph.add_edge(8, 7, 6)
        graph.add_edge(2, 3, 4)
        graph.add_edge(8, 4, 6)
        graph.add_edge(7, 5, 6)

        algo = GraphAlgo()
        algo.graph = graph

        algo.plot_graph()

    def test_others(self):
        graph = DiGraph()
        for i in range(1, 5):
            graph.add_node(i)
        graph.add_edge(1, 2, 5)
        graph.add_edge(2, 3, 4)
        graph.add_edge(3, 1, 0)

        algo = GraphAlgo(graph)
        self.assertEqual(graph, algo.get_graph())
        self.assertTrue(algo.save_to_json("test_save.json"))
        self.assertTrue(algo.load_from_json("test_save.json"))
        self.assertEqual(graph, algo.get_graph())

    def test_emptyGraph(self):
        graph = DiGraph()
        algo = GraphAlgo(graph)
        self.assertTrue(len(algo.connected_components()) ==0)
        self.assertEquals((float('inf'), []), algo.shortest_path(1, 4))

    def test_weightedGraphNotlinked(self): 
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_node(5)
        graph.add_node(6)
        graph.add_edge(1, 2, 5)
        graph.add_edge(2, 3, 5)
        graph.add_edge(4, 5, 5)
        graph.add_edge(2, 6, 10)
        graph.add_edge(6, 3, 30)
        graph.add_edge(3, 2, 0)
        graph.add_edge(3, 2, -1)
        graph.add_edge(1, 3, 1)

        algo = GraphAlgo(graph)
        self.assertEquals(1, algo.shortest_path(1, 3)[0])
        graph.remove_edge(1, 3)
        self.assertEquals(10, algo.shortest_path(1, 3)[0])
        self.assertEquals(5, algo.shortest_path(1, 2)[0])
        self.assertEquals((float('inf'), []), algo.shortest_path(3, 5))
        self.assertEquals(14, graph.get_mc())
        self.assertEquals(15, algo.shortest_path(1, 6)[0])
        graph.add_edge(2, 1, 10);
        self.assertEquals(30, algo.shortest_path(6, 3)[0])
        self.assertEquals(0, algo.shortest_path(3, 2)[0])
        self.assertEquals(10, algo.shortest_path(2, 1)[0])

        self.assertEquals(40, algo.shortest_path(6, 1)[0])

    def test_extremeCases(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_node(5)
        graph.add_node(6)

        graph.add_edge(1, 3, 6)
        graph.add_edge(3, 4, 10)
        graph.add_edge(4, 2, 5)
        graph.add_edge(2, 1, 10)
        graph.add_edge(2, 1, 10)
        graph.add_edge(2, 1, 10.9)


        algo = GraphAlgo(graph)


        self.assertEquals(11, graph.get_mc())
        graph.remove_node(2)
        self.assertEquals(5, graph.v_size())
        self.assertEquals(2, graph.e_size())
        self.assertFalse(graph.remove_node(2))
        self.assertEquals(16, algo.shortest_path(1, 4)[0])
        self.assertEquals((float('inf'), []), algo.shortest_path(1, 2))
        self.assertEquals(12, graph.get_mc())


if __name__ == '__main__':
    unittest.main()
