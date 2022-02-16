def fifth_and_sixth_task():
	'''
	5. Запросите у пользователя значения выручки и издержек фирмы.
	Определите, с каким финансовым результатом работает фирма.
	Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
	Выведите соответствующее сообщение.

	6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
	Это отношение прибыли к выручке. Далее запросите численность сотрудников
	фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
	'''

	def input_to_int(string):
		try:
			clear_value = float(string)
		except Exception as err:
			print('Вы ввели не число!')
			print('Ошибка:', err)
			return fifth_and_sixth_task()
		return clear_value

	revenue_str = input('введите объем выручки: ')
	loss_str = input('введите объем издержек: ')

	revenue = input_to_int(revenue_str)
	loss = input_to_int(loss_str)

	profit = revenue - loss
	is_profitable = profit >= 0

	if is_profitable:
		print(f'Доход составляет: {profit}')
		print(f'рентабельность выручки составляет: {profit / revenue}')
		employees_str = input('введите численность сотрудников: ')
		employees = input_to_int(employees_str)
		print(f"прибыль фирмы в расчёте на одного сотрудника, составляет: {profit / employees}")
	else:
		print(f'Убыток составляет: {profit}')
	return


if __name__ == '__main__':
	try:
		fifth_and_sixth_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
