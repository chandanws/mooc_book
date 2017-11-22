from priorityqueue import PriorityQueue
import sys
from graph import Graph, Vertex


def dijkstra(agraph, start):
	"""
	Find Single-Source shortest-paths on a weighted, directed graph
	Return shortest path
	agraph: class Graph
	start: class Vertex
	"""
	pq = PriorityQueue()
	for v in agraph:
		v.setDistance(sys.maxsize)
		v.setPred(None)
	start.setDistance(0)
	pq.buildHeap([(v.getDistance(), v) for v in agraph])
	while not pq.isEmpty():
		u = pq.delMin()
		for adjacent in u.getConnections():
			newDist = u.dist + u.getWeight(adjacent)
			if adjacent.dist > newDist:
				adjacent.setDistance(newDist)
				adjacent.setPred(u)
				pq.decreaseKey(adjacent, newDist)




