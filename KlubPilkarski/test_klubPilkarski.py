from klubPilkarski import KlubPilkarski 
import unittest

class TestTrener(unittest.TestCase):

	def setUp(self):
		self.test_dane = KlubPilkarski("Klub", "Trener")

	def test_trener(self):
		self.zmienna = self.test_dane.Klub()
		self.assertEqual(self.zmienna,True)




#	def test_klub_1(self):
#		self.zmienna = self.test_dane.klub_1()
#		self.assertEqual(self.zmienna,False)

#	def test_klub_2(self):
#		self.zmienna = self.test_dane.klub_2()
#		self.assertEqual(self.zmienna,True)

#	def test_klub_3(self):
#		self.zmienna = self.test_dane.klub_3()
#		self.assertEqual(self.zmienna,True)

if __name__ == '__main__':
    unittest.main()