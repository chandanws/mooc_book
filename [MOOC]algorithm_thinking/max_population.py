"""
Program sorts by the populations of clusters.
"""
#!/usr/bin/python
#general imports
from alg_cluster import Cluster



def max_population(cluster_list, index):
    """
    Function sort by the populations of clusters.
    Input: cluster_list, index of cluster_list.
    Output: A list of index sorted by the populations of clusters.
    """
    #base case
    if len(cluster_list) == 2:
        if cluster_list[0].total_population() \
            > cluster_list[1].total_population():
            return [index[0], index[1]]
        else:
            return [index[1], index[0]]
    if len(cluster_list) == 1:
        return [index[0]]
    #divide
    len_cluster = len(cluster_list)
    medium = len_cluster/2
    left_cluster = cluster_list[0 : medium]
    right_cluster = cluster_list[medium : len_cluster]
    left_index = index[0 : medium]
    right_index = index[medium : len_cluster]
    index_left = max_population(left_cluster, left_index)
    index_right = max_population(right_cluster, right_index)
    #conquer
    index_list = []
    dummy_left = 0
    dummy_right = 0
    while dummy_left + dummy_right < len(index_left) + len(index_right) -3:
        print 'cluster_list[dummy_left].total_population()',cluster_list[dummy_left].total_population()
        print 'cluster_list[dummy_right].total_population()',cluster_list[dummy_right].total_population()
        if cluster_list[dummy_left].total_population()\
            > cluster_list[dummy_right].total_population():
            index_list.append(index_left[dummy_left])
            if dummy_left < len(index_left)-1:
                dummy_left = dummy_left + 1
                print 'dummy_left=', dummy_left
        else:
            index_list.append(index_right[dummy_right])
            if dummy_right < len(index_right)-1:
                dummy_right = dummy_right + 1
                print 'dummy_right=', dummy_right

    return index_list

if __name__ == "__main__":
    CLUSTER_LIST = [Cluster(set([]), 0, 0, 12, 0),\
    Cluster(set([]), 0, 0, 20, 0),\
    Cluster(set([]), 0, 0, 30, 0),\
    Cluster(set([]), 0, 0, 40, 0),\
    Cluster(set([]), 0, 0, 100, 0),\
    Cluster(set([]), 0, 0, 90, 0),\
    Cluster(set([]), 0, 0, 80, 0),\
    Cluster(set([]), 0, 0, 70, 0),\
    Cluster(set([]), 0, 0, 1, 0),\
    Cluster(set([]), 0, 0, 2, 0),\
    Cluster(set([]), 0, 0, 3, 0),\
    Cluster(set([]), 0, 0, 4, 0),\
    Cluster(set([]), 0, 0, 5, 0),\
    Cluster(set([]), 0, 0, 6, 0),\
    Cluster(set([]), 0, 0, 7, 0)]
    INDEX = range(15)
    print max_population(CLUSTER_LIST, INDEX)

