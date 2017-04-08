vigia = [10, 9, 10]

for cartas in vigia:
	if vigia.count(cartas) == 2:
		iguales= vigia.pop(vigia.index(cartas))
		vigia.remove(iguales)
		residuo= vigia.pop()
		if residuo + 1== iguales:
			print("ESTA MIELDA ES VIGIA menor")
		elif iguales + 1== residuo:
			print("ESTA MIELDA ES VIGIA mayor")