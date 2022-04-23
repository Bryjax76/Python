import temperatura
import unittest

class TestCalc(unittest.TestCase):
	def test_kelwin(self):
		self.assertEqual(temperatura.kelwin(3),276.15)
		self.assertEqual(temperatura.kelwin(-5),268.15)
	def test_fahrenheit(self):
		self.assertEqual(temperatura.fahrenheit(5),41)
		self.assertEqual(temperatura.fahrenheit(-5),23)

if __name__ == '__main__':  
        unittest.main()
