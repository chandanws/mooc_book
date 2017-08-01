#!/usr/bin/python
"""
This programs complete the application 2
"""
import urllib2
import random
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

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

def er_ugraph(num_nodes, probability):
    """
    Function uses num_nodes to creat a undirected ER graph according
    to the probability.
    Returns a dictionary whose keys are nodes and values are neighbors.
    """
    nodes = range(num_nodes)
    ugraph = {}
    for node in nodes:
        ugraph[node] = set([])
    for node1 in nodes:
        for node2 in nodes:
            if node1 is not node2:
                dummy_random = random.random()
                if dummy_random < probability:
                    ugraph[node1].add(node2)
                    ugraph[node2].add(node1)
    return ugraph


def load_ugraph(url):
    """
    Function opens provided url and read text to creat a graph.
    Returns a dictionary whose keys are nodes and values are neighbors.
    """
    graph_text = urllib2.urlopen(url)
    graph_lines = graph_text.read()
    graph_lines = graph_lines.split('\n')
    lines = graph_lines[ : -1]

    ugraph = {}
    for line in lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        ugraph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            ugraph[node].add(int(neighbor))
    return ugraph

class UPATrial:
    """
    Simple class to encapsulate optimizated trials for the UPA algorithm

    Maintains a list of node numbers with multiple instance of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities

    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a UPATrial object corresponding to a
        complete graph with num_nodes nodes

        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) \
                for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers

        Updates the list of node numbers so that each node number
        appears in correct ratio

        Returns:
        Set of nodes
        """

        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))

        # update the list of node numbers so that each node number
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))

        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors


def upa_ugraph(num_nodes, start_num):
    """
    Function creates UPA ugraph.
    Returns: A Dictionary whose keys are nodes and values are neighbors.
    """
    ugraph = make_complete_ugraph(start_num)
    trail = UPATrial(start_num)
    for node in xrange(start_num, num_nodes):
        ugraph[node] = set([])
    for node in xrange(start_num, num_nodes):
        neighbors = trail.run_trial(start_num)
        ugraph[node] = neighbors
        for neighbor in neighbors:
            ugraph[neighbor].add(node)
    return ugraph

def make_complete_ugraph(num_nodes):
    """
    Function creates an undirected complete graph.
    Returns a dictionary whose keys are nodes and values are neighbors.
    """
    ugraph = {}
    nodes = range(num_nodes)
    for node in nodes:
        ugraph[node] = set([neighbor for neighbor in nodes \
                if node is not neighbor])
    return ugraph

def num_of_nodes_and_edges(ugraph):
    """
    Function calcutes the number of nodes and edges according to
    the giving undirect graph.
    Returns a tuple contains number of nodes and number of edges.
    """
    nodes = ugraph.keys()
    neighbors = ugraph.values()
    num_edges = 0
    for neighbor in neighbors:
        num_edges = num_edges + len(neighbor)/2
    num_nodes = len(nodes)
    return (num_nodes, num_edges)

def random_order(ugraph):
    """
    Function returns a radom order from 0 to len(node).
    """
    nodes = ugraph.keys()
    order = random.sample(nodes, int(len(nodes)*0.25))
    return order

if __name__ == "__main__":
    NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"
    NETGRAPH = load_ugraph(NETWORK_URL)
    (NUM_NODES, NUM_EDGES) = num_of_nodes_and_edges(NETGRAPH)
    PROBABILITY = round(float(NUM_EDGES)/(np.power(float(NUM_NODES-1), 2)), 12)
    ERGRAPH = er_ugraph(NUM_NODES, PROBABILITY)
    UPAGRAPH = upa_ugraph(NUM_NODES, 2)

    NET_ATTACK = random_order(NETGRAPH)
    ER_ATTACK = random_order(ERGRAPH)
    UPA_ATTACK = random_order(UPAGRAPH)

    NET_RESI = compute_resilience(NETGRAPH, NET_ATTACK)
    ER_RESI = compute_resilience(ERGRAPH, ER_ATTACK)
    UPA_RESI = compute_resilience(UPAGRAPH, UPA_ATTACK)

    plt.figure()
    plt.hold(True)
    plt.plot(NET_RESI, 'b', label='NETWORK')
    plt.plot(ER_RESI, 'r', label='ER P=1.43952E-3')
    plt.plot(UPA_RESI, 'y', label='UPA M=2')
    dummy_x = np.arange(NUM_NODES)
    dummy_y = NUM_NODES - dummy_x
    plt.plot(dummy_x, dummy_y)
    plt.legend(loc='upper right')
    plt.xlabel("Attack Number")
    plt.ylabel("Resilience")
    plt.show()
