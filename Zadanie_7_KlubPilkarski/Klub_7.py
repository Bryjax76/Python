import os

class KlubPilkarski():

	def __init__(self,klub,klub2):
		self.klub = klub
		self.klub2 = klub2


	def Plik(self):
		f = open("klub.txt", "w")
		f.write(self.klub + "\n")
		f.write(self.klub2 + "\n")
		f.close()

	