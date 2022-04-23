from Klub_7 import KlubPilkarski 
import unittest
import os

class TestPlikTxt(unittest.TestCase):

	def setUp(self):
		self.test_dane = KlubPilkarski("Bayern", "Legia")

	def test_txt(self):
		self.zmienna = self.test_dane.Plik()
		zmienna = open("klub.txt", "r")
		tab = []
		for i in zmienna:
			tab.append(i)

		self.assertEqual(tab[0].strip("\n"),"Bayern")

	#def tearDown(self):
	#	self.zmienna2 = self.test_dane.delete_klubPilkarski()
	#	if(self.assertEqual(self.zmienna2, os.path.exists('klub.txt'))):
	#		os.remove('klub.txt')

	def tearDown(self):
		os.remove('klub.txt')


if __name__ == '__main__':
    unittest.main()