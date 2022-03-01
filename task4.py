import math


def fourth_task():
	'''
	4. Программа принимает действительное положительное число x и целое
	отрицательное число y. Выполните возведение числа x в степень y.
	Задание реализуйте в виде функции my_func(x, y). При решении
	задания нужно обойтись без встроенной функции возведения числа в степень.
	'''

	param1 = input('введите действительное положительное число x: ')
	param2 = input('введите целое отрицательное число y: ')
	try:
		param1 = float(param1)
		param2 = int(param2)
	except Exception as err:
		print('недопустимые значения')
	if param1 <= 0:
		print('x должно быть больше 0')
	elif param2 >= 0:
		print('y должно быть отрицательным')
	else:
		result = math.pow(param1, param2)
		print('x**y=', result)
	return fourth_task()


if __name__ == '__main__':
	try:
		fourth_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
