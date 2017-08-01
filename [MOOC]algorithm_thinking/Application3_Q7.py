"""
Program distortion of the 111 county cancer risk data set using methold of 
kmeans_clustering and hierarchical_clustering.
"""

import math
import random
import urllib2
import alg_cluster

import project3
import alg_clusters_matplotlib



###################################################
# Code to load data tables

# URLs for cancer risk data tables of various sizes

DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"
DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"



def load_data_table(data_url):
    """
    Import a table of county-based cancer risk data
    from a csv format file
    """
    data_file = urllib2.urlopen(data_url)
    data = data_file.read()
    data_lines = data.split('\n')
    print "Loaded", len(data_lines), "data points"
    data_tokens = [line.split(',') for line in data_lines]
    return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])]
            for tokens in data_tokens]


#####################################################################
# Code to load cancer data, compute a clustering and
# visualize the results


def compute_distortion(cluster_list, data_table):
    """
    Function compute the distortion of given data_table.
    Return a float number.
    """
    cluster_distortion = 0
    for clustering in cluster_list:
        cluster_distortion = clustering.cluster_error(data_table) \
            + cluster_distortion
    return cluster_distortion

def distortion_of_clustering():
    """
    Load a data table, compute a list of clusters and
    plot a list of clusters

    """
    data_table = load_data_table(DATA_111_URL)

    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), \
            line[1], line[2], line[3], line[4]))
    hierarchical_cluster_list = project3.hierarchical_clustering(singleton_list, 9)
    print "hierarchical",compute_distortion(hierarchical_cluster_list, data_table)
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), \
        line[1], line[2], line[3], line[4]))
    kmeans_cluster_list = project3.kmeans_clustering(singleton_list, 9, 5)
    print "kmeans",compute_distortion(kmeans_cluster_list, data_table)



distortion_of_clustering()
