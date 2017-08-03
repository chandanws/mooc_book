import unittest


class Node:
	"""
	Each node contains one element
	"""
	def __init__(self, elem):
		self.parent = []
		self.elem = elem
		self.rank = 0


class DisjointSet:
	"""
	Disjoint set data strcuture
	"""

	def __init__(self):
		self.sets = []

	def make_set(self, node):
		"""
		creates a new set whose only member (and thus representative) is x.
		"""
		node.parent = node
		self.sets.append(node)

	def union(self, nodex, nodey):
		"""
		unites the dynamic sets that contain x and y, into a new set that is the union of these two sets.
		"""
		tree_x = self.find_set(nodex)
		tree_y = self.find_set(nodey)
		if tree_x.rank > tree_y.rank:
			tree_y.parent = tree_x
			self.sets.remove(tree_y)
			tree_x.rank += 1
		else:
			tree_x.parent = tree_y
			self.sets.remove(tree_x)
			tree_y.rank += 1


	def find_set(self, node):
		"""
		returns the representative of the set containing x
		"""
		if node != node.parent:
			node.parent = self.find_set(node.parent)
		return node.parent

	def __len__(self):
		return len(self.sets)


class TestDisjointSet(unittest.TestCase):

	def test_make_set(self):
		to_test = DisjointSet()
		for elem in range(10):
			newnode = Node(elem)
			to_test.make_set(newnode)
		self.assertEqual(len(to_test), 10)

	def test_find_set(self):
		to_test = DisjointSet()
		elems = [i for i in range(10)]
		elems_to = {}
		for elem in elems:
			newnode = Node(elem)
			elems_to[elem] = newnode
			to_test.make_set(newnode)

		self.assertEqual(to_test.find_set(elems_to[5]), elems_to[5])

	def test_union(self):
		to_test = DisjointSet()
		elems = [i for i in range(10)]
		elems_to = {}
		for elem in elems:
			newnode = Node(elem)
			elems_to[elem] = newnode
			to_test.make_set(newnode)

		x = elems_to[1]
		y = elems_to[2]
		to_test.union(x, y)
		self.assertEqual(to_test.find_set(x), to_test.find_set(y))


if __name__ == "__main__":
	unittest.main()