#!/usr/bin/python
"""
This file use citation graph to calcute the degrees distribution.
The url of the graph is
http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt
"""

# imports
import urllib2
import matplotlib.pylab as plt

def load_graph(graph_url):
    """
    Function loads a graph
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))
    return answer_graph

def make_graph_use_nodes(nodes):
    """
    Function use nodes provided to create a new graph.
    Return a dictory whose keys are nodes, values are 0.
    """
    digraph = {}
    for node in nodes:
        digraph[node] = 0
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

    print "Number of nodes is",len(nodes)
    degrees = degree_digraph.values()
    sum_degrees = 0
    for degree in degrees:
        sum_degrees = sum_degrees + degree
    print "Everage of degree is", sum_degrees/len(nodes)
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

    plt.loglog(degrees, number_of_degrees, 'r', marker='.', linestyle='None')
    plt.title("In degree distibution of CITATION GRAPH")
    plt.xlabel('In degree')
    plt.ylabel('Distribution')
    plt.show()

if __name__ == "__main__":
    CITATION_URL = 'http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt'
    GRAPH = load_graph(CITATION_URL)
    CITATION_DEGREE_DISTRIBUTION = in_degree_distribution(GRAPH)
    plot_degree_distribution(CITATION_DEGREE_DISTRIBUTION)

