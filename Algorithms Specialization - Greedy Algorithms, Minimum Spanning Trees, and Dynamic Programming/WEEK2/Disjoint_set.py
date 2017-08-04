import unittest


class DisjointSet:
	"""
	Disjoint set data structure
	"""

	def __init__(self):
		self.sets = []
		self.parent = {}
		self.rank = {}
		self._num = 0

	def make_set(self, node):
		"""
		creates a new set whose only member (and thus representative) is x.
		"""
		self.parent[node] = node
		self.sets.append(node)
		self.rank[node] = 0
		self._num += 1

	def union(self, x, y):
		"""
		unites the dynamic sets that contain x and y, into a new set that is the union of these two sets.
		"""
		x_root = self.find_set(x)
		y_root = self.find_set(y)
		if x_root == y_root:
			return

		if self.rank[x_root] > self.rank[y_root]:
			self.parent[y_root] = x_root
		else:
			self.parent[x_root] = y_root
			if self.rank[x_root] == self.rank[y_root]:
				self.rank[y_root] = self.rank[y_root] + 1
		self._num -= 1

	def find_set(self, x):
		"""
		returns the representative of the set containing x
		"""
		if self.parent[x] != x:
			self.parent[x] = self.find_set(self.parent[x])
		return self.parent[x]

	def __len__(self):
		return self._num


class TestDisjointSet(unittest.TestCase):

	def test_make_set(self):
		to_test = DisjointSet()
		for elem in range(10):
			to_test.make_set(elem)

	def test_find_set(self):
		to_test = DisjointSet()
		for elem in range(10):
			to_test.make_set(elem)

		self.assertEqual(to_test.find_set(5), 5)

	def test_union(self):
		to_test = DisjointSet()
		elems = [i for i in range(10)]
		for elem in elems:
			to_test.make_set(elem)
		self.assertEqual(len(to_test), 10)
		to_test.union(1, 2)
		self.assertEqual(len(to_test), 9)
		to_test.union(2, 4)
		to_test.union(4, 7)
		self.assertEqual(to_test.find_set(1), to_test.find_set(4))
		self.assertNotEqual(to_test.find_set(1), to_test.find_set(5))
		self.assertEqual(to_test.find_set(1), to_test.find_set(7))
		self.assertEqual(len(to_test), 7)


if __name__ == "__main__":
	unittest.main()