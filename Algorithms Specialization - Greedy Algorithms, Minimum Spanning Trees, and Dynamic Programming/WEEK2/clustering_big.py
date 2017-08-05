from disjoint_set import DisjointSet
import unittest


class HashTable:
	def __init__(self, size):
		self.size = size
		self.slots = [None for i in range(self.size)]

	def add(self, key, value):
		if self.slots[key]:
			self.slots[key].append(value)
		else:
			self.slots[key] = [value]

	def values(self):
		key = 1
		for val in self.slots:
			if val:
				yield (key, val)
		key += 1


class BigClustring:

	def __init__(self):
		self.hash_table = None
		self.num = None
		self.len_bit = None
		self.disjoint_set = DisjointSet()
		self.val = []

	def read_from_file(self, file_name):
		with open(file_name) as infile:
			line = infile.readline()
			line = line.strip('\n')
			self.num, self.len_bit = [int(num) for num in line.split()]
			self.hash_table = HashTable(2 ** self.len_bit)

			node = 1
			for line in infile.readlines():
				line = line.strip('\n')
				line = line.replace(' ', '')
				val = int(line, 2)
				self.hash_table.add(val, node)
				self.disjoint_set.make_set(node)
				self.val.append(val)
				node += 1

		if self.num + 1 != node:
			raise ValueError

	def hamming(self):
		"""
		return binary integer at hamming distance 1 or 2
		"""
		self.hamm = []
		for i in range(self.len_bit):
			for j in range(self.len_bit):
				self.hamm.append(1 << i | 1 << j)

	def neighbors(self, val):
		"""
		return node_index of neighbors for val
		"""
		for key in self.hamm:
			if self.hash_table.slots[key ^ val] is not None:
				yield self.hash_table.slots[key ^ val][0]

	def cluster(self):

		# first find the 0 distance nodes
		for key, val in self.hash_table.values():
			if len(val) > 1:
				# union
				for val1 in val:
					for val2 in val:
						if val1 != val2:
							self.disjoint_set.union(val1, val2)

		# find neighbors of node
		node = 1
		for val in self.val:
			neighbors = self.neighbors(val)
			for neighbor in neighbors:
				self.disjoint_set.union(node, neighbor)
			node += 1
		return len(self.disjoint_set)


class TestBigCluster(unittest.TestCase):
	"""
	Test class BigClustering
	"""
	def test_small(self):
		file_name = 'testcase1_small_for_big_clustering.txt'
		to_cluster = BigClustring()
		to_cluster.read_from_file(file_name)
		to_cluster.hamming()
		k = to_cluster.cluster()
		self.assertEqual(k, 1)

	def test_medium(self):
		file_name = 'testcase2_medium_for_big_clustering.txt'
		to_cluster = BigClustring()
		to_cluster.read_from_file(file_name)
		to_cluster.hamming()
		k = to_cluster.cluster()
		self.assertEqual(k, 4)

	def test_big(self):
		file_name = 'input_random_30_128_24.txt'
		to_cluster = BigClustring()
		to_cluster.read_from_file(file_name)
		to_cluster.hamming()
		k = to_cluster.cluster()
		with open('output_random_30_128_24.txt') as infile:
			line = infile.readline()
			line = line.strip('\n')
			result = int(line)
		self.assertEqual(k, result)

	def test_large(self):
		file_name = 'input_random_38_256_24.txt'
		to_cluster = BigClustring()
		to_cluster.read_from_file(file_name)
		to_cluster.hamming()
		k = to_cluster.cluster()
		with open('output_random_38_256_24.txt') as infile:
			line = infile.readline()
			line = line.strip('\n')
			result = int(line)
		self.assertEqual(k, result)

	def test_enormous(self):
		file_name = 'clustering_big.txt'
		to_cluster = BigClustring()
		to_cluster.read_from_file(file_name)
		to_cluster.hamming()
		k = to_cluster.cluster()
		self.assertEqual(k, 6118)

if __name__ == '__main__':
	unittest.main()