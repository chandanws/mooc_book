#!/usr/bin/python
"""
This program uses Breadth-first search to ....
"""

#general input
from collections import deque
import urllib2


def bfs_visited(ugraph, start_node):
    """
    Function takes the undirected graph ugraph and the node start_node.
    Returns the set consisting of all nodes that are visited by a
    breadth-first search that starts at start_node.
    """
    queue = deque([])
    visited = set([start_node])
    queue.append(start_node)
    while len(queue) != 0:
        node = queue.popleft()
        neighbors = ugraph[node]
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

def cc_visited(ugraph):
    """
    Function takes the undirected graph ugraph
    Returns a list of sets where each set consists
    of all the nodes in a connected component
    """
    nodes = ugraph.keys()
    remaining_nodes = nodes
    connected_nodes = []
    while len(remaining_nodes) is not 0:
        arbitrary_node = remaining_nodes[0]
        visited = bfs_visited(ugraph, arbitrary_node)
        connected_nodes.append(visited)
        for node in visited:
            remaining_nodes.remove(node)
    return connected_nodes

def largest_cc_size(ugraph):
    """
    Function takes the undirected graph ugraph.
    Returns the size of the largest connected component in ugraph.
    """
    connected_nodes = cc_visited(ugraph)
    largest_size = 0
    for component in connected_nodes:
        if largest_size < len(component):
            largest_size = len(component)
    return largest_size

def compute_resilience(ugraph, attack_order):
    """
    Function removes the given node and its edges from ugraph.
    Returns a list whose k + 1th entry is the size of the largest
    connected component for the components resulting graph after
    kth remove. The first entry is the size of the largest connected
    components of orignal graph.
    """
    cc_size_initial = largest_cc_size(ugraph)
    cc_size = [cc_size_initial]
    for attack in attack_order:
        del ugraph[attack]
        for node in ugraph:
            neighbors = ugraph[node]
            if attack in neighbors:
                ugraph[node].remove(attack)
        cc_size.append(largest_cc_size(ugraph))
    return cc_size

def load_graph(graph_url):
    """
    Function loads a graph from graph_url
    Returns a dictonary that contains the graph.
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]

    graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            graph[node].add(int(neighbor))
    print "graph=",graph
    return graph

if __name__ == '__main__':
    NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"
    GRAPH = load_graph(NETWORK_URL)
    ATTACK_ORDER = [1,5,7]
    print compute_resilience(GRAPH, ATTACK_ORDER)
