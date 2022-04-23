from imie import Pracownik 
import unittest

class TestImie(unittest.TestCase):

	def setUp(self):
		self.test_dane = Pracownik("Jan","Kowalski",2000)

	def test_email(self):
		self.zmienna = self.test_dane.email()
		self.assertEqual(self.zmienna,"Jan.Kowalski@testemail.com")
	def test_nazwa(self):
		self.zmienna = self.test_dane.nazwa()
		self.assertEqual(self.zmienna,"Jan Kowalski")
	def test_wynagrodzenie(self):
		self.zmienna = self.test_dane.podwyzka()
		self.assertEqual(self.zmienna,4000)

if __name__ == '__main__':
    unittest.main()
