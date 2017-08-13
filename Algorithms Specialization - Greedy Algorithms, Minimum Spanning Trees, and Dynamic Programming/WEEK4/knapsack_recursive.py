import unittest
import sys
sys.setrecursionlimit(3000)


def knapSack(val, wt, capacity):
	"""
	Recursive implementation of 0-1 Knapsack Problem

	val: value
	wt: weight
	capacity: capacity
	"""
	def max_value(i, j):
		# base case
		if i == 0:
			return 0

		# sub-problem computed
		if (i, j) in hash_table:
			return hash_table[(i, j)]
		else:
			if wt[i - 1] > j:

				# only case 1
				max_val = max_value(i - 1, j)
				hash_table[(i, j)] = max_val
			else:
				#  case 1, item i-1 excluded
				case1 = max_value(i - 1, j)
				# case 2, item i-1 included
				case2 = max_value(i - 1, j - wt[i - 1]) + val[i - 1]
				max_val = max(case1, case2)
				hash_table[(i, j)] = max_val
		return max_val

	hash_table = {}
	return max_value(len(val), capacity)


class TestKnapsack(unittest.TestCase):
	def tests_final(self):
		values = []
		weights = []
		with open('input_random_44_2000000_2000.txt') as infile:
			line = infile.readline()
			line = line.strip('\n').split(' ')
			capacity, n = [int(item) for item in line]
			for line in infile.readlines():
				line = line.strip('\n').split(' ')
				val, weight = [int(item) for item in line]
				values.append(val)
				weights.append(weight)
		if n != len(values):
			raise ValueError

		max_val = knapSack(values, weights, capacity)
		self.assertEqual(max_val, 49957183)

	def notest_large(self):
		values = []
		weights = []
		with open('input_random_29_10000_1000.txt') as infile:
			line = infile.readline()
			line = line.strip('\n').split(' ')
			capacity, n = [int(item) for item in line]
			for line in infile.readlines():
				line = line.strip('\n').split(' ')
				val, weight = [int(item) for item in line]
				values.append(val)
				weights.append(weight)
		if n != len(values):
			raise ValueError

		max_val = knapSack(values, weights, capacity)
		self.assertEqual(max_val, 167375)

	def notests_big(self):
		values = []
		weights = []
		with open('input_random_19_100_1000.txt') as infile:
			line = infile.readline()
			line = line.strip('\n').split(' ')
			capacity, n = [int(item) for item in line]
			for line in infile.readlines():
				line = line.strip('\n').split(' ')
				val, weight = [int(item) for item in line]
				values.append(val)
				weights.append(weight)
		if n != len(values):
			raise ValueError

		max_val = knapSack(values, weights, capacity)
		self.assertEqual(max_val, 1580)

	def notests_small(self):
		values = []
		weights = []
		with open('small_test_case.txt') as infile:
			line = infile.readline()
			line = line.strip('\n').split(' ')
			capacity, n = [int(item) for item in line]
			for line in infile.readlines():
				line = line.strip('\n').split(' ')
				val, weight = [int(item) for item in line]
				values.append(val)
				weights.append(weight)
		if n != len(values):
			raise ValueError

		max_val = knapSack(values, weights, capacity)
		self.assertEqual(max_val, 8)


if __name__ == '__main__':
	unittest.main()
