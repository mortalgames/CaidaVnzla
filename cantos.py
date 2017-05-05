#CASA GRANDE

casa_grande = [12, 1, 12]

def casaGrande(mano):
	if [1, 12, 12] == sorted(mano):
		print("Casa grande")
		return True
	return False

# print(casaGrande(casa_grande))

#CASA CHICA

casa_chica= [12, 1, 12]

def casaChica(mano):
	if [1, 1, 12] == sorted(mano):
		print("Casa Chica")
		return True
	return False

# print(casaChica(casa_chica))

#REGISTRO

registro= [15, 11, 1]

def Registro(mano):
	if [1, 11, 12] == sorted(mano):
		print("Registro")
		return True
	return False

#print(Registro(registro))

#RONDA

ronda_mano = [10, 3, 10]

def ronda(mano):
	for numero in mano:
		if mano.count(numero) == 2:
			los_iguales = mano.pop(mano.index(numero))
			if 1 <= los_iguales <= 7:
				print("1 punto bicho")
			elif los_iguales == 10:
				print("2 puntos mano")
			elif los_iguales == 11:
				print("3 puntos manuscrito")
			else:
				print("4 puntos manofactura")
			return True
	return False

# print(ronda(ronda_mano))

#TRIVILIN

trivilin_mano = [9, 9, 9]

def trivilin(mano):
	for numero in mano:
		if mano.count(numero) == 3:
			return True
	return False

# print(trivilin(trivilin_mano))

#VIGIA

vigia_mano = [9, 10, 10]

def vigia(mano):
	for cartas in mano:
		if mano.count(cartas) == 2:
			iguales= mano.pop(mano.index(cartas))
			vigia_mano.remove(iguales)
			residuo= vigia_mano.pop()
			if residuo + 1 == iguales:
				print("Esto es vigia mayor")
			elif residuo - 1 == iguales:
				print("Esto es vigia menor")
			return True
	return False

# print(vigia(vigia_mano))

#PATRULLA
cards= [7, 10, 11]
hand= sorted(cards)

def Patrulla(mano):
	if hand[0] == 6 and hand[1] + 3== hand[2]:
		return("Es Patrulla 6")
	elif hand[0]== 7 and hand[1]+ 1== hand[2]:
		return("patrulla 7")		
	elif hand[0] + 1 == hand[1] and hand[1] + 1== hand[2]:
		return("Esto es patrulla")
	else:
		return False	
#print(Patrulla(hand))