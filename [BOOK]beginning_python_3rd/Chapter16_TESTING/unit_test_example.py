import unittest
import doc_test_example as my_math

class ProductTestCase(unittest.TestCase):

	def testIntegers(self):
		for x in xrange(-10,10):
			p = my_math.square(x)
			self.failUnless(p == x*x, 'Integer multiplication failed')

	def testFloats(self):
		for x in xrange(-10,10):
			x = x/10.0
			p = my_math.square(x)
			self.failUnless(p == x*x, 'Float multiplication failed')


if __name__ == "__main__":
	unittest.main()