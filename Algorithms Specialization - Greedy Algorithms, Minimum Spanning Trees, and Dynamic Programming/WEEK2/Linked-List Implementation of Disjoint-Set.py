import unittest


class Node:
	"""
	class Node for double liked list
	"""
	def __init__(self, elem):
		self.prev = None
		self.elem = elem
		self.next = None

	def __hash__(self):
		return hash(self.elem)

	def __eq__(self, x, y):
		return x.elem == y.elem


class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def add(self, node):
		"""
		add element to disjoint set
		"""
		if self.head:
			node.prev = self
			self.tail.next = node
			self.tail = node
		else:
			self.head = node
			self.tail = node
			node.prev = self
		self.length += 1

	def __len__(self):
		return self.length

	def set_length(self, l):
		self.length = l

	def __iter__(self):
		next_node = self.head
		while next_node:
			yield next_node
			next_node = next_node.next


			

class DisjointSet:

	def __init__(self):
		self.sets = []

	def make_set(self, node):
		""" 
		creates a new set whose only member (and thus representative) is x.
		"""
		alist = LinkedList()
		alist.add(node)
		self.sets.append(alist)
		return alist

	def union(self, nodex, nodey):
		"""
		unites the dynamic sets that contain x and y, into a new set that is the union of these two sets.
		"""
		listx = self.find_set(nodex)
		listy = self.find_set(nodey)
		
		# append the shorter list onto the longer.
		if len(listx) > len(listy):
			listx.tail.next = listy.head
			for y in listy:
				y.prev = listx
			listx.tail = listy.tail
			listx.set_length = len(listx) + len(listy)
			self.sets.remove(listy)
		else:
			listy.tail.next = listx.head
			for x in listx:
				x.prev = listy
			listy.tail = listx.tail
			listy.setlength = len(listx) + len(listy)
			self.sets.remove(listx)



	def find_set(self, node):
		"""
		returns the representative of the set containing x
		"""
		return node.prev

	def connected_components(self):
		for link_list in self.sets:
			print('( ', end='')
			for node in link_list:
				print(node.elem, end=' ')
			print(') ', end='')

	def __len__(self):
		return len(self.sets)


class TestNode(unittest.TestCase):

	def test_hash(self):
		nodes1 = Node(5)
		nodes2 = Node(6)
		dic_test = {}
		dic_test[nodes1] = 'saf'
		dic_test[nodes2] = '4sf'


class TestLinkedList(unittest.TestCase):

	def tests_add(self):
		alist = LinkedList()
		for elem in range(10):
			alist.add(Node(elem))

	def test_iter(self):
		alist = LinkedList()
		for elem in range(10):
			alist.add(Node(elem))
		to_test = []
		for node in alist:
			to_test.append(node.elem)
		self.assertEqual(to_test, [ i for i in range(10)])

	def test_length(self):
		alist = LinkedList()
		for elem in range(10):
			alist.add(Node(elem))
		self.assertEqual(len(alist), 10)
		alist.set_length(100)
		self.assertEqual(len(alist), 100)


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

		to_test2 = LinkedList()
		to_test2.add(elems_to[5])

		self.assertEqual(to_test.find_set(elems_to[5]), to_test2)

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

	def test_connected_components(self):
		to_test = DisjointSet()
		elems = [i for i in range(10)]
		elems_to = {}
		for elem in elems:
			newnode = Node(elem)
			elems_to[elem] = newnode
			to_test.make_set(newnode)

		to_test.union(elems_to[2], elems_to[4])
		to_test.union(elems_to[5], elems_to[1])
		to_test.union(elems_to[8], elems_to[0])
		to_test.union(elems_to[4], elems_to[0])

		to_test.connected_components()


if __name__ == "__main__":
	unittest.main()

