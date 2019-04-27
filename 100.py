def ciclo():
	x = 1
	while x < 1000:
		x = x + 1
		print(x)
		if x == 100 or x == 200 or x == 300 or x == 400 or x == 500 or x == 600 or x == 700 or x == 800 or x == 900:
			seguir = input("Desea seguir el conteo? ")
			if seguir.lower() == "si":
				print(x)
			elif seguir.lower() == "no":
				print("****************************************************")
				print("Programa finalizado.")
				print("****************************************************")
				break
			elif seguir.lower() != "si" or "no":
				print("****************************************************")
				print("No existe esa opcion, intente de nuevo")
				print("****************************************************")
				break


ciclo()		