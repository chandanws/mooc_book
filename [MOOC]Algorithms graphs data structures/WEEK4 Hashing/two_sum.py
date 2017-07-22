
def two_sum_count(numbers, low, high):
	"""
	Compute the number of target values t in the interval[low, high] (inclusive),
	such that there are distinct numbers x, y that satisfy x+y = t
	"""
	counts = 0

	# choose a number
	for number in numbers.keys():

		# confine another number
		for another_number in range(-number+low, -number+high+1):
			# check if it exists
			if another_number in numbers:
					counts += 1

	return counts


class HashTable(object):

	def __init__(self):

		self.size = 5E6
		self.slots = [set() * self.size]

	def put(self, key, data):

		hash_value = self.hash_function(key)
		if self.slots[hash_value]:
			self.slots[hash_value] = data
		else:
			self.slots[hash_value].add(data)

	def hash_function(self, key):

		return key//(self.size/2)

	def get(self, key):
		"""
		there key == data
		"""
		return key

	def __contains__(self, item):

		for keyset in self.slots:
			for key in keyset:
				if key == item:
					return True

		else False

if __name__ == "__main__":

	# target files for counting
	text_file = 'two_sum.txt'

	numbers = {}

	with open(text_file, 'r') as infile:
		for line in infile.readlines():
			numbers[int(line)] = 1



	print(two_sum_count(numbers, -10000, 10000))
