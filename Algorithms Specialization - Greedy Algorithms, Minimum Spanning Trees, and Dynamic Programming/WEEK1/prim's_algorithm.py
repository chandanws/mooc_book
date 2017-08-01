from priorityqueue import PriorityQueue
import sys


def prim(agraph, start):
    pq = PriorityQueue()
    for v in agraph:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in G])
    while not pq.isEmpty():
        u = pq.delMin()
        for adjacent in u.getConnections():
          newCost = u.getWeight(adjacent)
          if adjacent in pq and newCost < adjacent.getDistance():
              adjacent.setPred(u)
              adjacent.setDistance(newCost)
              pq.decreaseKey(adjacent, newCost)
