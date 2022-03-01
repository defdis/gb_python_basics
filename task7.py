from math import factorial


def sixth_task():
	'''
	7. Реализовать генератор с помощью функции с ключевым словом yield,
	создающим очередное значение. При вызове функции должен создаваться
	объект-генератор. Функция вызывается следующим образом: for el in fact(n).
	Она отвечает за получение факториала числа.
	В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

	Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
	'''

	def fact(n):
		for i in range(n):
			yield f'{i+1}! = {factorial(i+1)}'

	try:
		inp_n = int(input('введите n: '))
		for el in fact(inp_n):
			print(el)
	except Exception as err:
		print('введите число!')
	return sixth_task()


if __name__ == '__main__':
	try:
		sixth_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
