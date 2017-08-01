from priorityqueue import PriorityQueue
from graph import Graph
import unittest
import sys


def prim(agraph, start):
    """
    Prim's algorithm for minimum spanning tree
    Using min-heap data structure

    return the overall cost of a minimum spanning tre
    """
    pq = PriorityQueue()
    total_cost = 0
    for v in agraph:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in agraph])
    while not pq.isEmpty():
        cost, u = pq.delMin()
        total_cost += cost
        for adjacent in u.getConnections():
          newcost = u.getWeight(adjacent)
          if adjacent in pq and newcost < adjacent.getDistance():
              adjacent.setPred(u)
              adjacent.setDistance(newcost)
              pq.decreaseKey(adjacent, newcost)

    return total_cost


class TestPrim(unittest.TestCase):

    def setUp(self):
        pass

    def test_big(self):
        agraph = Graph()
        count = 0
        with open('edges.txt') as infile:
            for line in infile:
                if count == 0:
                    pass
                else:
                    from_v, to_u, cost = [int(number) for number in line.split()]
                    agraph.addEdge(from_v, to_u, cost)
                    agraph.addEdge(to_u, from_v, cost)
                count += 1

        self.assertEqual(prim(agraph, agraph.getVertex(1)), -3612829)

    def test_small(self):
        agraph = Graph()
        count = 0
        with open('testcase1_prim.txt') as infile:
            for line in infile:
                if count == 0:
                    pass
                else:
                    from_v, to_u, cost = [int(number) for number in line.split()]
                    agraph.addEdge(from_v, to_u, cost)
                    agraph.addEdge(to_u, from_v, cost)
                count += 1

        self.assertEqual(prim(agraph, agraph.getVertex(1)), 14)


if __name__ == "__main__":
    unittest.main()













