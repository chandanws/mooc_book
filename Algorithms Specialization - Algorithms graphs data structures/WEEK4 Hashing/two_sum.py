class HashTable(object):

	def __init__(self):

		self.size = 5000000
		self.slots = [set() for i in range(self.size)]
		self.data = set()

	def put(self, key, data):

		hash_value = self.hash_function(key)
		self.slots[hash_value].add(data)
		self.data.add(data)

	def hash_function(self, key):

		return key//(self.size//2)

	def get(self, key):
		"""
		there key == data
		"""
		slot = self.hash_function(key)
		if key in self.slots[slot]:
			return key
		else:
			return None

	def buildfromfile(self, textfile):

		with open(text_file, 'r') as infile:
			for line in infile.readlines():
				self.put(int(line), int(line))

	def two_sum_count(self):
		"""
		Compute the number of target values t in the interval[low, high] (inclusive),
		such that there are distinct numbers x, y that satisfy x+y = t
		"""
		sums = set()

		for key1 in self.data:
			left = self.hash_function(-key1-10000)
			right = self.hash_function(-key1+10000)

			for slot in self.slots[left:right+1]:

				for key2 in slot:

					if 10000 > key1 + key2 > -10000:
						sums.add(key1+key2)

		return len(sums)


if __name__ == "__main__":

	# target files for counting
	text_file = 'two_sum.txt'

	hashnumber = HashTable()
	hashnumber.buildfromfile(text_file)
	print(hashnumber.two_sum_count())