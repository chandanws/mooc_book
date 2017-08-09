import unittest
import numpy as np


def knapsack01(value, weight, capacity):
	"""
	kanapsack01 solves a 0-1 knapsack problem,
	input: values(value) and weights(W) of items to put into knapsack ( size of which is capacity)
	output: the index of items that maximize the value of items putted in the knapsack
	the index of items counts from 0, and corresponding value
	"""
	n = len(value)  # the number of items
	# maximum value that can be attained with weight <= weight using first i items
	m = np.zeros(shape=(n + 1, capacity + 1), dtype=int)
	for i in range(capacity+1):
		m[0, i] = 0

	if not isinstance(capacity, int):
		raise ValueError('knapsack_size should be an integer')

	for i in range(1, n+1):  # items
		for j in range(1, capacity+1):  # sizes
			if weight[i-1] > j:
				m[i, j] = m[i - 1, j]
			else:
				m[i, j] = max(m[i - 1, j], m[i - 1, j - weight[i-1]] + value[i-1])

	max_val = m[-1, -1]
	items = set()

	while max_val > 0 and i > 0:
		if max_val - value[i-1] in m[i - 1, :]:
			max_val = max_val - value[i-1]
			items.add(i-1)
			i -= 1
		else:
			i -= 1
	return items, m[-1, -1]


class TestKnapsack(unittest.TestCase):


	def tests_big(self):
		values = []
		weights = []
		with open('input_random_19_100_1000.txt') as infile:
			line = infile.readline()
			line = line.strip('\n').split(' ')
			knapsack_size, num_item = [int(item) for item in line]
			for line in infile.readlines():
				line = line.strip('\n').split(' ')
				val, weight = [int(item) for item in line]
				values.append(val)
				weights.append(weight)
		if num_item != len(values):
			raise ValueError

		items, max_val = knapsack01(values, weights, knapsack_size)
		self.assertEqual(max_val, 1580)

	def tests_small(self):
		values = []
		weights = []
		with open('small_test_case.txt') as infile:
			line = infile.readline()
			line = line.strip('\n').split(' ')
			knapsack_size, num_item = [int(item) for item in line]
			for line in infile.readlines():
				line = line.strip('\n').split(' ')
				val, weight = [int(item) for item in line]
				values.append(val)
				weights.append(weight)
		if num_item != len(values):
			raise ValueError

		items, max_val = knapsack01(values, weights, knapsack_size)
		self.assertEqual(items, set([2, 3]))
		self.assertEqual(max_val, 8)


if __name__ == '__main__':
	unittest.main()
