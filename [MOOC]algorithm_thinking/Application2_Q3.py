#!/usr/bin/python
"""
This programs complete the application 2 question 1
"""
import time
import random
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
    for attack_node in attack_order:
        neighbors = ugraph[attack_node]
        ugraph.pop(attack_node)
        for neighbor in neighbors:
            ugraph[neighbor].remove(attack_node)
        cc_size.append(largest_cc_size(ugraph))
    return cc_size

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

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

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

def targeted_order(ugraph):
    """
    Function calculate a list of nodes who have maximnum degree sequently.
    Returns a list whose forward elements have larger degrees than behaind
    element.
    """
   # copy the graph
    new_graph = copy_graph(ugraph)

    order = []
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node

        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order

def fast_targeted_order(ugraph):
    """
    Function calculate a list of nodes who have maximnum degree sequently.
    Returns a list whose forward elements have larger degrees than behaind
    element.
    """
    nodes = ugraph.viewkeys()
    degree_sets = [set([]) for node in nodes]
    for node in nodes:
        degree = len(ugraph[node])
        degree_sets[degree].add(node)

    ordered_list = []
    for degree in xrange(len(nodes)-1, -1, -1):
        num_of_degree = degree_sets[degree]
        while num_of_degree != set([]):
            node = degree_sets[degree].pop()
            neighbors = ugraph[node]
            for neighbor in neighbors:
                degree_of_neighbor = len(ugraph[neighbor])
                degree_sets[degree_of_neighbor].remove(neighbor)
                degree_sets[degree_of_neighbor - 1].add(neighbor)
                ugraph[neighbor].remove(node)
            ordered_list.append(node)
            ugraph.pop(node)
    return ordered_list


if __name__ == "__main__":
    NUM_NODES = range(10, 1000, 10)
    START_NUM = 5

    TIME_TARGET = []
    TIME_FAST = []

    for NUM_NODE in NUM_NODES:
        UPAGRAPH = upa_ugraph(NUM_NODE, START_NUM)
        start_time = time.time()
        UPA_ATTACK_ORDER = targeted_order(UPAGRAPH)
        TIME_TARGET.append(time.time() - start_time)

        start_time = time.time()
        UPA_ATTACK_ORDER = fast_targeted_order(UPAGRAPH)
        TIME_FAST.append(time.time() - start_time)

    plt.figure()
    plt.hold(True)
    plt.plot(NUM_NODES, TIME_TARGET, label='TIME_TARGET')
    plt.plot(NUM_NODES, TIME_FAST, label='TIME_FAST')
    plt.xlabel('Number of nodes')
    plt.ylabel('Runing time(second)')
    plt.legend(loc='upper right')
    plt.title('Using Desktop Python')
    plt.show()

