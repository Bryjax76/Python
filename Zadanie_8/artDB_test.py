import artDB
import unittest
import os
import sqlite3


class TestDB(unittest.TestCase):

	def setUp(self):
		artDB.create_database()

	def test_select(self):
		self.result = artDB.select_all_kluby('Bayern')
		self.assertEqual(self.result, [('Niemcy',)])

	def test_update(self):
		self.result = artDB.update_all_kluby('Hiszpania','Paris Platynov')
		self.assertEqual(artDB.select_all_kluby('AC Milan'), [('Hiszpania',)])

	def test_delete(self):
		self.result = artDB.delete_all_kluby('Baza 44')
		self.assertEqual(artDB.select_all_kluby('Baza 44'),[])


	def tearDown(self): 
		os.remove('mydatabase.db')



if __name__ == '__main__':
    unittest.main()
