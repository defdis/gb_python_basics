def third_task():
	'''
		Пользователь вводит месяц в виде целого числа от 1 до 12.
		Сообщить, к какому времени года относится месяц
		(зима, весна, лето, осень). Напишите решения через list и dict.
		:return: str(зима, весна, лето, осень)
	'''
	result = None
	seasons = {
		'осень': [9, 10, 11],
		'зима': [12, 1, 2],
		'весна': [3, 4, 5],
		'лето': [6, 7, 8],
	}

	input_month = input('введите номер месяца: ')
	try:
		clear_input = int(input_month)
	except Exception as err:
		print('Вы ввели не число!')
		print('Ошибка:', err)
		return third_task()

	if clear_input:
		for season, month_number_list in seasons.items():
			if clear_input in month_number_list:
				result = season
	print(result)
	return third_task()

if __name__ == '__main__':
	try:
		third_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
