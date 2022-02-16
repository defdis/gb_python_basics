def fourth_task():
	'''
	Пользователь вводит целое положительное число.
	Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
	'''

	number = input('введите любое целое положительное число: ')

	try:
		clear_input = int(number)
		if clear_input < 1:
			print('число должно быть положительное')
			return fourth_task()
	except Exception as err:
		print('Вы ввели не число!')
		print('Ошибка:', err)
		return fourth_task()

	biggest_number = 0

	while clear_input:
			digit = clear_input % 10
			if biggest_number < digit:
				biggest_number = digit
			clear_input = clear_input // 10

	print(f'самая большая цифра в числе {biggest_number}')
	return f'самая большая цифра в числе {biggest_number}'


if __name__ == '__main__':
	try:
		fourth_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
