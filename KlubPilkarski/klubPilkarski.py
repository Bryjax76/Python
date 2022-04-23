class KlubPilkarski():

	def __init__(self,klub,trener=None):
		self.klub = klub
		self.trener = trener

#	def klub_1(self):
#		return self.trener == False
#	def klub_2(self):
#		return self.trener == True
#	def klub_3(self):
#		return self.trener == True

	def Klub(self):
		if(self.trener != None):
			return True
		else:
			return False