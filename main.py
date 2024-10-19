def main():
	print("1. Ростелеком")
	print("2. Дом.Ру")
	print("3. DonOnline")
	print("4. билайн Интернет")
	print("5. Информация")
	vibor = input('>')
	
	if vibor == "1":
		print("Возможные логины и пароли:")
		print("1) Логин: admin")
		print("Пароль: admin")
		print("2) Логин: admin1")
		print("Пароль: password")
		vibor2 = input('Продолжить [да/нет]? ')
		if vibor2 == "да":
			main()
		else:
			print("Выход...")
	
	elif vibor == "2":
		print("Возможные логины и пароли:")
		print("1) Логин: admin")
		print("Пароль: 1234")
		print("2) Логин: admin")
		print("Пароль: admin")
		vibor3 = input('Продолжить [да/нет]? ')
		if vibor3 == "да":
			main()
		else:
			print("Выход...")
	
	elif vibor == "3":
		print("Возможные логины и пароли:")
		print("1) Логин: admin")
		print("Пароль: admin")
		vibor4 = input('Продолжить [да/нет]? ')
		if vibor4 == "да":
			main()
		else:
			print("Выход...")
	
	elif vibor == "4":
		print("Возможные логины и пароли:")
		print("1) Логин: admin")
		print("Пароль: admin")
		print("2) Логин: SuperUser")
		print("Пароль: Beeline$martB0x")
		print("3) Логин: SuperUser")
		print("Пароль: SFXXXXXXXXXX (Подсказка: вместо X вставьте серийный номер сзади роутера.)")
		vibor5 = input('Продолжить [да/нет]? ')
		if vibor5 == "да":
			main()
		else:
			print("Выход...")
	
	elif vibor == "5":
		print("Создали: SG-Products")
		print("Мы не несём ответственность в случаи взлома/изменения пароля роутера.")
		vibor6 = input('Продолжить [да/нет]? ')
		if vibor6 == "да":
			main()
		else:
			print("Выход...")
	
	else:
		print("?")
		main()

main()
