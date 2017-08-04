import sys
sys.path.append('/users/larry/Algorithm/')
from graph import Graph
from disjoint_set import DisjointSet
import unittest


def kruskal_mst(agraph):
	"""
	Return a minimum spanning tree using kruskal's algorithm
	"""
	# minimum spanning tree
	mst = []

	# disjoint set
	disjoint_set = DisjointSet()

	# make set
	for vertex in agraph.Vertices():
		disjoint_set.make_set(vertex)

	# edges of the graph
	edges = agraph.edges()
	edges.sort(key=lambda tup: tup[2])

	for u, v, cost in edges:
		if disjoint_set.find_set(u) != disjoint_set.find_set(v):
			mst.append((u, v, cost))
			disjoint_set.union(u, v)
	return mst


class TestKruskalMST(unittest.TestCase):

	def test_small(self):
		agraph = Graph()
		count = 0
		with open('testcase1_kruskal.txt') as infile:
			for line in infile:
				if count == 0:
					pass
				else:
					from_v, to_u, cost = [int(number) for number in line.split()]
					agraph.addEdge(from_v, to_u, cost)
					agraph.addEdge(to_u, from_v, cost)
				count += 1
		mst = kruskal_mst(agraph)
		total_cost = 0
		for u, v, cost in mst:
			total_cost += cost
		self.assertEqual(total_cost, 14)

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
		mst = kruskal_mst(agraph)
		total_cost = 0
		for u, v, cost in mst:
			total_cost += cost
		self.assertEqual(total_cost, -3612829)


if __name__ == "__main__":
	unittest.main()