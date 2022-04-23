class Pracownik():

	def __init__(self,imie,nazwisko,wynagrodzenie):
		self.imie = imie
		self.nazwisko = nazwisko
		self.wynagrodzenie = wynagrodzenie

	def email(self):
		return self.imie + "." + self.nazwisko + "@testemail.com"
	def nazwa(self):
		return self.imie + " " + self.nazwisko
	def podwyzka(self):
		return self.wynagrodzenie * 2
