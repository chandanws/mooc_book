#!/usr/bin/python
"""
This file use ER graph to calcute the degrees distribution.
The url of the graph is
"""

# imports
from random import randrange
import matplotlib.pylab as plt

def er_graph(num_nodes, probability_p, probability_q):
    """
    Function creat a  er graph
    Returns a dictionary that models a graph
    """
    nodes = range(num_nodes)
    digraph = make_graph_use_nodes(nodes, set([]))
    for neighbor1 in nodes:
        digraph[neighbor1] = set([])
        for neighbor2 in nodes:
            if neighbor1 == neighbor2:
                continue
            random_number1 = randrange(0,101,1)/100.0
            if (random_number1 < probability_p):
                digraph[neighbor1].add(neighbor2)
    for neighbor1 in nodes:
        for neighbor2 in nodes:
            if neighbor1 == neighbor2:
                continue
            random_number2 = randrange(0,101,1)/100.0
            if (random_number2 < probability_q):
                digraph[neighbor2].add(neighbor1)
    return digraph

def make_graph_use_nodes(nodes, initial):
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
    degree_digraph = make_graph_use_nodes(nodes, 0)
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
            degree_distribution[degree] =  1
        if degree > max_degree:
            max_degree = degree

    #normailze
    degrees = degree_distribution.keys()
    total_number_of_degree = sum(degree_distribution.values())
    for degree in degrees:
        degree_distribution[degree] = float(degree_distribution[degree]) \
                /float(total_number_of_degree)
    return degree_distribution

def plot_degree_distribution(degree_distribution):
    """
    Function plots the degree distribution use matplotlib.pylab
    """
    degrees = degree_distribution.keys()
    number_of_degrees = degree_distribution.values()

    plt.plot(degrees, number_of_degrees, 'r', marker='.', linestyle='None')
    plt.title("In degree distibution of ER GRAPH")
    plt.xlabel('In degree')
    plt.ylabel('Distribution')
    plt.show()

if __name__ == "__main__":
    GRAPH = er_graph(1000, 0.5, 0.5)
    CITATION_DEGREE_DISTRIBUTION = in_degree_distribution(GRAPH)
    plot_degree_distribution(CITATION_DEGREE_DISTRIBUTION)

