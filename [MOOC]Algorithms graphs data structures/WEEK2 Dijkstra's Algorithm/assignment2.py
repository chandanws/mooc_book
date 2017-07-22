from priorityqueue import PriorityQueue
from graph import Graph, Vertex
import sys
import unittest
import cProfile

def dijkstra(aGraph, start):
	"""
	Find Single-Source shortest-paths on a weighted, directed graph
	Return shortest path
	aGraph: class Graph
	start: class Vertex
	"""
	pq = PriorityQueue()
	start.setDistance(0)
	pq.buildHeap([(v.getDistance(), v) for v in aGraph])
	while not pq.isEmpty():
		u = pq.delMin()
		for adjacent in u.getConnections():
			newDist = u.dist + u.getWeight(adjacent)
			if adjacent.dist > newDist:
				adjacent.setDistance(newDist)
				adjacent.setPred(u)
				pq.decreaseKey(adjacent, newDist)


class TestDijkstra(unittest.TestCase):


	def testShortest(self):

		aGraph = Graph()
		with open('dijkstraData.txt') as infile:
			for line in infile:
				numbers = [number for number in line.split()]
				from_v = int(numbers[0])

				for to_v_cost in numbers[1:]:
					to_v, cost = to_v_cost.split(',')
					aGraph.addEdge(from_v, int(to_v), int(cost))

		dijkstra(aGraph, aGraph.getVertex(1))

		dists = []
		for vertex_id in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]:
			dist = aGraph.getVertex(vertex_id).getDistance()
			if dist == sys.maxsize:
				dist = 100000
			dists.append(dist)
		assert dists == [2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068]


if __name__ == '__main__':
	cProfile.run(unittest.main())
