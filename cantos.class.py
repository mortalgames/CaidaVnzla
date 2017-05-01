casa_grande = [12, 1, 12]
trivilin_mano = [9, 9, 9]

class Cantos(object):

	def __init__(self, hand):
		self.hand = hand
		self.__canto = None
		self.__message = None
		self.__points = 0
		self.valid_hand()

	def valid_hand(self):
		if type(self.hand) is not list:
			raise TypeError("hand should be a list")

	def casa_grande(self):
		if [1, 12, 12] == sorted(self.hand):
			self.canto = "Casa grande"
			self.points = 12
			return True
		return False

	def trivilin(self):
		for number in self.hand:
			if self.hand.count(number) == 3:
				self.canto = "Trivilin"
				self.points = 5
				return True
		return False

	def check_hand(self):

		if self.trivilin():
			return self.canto, self.points
		elif self.casa_grande():
			return self.canto, self.points
		else:
			return "Continue..."
		

canto = Cantos(casa_grande)
canto_ganador, canto_puntos = canto.check_hand()
print(canto_ganador, canto_puntos)