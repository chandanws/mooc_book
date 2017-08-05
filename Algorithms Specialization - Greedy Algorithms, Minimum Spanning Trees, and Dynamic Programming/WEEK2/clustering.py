import sys
sys.path.append('/Users/larry/Algorithm')
from graph import Graph
from disjoint_set import DisjointSet
import unittest


def clustering(agraph, k):
	"""
	Max-Spacing k clustering

	Return maximum spacing of a k-clustering
	and corresponding mst.
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
		if len(disjoint_set) >= k:

			if disjoint_set.find_set(u) != disjoint_set.find_set(v):
				mst.append((u, v, cost))
				max_cost = cost
				disjoint_set.union(u, v)
		else:
			break


	return max_cost, mst


class TestClustering(unittest.TestCase):

	def testbig(self):
		count = 0
		agraph = Graph()
		with open('clustering.txt') as infile:
			for line in infile.readlines():
				line = line.strip('\n')
				if count == 0:
					pass
				else:
					u, v, cost = [int(num) for num in line.split()]
					agraph.addEdge(u, v, cost)
				count += 1
		cost, mst = clustering(agraph, 4)
		self.assertEqual(cost, 106)

	def test_large2(self):
		count = 0
		agraph = Graph()
		with open('input_completeRandom_29_1024.txt') as infile:
			for line in infile.readlines():
				line = line.strip('\n')
				if count == 0:
					pass
				else:
					u, v, cost = [int(num) for num in line.split()]
					agraph.addEdge(u, v, cost)
				count += 1
		cost, mst = clustering(agraph, 4)
		with open('output_completeRandom_29_1024.txt') as infile:
			for line in infile.readlines():
				line = line.strip('\n')
				result = int(line)

	def test_large1(self):
		count = 0
		agraph = Graph()
		with open('input_completeRandom_10_32.txt') as infile:
			for line in infile.readlines():
				line = line.strip('\n')
				if count == 0:
					pass
				else:
					u, v, cost = [int(num) for num in line.split()]
					agraph.addEdge(u, v, cost)
				count += 1
		cost, mst = clustering(agraph, 4)
		with open('output_completeRandom_10_32.txt') as infile:
			for line in infile.readlines():
				line = line.strip('\n')
				result = int(line)

		self.assertEqual(cost, result)

	def test_medium(self):
		count = 0
		agraph = Graph()
		with open('testcase2_for_clustering.txt') as infile:
			for line in infile.readlines():
				line = line.strip('\n')
				if count == 0:
					pass
				else:
					u, v, cost = [int(num) for num in line.split()]
					agraph.addEdge(u, v, cost)
				count += 1
		cost, mst = clustering(agraph, 4)
		self.assertEqual(cost, 7)

	def test_small(self):
		count = 0
		agraph = Graph()
		with open('testcase1_for_clustering.txt') as infile:
			for line in infile.readlines():
				line = line.strip('\n')
				if count == 0:
					pass
				else:
					u, v, cost = [int(num) for num in line.split()]
					agraph.addEdge(u, v, cost)
				count += 1
		cost, mst = clustering(agraph, 1)
		self.assertEqual(cost, 1)




if __name__ == '__main__':
	unittest.main()


