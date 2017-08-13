import sys
import unittest


def optimal_bst(freq):
	def opt_cost(hash_table, freq, i, j):
		"""
		Optimal Binary Search Tree
		Recursive Method used here
		"""

		# base case: only 0~1 element
		if j < i:
			return 0
		if j == i:
			return freq[i]

		# if already exists
		if (i, j) in hash_table:
			return hash_table[(i, j)]

		min_cost = sys.maxsize
		for r in range(i, j + 1):
			cost = opt_cost(hash_table, freq, i, r - 1) + opt_cost(hash_table, freq, r + 1, j)
			if cost < min_cost:
				min_cost = cost

		hash_table[(i, j)] = sum(freq[i:j + 1]) + min_cost
		return hash_table[(i, j)]

	return opt_cost({}, freq, 0, len(freq) - 1)


class TestOptimalBST(unittest.TestCase):
	def test_small1(self):
		freq = [34, 8, 50]
		result = optimal_bst(freq)
		answer = 142
		self.assertEqual(result, answer)

	def test_small2(self):
		freq = [34, 8, 50, 4, 5, 2, 4, 7, 8, 13, 43]
		result = optimal_bst(freq)
		answer = 413
		self.assertEqual(result, answer)

	def test_medium(self):
		freq = [42, 28, 22, 29, 73, 31, 61, 38, 80, 87, 54, 79, 33, 70, 93, 33, 50, 83, 99, 16, 98, 34, 18, 30, 54, 3,
		        8, 68, 82, 47, 46, 64, 95, 1, 60, 22, 72, 67, 62, 58, 54, 82, 68, 84, 84, 10, 3, 11, 38, 79, 12, 41, 91,
		        47, 2, 71, 38, 84, 36, 27, 5, 52, 71, 100, 14, 13, 9, 33, 4, 47, 17, 41, 100, 76, 42, 34, 97, 5, 53, 78,
		        34, 40, 77, 55, 91, 99, 36, 80, 37, 72, 78, 23, 84, 51, 70, 22, 86, 35, 13, 13]
		result = optimal_bst(freq)
		answer = 26439
		self.assertEqual(result, answer)


if __name__ == '__main__':
	unittest.main()
