import calculator
import unittest

class TestCalc(unittest.TestCase):
	def test_dod(self):
		self.assertEqual(calculator.dodawanie(3,5),8)
		self.assertEqual(calculator.dodawanie(-1,1),0)
	def test_odej(self):
		self.assertEqual(calculator.odejmowanie(5,2),3)
		self.assertEqual(calculator.odejmowanie(5,1),4)
	def test_mozenie(self):
		self.assertEqual(calculator.mnozenie(2,2),4)
		self.assertEqual(calculator.mnozenie(5,5),25)
	def test_dzielenie(self):
		with self.assertRaises(Exception) as cm:
			calculator.dzielenie(10,0)
		self.assertEqual(calculator.dzielenie(12,6),2)
	def test_potega(self):
		self.assertEqual(calculator.potega(2),4)
		self.assertEqual(calculator.potega(4),16)
	def test_pierwiastek(self):
		self.assertEqual(calculator.pierwiastek(16),4)
		self.assertEqual(calculator.pierwiastek(4),2)
	def test_procent(self):
		self.assertEqual(calculator.procent(50,100),50)
		self.assertEqual(calculator.procent(20,40),50)
if __name__ == '__main__':  
        unittest.main()
