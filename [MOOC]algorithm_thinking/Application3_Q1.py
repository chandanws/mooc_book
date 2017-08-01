#!/usr/bin/python
#Filename: Application3.py
"""
This program completes the project3 of algorithm thinking.
"""



#general imports
from alg_cluster import Cluster
from random import random
from random import sample
import time
import matplotlib.pylab as plt

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function to compute Euclidean distance between two clusters
    in cluster_list with indices idx1 and idx2.
    Returns tuple (dist, idx1, idx2) with idx1 < idx2
    where dist is distance between cluster_list[idx1] and
    cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(\
            cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def pair_distance_not_sort(cluster_list, idx1, idx2):
    """
    Helper function to compute Euclidean distance between two clusters
    in cluster_list with indices idx1 and idx2.
    Returns tuple (dist, idx1, idx2) where dist is distance
    between cluster_list[0] and cluster_list[1]
    """
    return (cluster_list[0].distance(\
            cluster_list[1]), idx1, idx2)

def slow_closest_pairs(cluster_list):
    """
    Compute the set of closest pairs of cluster in list of clusters
    using O(n^2) all pairs algorithm

    Returns the set of all tuples of the form (dist, idx1, idx2)
    where the cluster_list[idx1] and cluster_list[idx2]
    have minimum distance dist.

    """
    closest_pairs = []
    closest_pair = (float('inf'), -1, -1)
    closest_pairs.append(closest_pair)
    cluster_length = len(cluster_list)

    for index1 in xrange(cluster_length):
        for index2 in xrange(cluster_length):
            if index1 != index2:
                distance_of_pair = pair_distance(cluster_list, index1, index2)
                distance_of_pair = distance_of_pair[0]
                if closest_pairs[0][0] > distance_of_pair:
                    closest_pairs[0] = (distance_of_pair,\
                            min(index1, index2), max(index1, index2))
                elif closest_pairs[0][0] == distance_of_pair:
                    closest_pairs.append((distance_of_pair,\
                            min(index1, index2), max(index1, index2)))
    closest_pairs_final = closest_pairs
    for closest_pair in closest_pairs[1 : -1]:
        if closest_pair[0] > closest_pairs[0][0]:
            closest_pairs_final.remove(closest_pair)
    closest_pairs_set = set(closest_pairs_final)
    return closest_pairs_set

def fast_closest_pair(cluster_list):
    """
    Compute a closest pair of clusters in cluster_list
    using O(n log(n)) divide and conquer algorithm

    Returns a tuple (distance, idx1, idx2) with idx1 < idx 2 where
    cluster_list[idx1] and cluster_list[idx2]
    have the smallest distance dist of any pair of clusters
    """
    def fast_helper(cluster_list, horiz_order, vert_order):
        """
        Divide and conquer method for computing distance between
        closest pair of points
        Running time is O(n * log(n))

        horiz_order and vert_order are lists of indices for clusters
        ordered horizontally and vertically

        Returns a tuple (distance, idx1, idx2) with idx1 < idx 2 where
        cluster_list[idx1] and cluster_list[idx2]
        have the smallest distance dist of any pair of clusters

        """

        # base case
        if len(horiz_order) <= 3:
            cluster_list_ordered = [cluster_list[horiz_order[order]] \
                for order in xrange(len(horiz_order))]
            closest_pairs = slow_closest_pairs(cluster_list_ordered)
            closest_pair = closest_pairs.pop()
            (closest_distance, index_i, index_j) =\
                    closest_pair
            return (closest_distance, \
                min(horiz_order[index_i], horiz_order[index_j]),\
                max(horiz_order[index_i], horiz_order[index_j]))

        # divide
        else:
            medium = len(horiz_order)/2
            middle_horiz = (cluster_list[horiz_order[medium-1]].horiz_center()\
                +cluster_list[horiz_order[medium]].horiz_center())/2.0
            horiz_left = horiz_order[0 : medium]
            horiz_right = horiz_order[medium : len(horiz_order)]
            vert_left = [order for order in vert_order if order in horiz_left]
            vert_right = [order for order in vert_order if order in horiz_right]
            (distance, index_i, index_j) = min(\
                    fast_helper(cluster_list, horiz_left, vert_left),\
                    fast_helper(cluster_list, horiz_right, vert_right))
        # conquer
            vertical_small = [order for order in vert_order \
                    if abs(cluster_list[order].horiz_center() - middle_horiz)\
                    <= distance]
            for inx1 in xrange(0, len(vertical_small)-1):
                for inx2 in xrange(inx1+1, min(inx1+4, len(vertical_small))):
                    (distance, index_i, index_j) = min(\
                            (distance, index_i, index_j),\
                            pair_distance(cluster_list,\
                            vertical_small[inx1], vertical_small[inx2]))
        return (distance, index_i, index_j)

    # compute list of indices for the clusters ordered in the
    # horizontal direction
    hcoord_and_index = [(cluster_list[idx].horiz_center(), idx)
                        for idx in range(len(cluster_list))]
    hcoord_and_index.sort()
    horiz_order = [hcoord_and_index[idx][1] \
        for idx in range(len(hcoord_and_index))]

    # compute list of indices for the clusters ordered in vertical direction
    vcoord_and_index = [(cluster_list[idx].vert_center(), idx)
                        for idx in range(len(cluster_list))]
    vcoord_and_index.sort()
    vert_order = [vcoord_and_index[idx][1] \
        for idx in range(len(vcoord_and_index))]

    # compute answer recursively
    answer = fast_helper(cluster_list, horiz_order, vert_order)
    return answer

def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function mutates cluster_list

    Input: List of clusters, number of clusters
    Output: List of clusters whose length is num_clusters
    """
    while len(cluster_list) > num_clusters:
        (dummy_distance, inx1, inx2) = fast_closest_pair(cluster_list)
        Cluster.merge_clusters(cluster_list[inx1], cluster_list[inx2])
        cluster_list.remove(cluster_list[inx2])
    return cluster_list

def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Function computes an initial list of clusters with the property
    that each cluster consists of a single county chosen from the set of
    the num_cluster counties with the largest populations.
    Then compute num_iterations of k-means clustering

    Return this resulting list of clusters.
    """
    def max_population(cluster_list, num_clusters):
        """
        Function sort by the populations of clusters.
        Input: cluster_list, num_clusters
        Return: A list of index sorted by the populations of clusters.
        """
        population_list = []
        population_indices = []
        for cluster in cluster_list:
            population_list.append(cluster.total_population())
        population_list_sort = population_list[:]
        population_list_sort.sort()
        population_list_sort.reverse()
        population_list_sort = population_list_sort[0 : num_clusters]
        for population in population_list_sort:
            population_indices.append(population_list.index(population))
        return population_indices

    def renew_centering(cluster_list, center_clusters, \
            num_clusters, num_iterations):
        """
        Function renews the centering.
        Reuturn a list of clusters.
        """
        for dummy_iterations in xrange(num_iterations):
            #Initialize num_clusters empty clusters whose counties are empty set
            #and populations are zero.
            clustering_list = [Cluster(set([]), 0, 0, 0, 0) \
                for dummy_num in xrange(num_clusters)]
            #For each cluster, find the min distance center-cluster pair
            #and create a new clustering.
            cluster_index = 0
            center_index = 0
            for cluster in cluster_list:
                center_cluster_distance_list = []
                center_index = 0
                for center_cluster in center_clusters:
                    center_cluster_distance_list.append(\
                        pair_distance_not_sort([cluster, center_cluster], \
                            cluster_index, center_index))
                    center_index = center_index + 1
                min_center_cluster_distance = min(center_cluster_distance_list)
                clustering_list[min_center_cluster_distance[2]].\
                    merge_clusters(cluster_list[cluster_index])
                cluster_index = cluster_index + 1
            center_clusters = clustering_list
        return  clustering_list

    population_indices = max_population(cluster_list, num_clusters)
    center_clusters = []
    for population_index in population_indices:
        center_clusters.append(cluster_list[population_index])
    answer = renew_centering(cluster_list, center_clusters, \
        num_clusters, num_iterations)
    return answer

def gen_random_clusters(num_clusters):
    """
    Function creates a list of clusters where each cluster in this list
    corresponds to one randomly generated point in the square with corners
    (+-1, +-1).
    """
    rand_cluster_list = [Cluster(set([]), random()*sample([1, -1], 1)[0], \
        random()*sample([1, -1], 1)[0], 0, 0)\
        for dummy_num in xrange(num_clusters)]
    return rand_cluster_list

def question1():
    """
    Function compute the runing times of the functions slow_closest_pairs
    and fast_closest_pair for lists of clusters of size 2 to 200.
    """
    slow_time_list = []
    fast_time_list = []
    for cluster_size in xrange(2, 201):
        random_cluster = gen_random_clusters(cluster_size)
        #For the slow_time_list
        start_time = time.time()
        slow_closest_pairs(random_cluster)
        slow_time_list.append(time.time() - start_time)
        #For the fast_time_list
        start_time = time.time()
        fast_closest_pair(random_cluster)
        fast_time_list.append(time.time() - start_time)
    plt.figure()
    plt.hold(True)
    plt.plot(range(2, 201), slow_time_list, 'r', label='Slow Closest Pairs')
    plt.plot(range(2, 201), fast_time_list, 'b', label='Fast Closest Pair')
    plt.legend(loc='upper right')
    plt.title('Running Time Comparision')
    plt.xlabel('The size of clusters')
    plt.ylabel('Runing Time(s)')
    plt.hold(False)
    plt.show()

question1()


