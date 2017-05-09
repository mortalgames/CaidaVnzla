casa_grande = [12,12,1]
casa_chica= [12,1,1]
Registro= [11,12,1]
Patrulla= [] #VARIABLE
Vigia= []#VARIABLE
Ronda= []#VARIABLE
Trivilin= []#VARIABLE

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

	def casa_chica(self):
		if [1, 1, 12] == sorted(self.hand):
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

	def registro(self):
		if [1,11,12] == sorted(self.hand):
			self.canto= "Registro"
			self.points= 8
			return True
		return False

	def ronda(self):
		for number in self.hand:
			if self.hand.count(number) == 2:
				iguales= self.hand.pop(self.hand.index(number))
				if 1 <= iguales <= 7:
					self.canto= "Ronda"
					self.points= 1
				elif iguales == 10:
					self.canto= "Ronda"
					self.points= 2
				elif iguales == 11:
					self.canto= "Ronda"
					self.points= 3
				else:
					self.canto= "Ronda"
					self.points= 4
				return True
		return False

	def vigia(self):#REVISA Y DIME QUE OPINAS
		for number in self.hand:
			if self.hand.count(number)== 2:
				iguales= self.hand.pop(self.hand.index(number))
				self.hand.remove(iguales)
				residuo= self.hand.pop()
				if iguales == 10 and residuo == 7:
					self.canto= "VIGIA"
					self.points= 7		
				elif residuo == 10 and iguales == 7:
					self.canto= "VIGIA"
					self.points= 7
				elif residuo + 1 == iguales or residuo - 1== iguales:
					self.canto= "VIGIA"
					self.points= 7
				return True
		return False

	def  patrulla(self):
		hand= sorted(self.hand)
		if hand[0] == 6 and hand[1] + 3== hand[2]:
			self.canto= "Patrulla"
			self.points= 6
		elif hand[0]== 7 and hand[1]+ 1== hand[2]:
			self.canto= "Patrulla"
			self.points= 6		
		elif hand[0] + 1 == hand[1] and hand[1] + 1== hand[2]:
 			self.canto = "Patrulla"
 			self.points= 6

	def check_hand(self):
		if self.trivilin():
			return self.canto, self.points
		elif self.casa_grande():
			return self.canto, self.points
		elif self.casa_chica():
			return self.canto, self.points
		elif self.patrulla():
			return self.canto, self.points
		elif self.registro():
			return self.canto, self.points
		elif self.vigia():
			return self.canto, self.points
		elif self.ronda():
			return self.canto, self.points
		else:
			return "Continue..."
		

canto = Cantos()
canto_ganador, canto_puntos = canto.check_hand()
print(canto_ganador, canto_puntos)