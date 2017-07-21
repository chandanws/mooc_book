from priorityqueue import PriorityQueue
from graph import Graph, Vertex


def dijkstra(aGraph, start):
	"""
	Find Single-Source shortest-paths on a weighted, directed graph
	Return shortest path
	agraph: class Graph
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




