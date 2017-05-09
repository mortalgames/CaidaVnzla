cartas= [4,10,8]

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
		if [1, 10, 10] == sorted(self.hand):
			self.canto = "Casa grande"
			self.points = 10
			return True
		return False

	def casa_chica(self):
		if [1, 1, 10] == sorted(self.hand):
			self.canto= "Casa Chica"
			self.points= 6
			return True
		return False

	def trivilin(self):
		for number in self.hand:
			if self.hand.count(number) == 3:
				self.canto = "Trivilin"
				self.points = 5
				return True
		return False

	def vigironda(self):
		for cartas in self.hand:
			if self.hand.count(cartas) == 2:
				iguales= self.hand.pop(self.hand.index(cartas))
				self.hand.remove(iguales)
				residuo= self.hand.pop()
				if residuo + 1== iguales or residuo - 1== iguales:
					self.canto= "Vigia"
					self.points= 7
				elif 1 <= iguales <= 7:
					self.canto= "Ronda"
					self.points= 1
				elif iguales == 8:
					self.canto= "Ronda"
					self.points= 2	
				elif iguales == 9:
					self.canto= "Ronda"
					self.points= 3	
				elif iguales == 10:
					self.canto= "Ronda"
					self.points= 4
				return True
		return False

	def registro(self):
		if [1,9,10] == sorted(self.hand):
			self.canto= "Registro"
			self.points= 8
			return True
		return False
	
	def patrulla(self):
		hand= sorted(self.hand)
		if hand[0] + 1 == hand[1] and hand[1] + 1== hand[2]:
 			self.canto = "Patrulla"
 			self.points= 6
 			return True

	def check_hand(self):
		if self.casa_grande():
			return self.canto, self.points
		elif self.casa_chica():
			return self.canto, self.points
		elif self.trivilin():
			return self.canto, self.points
		elif self.vigironda():
			return self.canto, self.points
		elif self.patrulla():
			return self.canto, self.points
		elif self.registro():
			return self.canto, self.points		
		else:
			return "Continue..."
		

canto = Cantos(cartas)
canto_ganador, canto_puntos = canto.check_hand()
print(canto_ganador, canto_puntos)