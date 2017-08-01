#!/usr/bin/python
"""
This file use dpa graph to calcute the degrees distribution.
"""

# general imports
import random
import matplotlib.pylab as plt

class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm

    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities

    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a
        complete graph with num_nodes nodes

        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) \
            for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers

        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities

        Returns:
        Set of nodes
        """

        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))

        # update the list of node numbers so that each node number
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))

        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors




def dpa_graph(num_nodes, start_num):
    """
    Function creates dpa graph.
    Returns: A Dictionary.
    """
    nodes = range(start_num)
    graph = make_complete_graph(start_num)

    trail = DPATrial(start_num)
    for node in xrange(start_num, num_nodes):
        neighbors = trail.run_trial(start_num)
        graph[node]= neighbors

    return graph



def calculate_indegree(digraph):
    """
    Function calcultes the in degree of graph provided.
    Returns a integer number.
    """
    neighbors = digraph.values()
    in_degree = 0
    for neighbor in neighbors:
        in_degree = sum(neighbor) + in_degree

    return in_degree

def make_graph_use_nodes(nodes, initial=0):
    """
    Function use nodes provided to create a new graph.
    Return a dictory whose keys are nodes, values are initial.
    """
    digraph = {}
    for node in nodes:
        digraph[node] = initial
    return digraph

def make_complete_graph(num_nodes):
    """
    Function creates a new complete graph whose number of nodes
    are num_nodes provided
    """
    nodes = range(num_nodes)
    graph = {}
    for node in nodes:
        neighbor = set([item for item in nodes])
        neighbor.remove(node)
        graph[node] = neighbor
    return graph

def compute_in_degrees(digraph):
    """
    Function takes a directed graph digraph (represented as a dictionary)
    and computes the in-degrees for the nodes in the graph.
    Returns a dictory whose keys are nodes and valuse are degrees.
    """
    nodes = digraph.keys()
    degree_digraph = make_graph_use_nodes(nodes)
    for node in nodes:
        neighbors = digraph[node]
        for neighbor in neighbors:
            degree_digraph[neighbor] = degree_digraph[neighbor] + 1
    return degree_digraph

def in_degree_distribution(digraph):
    """
    Function takes a directed graph digraph (represented as a dictionary)
    and computes the unnormalized distribution of the in-degrees
    of the graph.

    Returns a dictory whose keys are degrees and valuses
    are normalized numbers of degrees.
    """

    nodes = digraph.keys()
    degree_distribution = {}
    degree_digraph = compute_in_degrees(digraph)

    max_degree = 0
    for node in nodes:
        degree = degree_digraph[node]
        if degree_distribution.get(degree) != None:
            degree_distribution[degree] = degree_distribution[degree] + 1
        else:
            degree_distribution[degree] = 1
        if degree > max_degree:
            max_degree = degree
    #normailze
    degrees = degree_distribution.keys()
    total_number_of_degree = sum(degree_distribution.values())
    for degree in degrees:
        degree_distribution[degree] = float(degree_distribution[degree]) \
                /float(total_number_of_degree)

    return degree_distribution

def plot_degree_distribution_use_log(degree_distribution):
    """
    Function plots the degree distribution use matplotlib.pylab
    """
    degrees = degree_distribution.keys()
    number_of_degrees = degree_distribution.values()

    plt.loglog(degrees, number_of_degrees, 'r', marker='.', linestyle='None')
    plt.title("In degree distibution of dpa GRAPH")
    plt.xlabel('In degree')
    plt.ylabel('Distribution')
    plt.show()
    

if __name__ == "__main__":
    GRAPH = dpa_graph(27770, 12)
    IN_DEGREE_DISTRIBUTION = in_degree_distribution(GRAPH)
    plot_degree_distribution_use_log(IN_DEGREE_DISTRIBUTION)
    ()