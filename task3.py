def third_task():
	'''
	3. Реализовать функцию my_func(), которая принимает три позиционных
	аргумента и возвращает сумму наибольших двух аргументов.
	'''

	def my_func(a: float, b: float, c: float) -> float:
		list_val = [a, b, c]
		print(list_val)
		first_max = max(list_val)
		list_val.remove(first_max)
		second_max = max(list_val)
		print(f'{first_max} + {second_max} = {first_max + second_max} ')
		return first_max + second_max
	first = input('введите число "а": ')
	second = input('введите число "b": ')
	third = input('введите число "c": ')
	try:
		my_func(float(first), float(second), float(third))
	except Exception as err:
		print('введите число! ::', err)
	return third_task()


if __name__ == '__main__':
	try:
		third_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
