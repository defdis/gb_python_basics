def first_task():
	'''
	1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта
	заработной платы сотрудника. Используйте в нём формулу:
	(выработка в часах*ставка в час) + премия.
	Во время выполнения расчёта для конкретных значений
	необходимо запускать скрипт с параметрами.
	'''

	def payroll_accounting(productivity: float, hourly_rate: float, award: float):
		payroll = (productivity * hourly_rate) + award
		print(f'ЗП составляет: {payroll}')
		return payroll

	input_productivity = input('введите выработку в часах: ')
	input_hourly_rate = input('введите ставку в час: ')
	input_award = input('введите сумму премии: ')

	try:
		payroll_accounting(float(input_productivity), float(input_hourly_rate), float(input_award))
	except Exception as err:
		print('Вы ввели не число!')
		print('Ошибка:', err)
	return first_task()


if __name__ == '__main__':
	try:
		first_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
