casa_grande = [12, 1, 12]

def casaGrande(mano):
	if [1, 12, 12] == sorted(mano):
		print("Casa grande")
		return True
	return False

print(casaGrande(casa_grande))