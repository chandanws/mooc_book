#!/usr/bin/python
"""
This file use dpa graph to calcute the degrees distribution.
"""

# imports
import matplotlib.pylab as plt
from random import randrange

def dpa_graph(num_nodes, start_num):
    """
    Function creats a new dpa graph
    Returns a dictionary that models a graph
    """
    graph = make_complete_graph(start_num)

    for new_node in range(start_num, num_nodes):
        choosed_node = choose_node(graph)
        graph[new_node] = choosed_node
    return graph

def choose_node(digraph):
    """
    Function choose num_choose nodes from digraph.
    Return a set that contains the choosed notes.
    """
    nodes = digraph.keys()
    choosed_node = set([])
    total_indegree = calculate_indegree(digraph)
    for node in nodes:
        random_number = randrange(1, 100000000)/100000000.0
        #calcute the probability of choosing the node
        probability_of_choosing = float(sum(digraph[node])+1)/float(total_indegree + len(digraph))
        if random_number < probability_of_choosing:
            choosed_node.add(node)

    return choosed_node


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
    print digraph
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
    print degree_distribution
    return degree_distribution

def plot_degree_distribution(degree_distribution):
    """
    Function plots the degree distribution use matplotlib.pylab
    """
    degrees = degree_distribution.keys()
    number_of_degrees = degree_distribution.values()

    plt.plot(degrees, number_of_degrees, 'r', marker='.', linestyle='None')
    plt.title("In degree distibution of dpa GRAPH")
    plt.xlabel('In degree')
    plt.ylabel('Distribution')
    plt.show()

if __name__ == "__main__":
    GRAPH = dpa_graph(27770, 12)
    CITATION_DEGREE_DISTRIBUTION = in_degree_distribution(GRAPH)
    plot_degree_distribution(CITATION_DEGREE_DISTRIBUTION)

