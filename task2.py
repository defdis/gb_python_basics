def second_task():
	'''
	2. Выполнить функцию, которая принимает несколько параметров,
	описывающих данные пользователя: имя, фамилия, год рождения,
	город проживания, email, телефон. Функция должна принимать
	параметры как именованные аргументы.
	Осуществить вывод данных о пользователе одной строкой.

	:return:
	'''

	def task(name='', last_name='', year_of_birth='', city_of_residence='', email='', phone=''):
		print(f'{name} {last_name}	{year_of_birth}	{city_of_residence}	{email}	{phone}')
		return second_task()

	name = input('введите имя: ')
	last_name = input('введите фамилию: ')
	year_of_birth = input('введите год рождения: ')
	city_of_residence = input('введите город проживания: ')
	email = input('введите email: ')
	phone = input('введите телефон: ')

	task(
		name=name,
		last_name=last_name,
		year_of_birth=year_of_birth,
		city_of_residence=city_of_residence,
		email=email,
		phone=phone
	)

	return second_task()


if __name__ == '__main__':
	try:
		second_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
