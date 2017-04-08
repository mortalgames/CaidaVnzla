vigia = [10, 9, 10]

for cartas in vigia:
	if vigia.count(cartas) == 2:
		los_iguales = vigia.pop(vigia.index(cartas))
		residuo= vigia.remove(los_iguales)
		print(vigia)