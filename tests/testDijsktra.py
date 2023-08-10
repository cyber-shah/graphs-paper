import unittest

import algorithms.Dijkstra as Dijkstra
from model import GraphMakers


class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        string_vertices = "a\nb\nc\nd"
        string_distances = "a b 2\nb c 1\na c 4\nc d 2\na d 8"

        graph = GraphMakers.graph_from_string(string_vertices, string_distances)
        shortest_path_list = Dijkstra.dijkstra(graph, 'a')

        self.assertEqual(0, shortest_path_list[0])
        self.assertEqual(2, shortest_path_list[1])
        self.assertEqual(3, shortest_path_list[2])
        self.assertEqual(5, shortest_path_list[3])


if __name__ == '__main__':
    unittest.main()
