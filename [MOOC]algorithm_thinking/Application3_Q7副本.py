"""
Program distortion of the county cancer risk data set using methold of 
kmeans_clustering and hierarchical_clustering.
"""

import urllib2
import alg_cluster

import project3
import matplotlib.pylab as plt


###################################################
# Code to load data tables

# URLs for cancer risk data tables of various sizes

DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"
DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"
DATA_896_URL = DIRECTORY + "data_clustering/unifiedCancerData_896.csv"



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
    data_table = load_data_table(DATA_896_URL)
    hierarchical_distortion_list = []
    kmeans_distortion_list = []

    for num_cluster in xrange(6, 21):
        singleton_list = []
        for line in data_table:
            singleton_list.append(alg_cluster.Cluster(set([line[0]]), \
                line[1], line[2], line[3], line[4]))
        hierarchical_cluster_list = project3.hierarchical_clustering(singleton_list, num_cluster)
        hierarchical_distortion_list.append(compute_distortion(hierarchical_cluster_list, data_table))

        singleton_list = []
        for line in data_table:
            singleton_list.append(alg_cluster.Cluster(set([line[0]]), \
                line[1], line[2], line[3], line[4]))
        kmeans_cluster_list = project3.kmeans_clustering(singleton_list, num_cluster, 5)
        kmeans_distortion_list.append(compute_distortion(kmeans_cluster_list, data_table))
    plt.figure()
    plt.hold(True)
    plt.plot(range(6, 21), hierarchical_distortion_list, 'r', label=' hierarchical')
    plt.plot(range(6, 21), kmeans_distortion_list, 'b', label='kmeans')
    plt.legend(loc='upper right')
    plt.title('Quality Comparision DataSet=896')
    plt.xlabel('Num_clusters')
    plt.ylabel('Distortion')
    plt.hold(False)
    plt.show()

distortion_of_clustering()
