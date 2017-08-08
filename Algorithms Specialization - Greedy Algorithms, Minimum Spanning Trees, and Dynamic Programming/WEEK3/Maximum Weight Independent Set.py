import unittest


def maximum_weight_independent_set(weights):
	"""
	Compute Maximum weight independent set for a path graph.
	Weights of vertexes in the path graph are given.
	Return maximum weight independent set.
	"""
	num = len(weights)
	a = [0] * (num + 1)
	in_set = []  # independent set
	a[0], a[1] = 0, weights[0]

	for i in range(2, num + 1):
		a[i] = max(a[i - 1], a[i - 2] + weights[i - 1])

	while i >= 1:
		if a[i - 1] >= a[i - 2] + weights[i - 1]:
			i -= 1
		else:
			in_set.append(i - 1)
			i -= 2
	in_set.reverse()
	return in_set


class TestMWIS(unittest.TestCase):
	def notest_big(self):
		with open('mwis.txt') as infile:
			weights = []
			count = 0
			for line in infile.readlines():
				line = line.strip('\n')
				if count == 0:
					num = int(line)
				else:
					weights.append(int(line))
				count += 1

		if count - 1 != num:
			raise ValueError

		inset = maximum_weight_independent_set(weights)

	def test_small4(self):
		with open('smalltestcase4.txt') as infile:
			weights = []
			count = 0
			for line in infile.readlines():
				line = line.strip('\n')
				if count == 0:
					num = int(line)
				else:
					weights.append(int(line))
				count += 1

		if count - 1 != num:
			raise ValueError
		inset = maximum_weight_independent_set(weights)
		result = [1, 3, 5, 7, 9]
		self.assertEqual(inset, result)

	def test_small3(self):
		with open('smalltestcase3.txt') as infile:
			weights = []
			count = 0
			for line in infile.readlines():
				line = line.strip('\n')
				if count == 0:
					num = int(line)
				else:
					weights.append(int(line))
				count += 1

		if count - 1 != num:
			raise ValueError
		inset = maximum_weight_independent_set(weights)
		result = [0, 2, 5, 8]

		self.assertEqual(inset, result)

	def test_smalltestcase1(self):
		with open('smalltestcase1.txt') as infile:
			weights = [int(num) for num in infile.readline().strip('\n').split(',')]

		inset = maximum_weight_independent_set(weights)
		result = [0, 2, 4, 6, 8, 10]
		self.assertEqual(inset, result)

	def test_smalltestcase2(self):
		with open('smalltestcase2.txt') as infile:
			weights = [int(num) for num in infile.readline().strip('\n').split(',')]
		inset = maximum_weight_independent_set(weights)
		result = [0, 3, 5, 7, 9]
		self.assertEqual(inset, result)


if __name__ == '__main__':
	unittest.main()
