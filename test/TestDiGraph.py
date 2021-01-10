import unittest
import time

from src.DiGraph import DiGraph


class MyTestCase(unittest.TestCase):
    def test_add_node(self):
        graph = DiGraph()
        for i in range(4):
            graph.add_node(i)
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 0, 3)
        graph.add_edge(3, 0, 7)
        self.assertEqual(4, graph.v_size())
        self.assertEqual(8, graph.get_mc())
        graph.add_edge(3, 0, 5)
        self.assertEqual(9, graph.get_mc())
        graph.add_edge(3, 0, 5)
        self.assertEqual(9, graph.get_mc())
        self.assertEqual(4, graph.e_size())
        graph.remove_node(0)
        self.assertEqual(3, graph.v_size())
        self.assertEqual(1, graph.e_size())
        self.assertTrue(graph.remove_edge(1, 2))
        self.assertEqual(0, graph.e_size())
        self.assertEqual(3, graph.v_size())
        self.assertFalse(graph.remove_edge(8, 9))

    def test_add_node1(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_node(5)
        graph.add_edge(1, 2, 3)
        graph.add_edge(2, 3, 4)
        graph.add_edge(3, 4, 10)
        graph.add_edge(4, 3, 1)
        graph.add_edge(3, 5, 7)
        graph.add_edge(5, 1, 1)
        graph.add_edge(1, 5, 2)

        self.assertEqual(12, graph.get_mc())
        self.assertEqual(5, graph.v_size())
        self.assertEqual(7, graph.e_size())

        keys = [1, 2, 3, 4, 5]
        self.assertEqual(keys, list(graph.get_all_v().keys()))
        self.assertEqual({2: 4, 4: 1}, graph.all_in_edges_of_node(3))
        self.assertEqual({4: 10, 5: 7}, graph.all_out_edges_of_node(3))

        graph.remove_edge(5, 1)
        self.assertEqual(6, graph.e_size())
        self.assertEqual(0, len(graph.all_out_edges_of_node(5)))
        self.assertEqual(13, graph.get_mc())

        graph.remove_node(3)
        self.assertEqual(4, graph.v_size())
        self.assertEqual(2, graph.e_size())

        self.assertEqual(0, len(graph.all_out_edges_of_node(4)))
        self.assertEqual(14, graph.get_mc())

    def test_add_node2(self):
        graph = DiGraph()
        for i in range(100):
            graph.add_node(i)
        graph.add_node(50)
        self.assertEqual(100, graph.v_size())
        self.assertTrue(graph.remove_node(6))
        self.assertEqual(99,graph.v_size())
        self.assertFalse( graph.remove_node(101))

    def test_empty_graph(self):
        graph = DiGraph()
        self.assertEqual(0, graph.v_size())
        self.assertFalse(graph.remove_edge(2, 5))
        self.assertFalse(graph.remove_node(2))

    def test_add_edge(self):
        graph = DiGraph()
        for i in range(1, 11):
            graph.add_node(i)
        graph.add_edge(1, 2, 5)
        graph.add_edge(1, 8, 4)
        graph.add_edge(9, 10, 0)
        graph.add_edge(5, 2, 3)

        self.assertEqual(4, graph.e_size())
        self.assertFalse(graph.add_edge(1, 100, 4))
        self.assertEqual(2, len(graph.all_out_edges_of_node(1)))
        self.assertEqual(0, len(graph.all_out_edges_of_node(4)))
        graph.remove_edge(1, 8)
        self.assertEqual(3, graph.e_size())
        self.assertEqual(1, len(graph.all_out_edges_of_node(1)))
        graph.remove_node(9)
        self.assertEqual(2, graph.e_size())
        self.assertEqual(0, len(graph.all_out_edges_of_node(10)))
        self.assertFalse(graph.add_edge(1, 2, -9))
        self.assertFalse(graph.add_edge(1, 4, -9))
        self.assertEqual(2, graph.e_size())# If the weight is negative then the number of ribs does not change.
        self.assertEqual(16, graph.get_mc())

    def test_edges_Empty_Graph(self):
        graph = DiGraph()
        self.assertFalse(graph.remove_edge(1,5))
        self.assertEqual(0, graph.v_size())
        self.assertEqual(0, graph.e_size())
        self.assertEqual(0, graph.get_mc())

    def test_edges_number_On_Full_Graph(self):
        graph = DiGraph()
        for i in range(1, 6):
            graph.add_node(i)

        for i in range(1, 6):
            for j in range(1, 6):
                result = graph.add_edge(i, j, 5)
                if i == j:
                    self.assertFalse(result)
                else:
                    self.assertTrue(result)
        graph.remove_edge(1, 5)
        self.assertEqual(19, graph.e_size())
        self.assertEqual(26, graph.get_mc())



if __name__ == '__main__':
    unittest.main()
