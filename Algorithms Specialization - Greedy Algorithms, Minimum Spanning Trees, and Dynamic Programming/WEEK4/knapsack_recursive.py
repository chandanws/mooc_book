import unittest
import sys

sys.setrecursionlimit(3000)


def knapsack01_recursive(hash_table, value, weight, i, j):
	# base case: when 1 items here
	if i == 1:
		if weight[i - 1] < j:
			hash_table[(i, j)] = value[i - 1]
			return value[i - 1]
		else:
			hash_table[(i, j)] = 0
		return 0

	# sub-problem computed
	if (i, j) in hash_table:
		return hash_table[(i, j)]
	else:
		if weight[i - 1] > j:
			# only case 1
			hash_table[(i, j)] = knapsack01_recursive(hash_table, value, weight, i - 1, j)
		else:
			#  case 1, item i-1 excluded
			case1 = knapsack01_recursive(hash_table, value, weight, i - 1, j)
			# case 2, item i-1 included
			case2 = knapsack01_recursive(hash_table, value, weight, i - 1, j - weight[i - 1]) + value[i - 1]
			hash_table[(i, j)] = max(case1, case2)

	return hash_table[(i, j)]


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

		max_val = knapsack01_recursive({}, values, weights, n, capacity)
		self.assertEqual(max_val, 49957183)

	def notests_large(self):
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

		max_val = knapsack01_recursive({}, values, weights, n, capacity)
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

		max_val = knapsack01_recursive({}, values, weights, n, capacity)
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

		max_val = knapsack01_recursive({}, values, weights, n, capacity)
		self.assertEqual(max_val, 8)


if __name__ == '__main__':
	unittest.main()
