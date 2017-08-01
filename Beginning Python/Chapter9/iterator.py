
class Fibs:
	"""
	Fibonacci numbers
	"""

	def __init__(self):
		self.a = 0
		self.b = 1

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 1000:
			raise StopIteration
		return self.a

	def __iter__(self):
		return self

if __name__ == "__main__":
	fibs = Fibs()
	for f in fibs:
		print(f)