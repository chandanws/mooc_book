import sys
sys.path.append('/users/larry/Algorithm')
from priorityqueue import PriorityQueue
from graph import Graph
import unittest
import sys


def prim(agraph, start):
    """
    Prim's algorithm for minimum spanning tree
    Using min-heap data structure

    return a minimum spanning tree
    """
    # vertex of minimun spanning tree
    mst_vertex = []
    pq = PriorityQueue()
    for v in agraph:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in agraph])
    while not pq.isEmpty():
        u = pq.delMin()
        mst_vertex.append(u)
        for adjacent in u.getConnections():
            newcost = u.getWeight(adjacent)
            if adjacent in pq and newcost < adjacent.getDistance():
                adjacent.setPred(u)
                adjacent.setDistance(newcost)
                pq.decreaseKey(adjacent, newcost)

    # edges of minimum spanning tree
    mst = []
    for i in range(1, len(mst_vertex)):
        # u, v, cost
        mst.append((mst_vertex[i-1], mst_vertex[i],  mst_vertex[i].getDistance()))

    return mst


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

        total_cost = 0
        mst = prim(agraph, agraph.getVertex(1))
        for u, v, cost in mst:
            total_cost += cost
        self.assertEqual(total_cost, -3612829)

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

        total_cost = 0
        mst = prim(agraph, agraph.getVertex(1))
        for u, v, cost in mst:
            total_cost += cost
        self.assertEqual(total_cost, 14)


if __name__ == "__main__":
    unittest.main()













