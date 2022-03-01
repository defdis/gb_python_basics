def first_task():
	'''
	1. Реализовать функцию, принимающую два числа (позиционные аргументы)
	и выполняющую их деление. Числа запрашивать у пользователя,
	предусмотреть обработку ситуации деления на ноль.
	:return: list item type
	'''

	def clean_inpun_val(value):
		try:
			clear_input = float(value)
		except Exception as err:
			print('Вы ввели не число!')
			print('Ошибка:', err)
			clear_input = value
		return clear_input

	def division(a, b):
		try:
			return a/b
		except ZeroDivisionError:
			print("на ноль делить нельзя")
		return first_task()

	input_divisible = input('введите делимое (число): ')
	input_divider = input('введите делитель (число): ')
	value_divisible = clean_inpun_val(input_divisible)
	value_divider = clean_inpun_val(input_divider)
	print(division(value_divisible, value_divider))
	return first_task()


if __name__ == '__main__':
	try:
		first_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
