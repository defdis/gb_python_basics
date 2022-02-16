def second_task():
	'''
	Пользователь вводит время в секундах. Переведите время в часы,
	минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
	:return str:: чч:мм:сс:
	'''

	clear_input = 0
	input_sec = input('введите любое количевство секунд: ')
	try:
		clear_input = int(input_sec)
	except Exception as err:
		print('Вы ввели не число!')
		print('Ошибка:', err)
		return second_task()

	hours = clear_input // 3600
	minutes = (clear_input % 3600) // 60
	seconds = (clear_input % 3600) % 60


if __name__ == '__main__':
	try:
		second_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
