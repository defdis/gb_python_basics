def third_task():
	'''
	Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
	Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
	'''

	clear_input = 0
	n = input('введите любое чесло: ')

	try:
		clear_input = abs(int(n))
	except Exception as err:
		print('Вы ввели не число!')
		print('Ошибка:', err)
		return third_task()

	print(f'{clear_input} + {clear_input*2} + {clear_input*3} = {clear_input + int(str(clear_input)*2) + int(str(clear_input)*3)}')
	return clear_input + int(str(clear_input)*2) + int(str(clear_input)*3)


if __name__ == '__main__':
	try:
		third_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
