from functools import reduce


def fifth_task():
	'''
	5. Реализовать формирование списка, используя функцию range()
	и возможности генератора. В список должны войти чётные числа
	от 100 до 1000 (включая границы). Нужно получить результат
	вычисления произведения всех элементов списка.
	Подсказка: использовать функцию reduce().

	'''
	print(reduce(lambda a, b: a*b, [num for num in range(100, 1001, 2)]))
	return


if __name__ == '__main__':
	try:
		fifth_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
