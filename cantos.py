#CASA GRANDE

casa_grande = [12, 1, 12]

def casaGrande(mano):
	if [1, 12, 12] == sorted(mano):
		print("Casa grande")
		return True
	return False

# print(casaGrande(casa_grande))

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

print(ronda(ronda_mano))

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