def seventh_task():
	'''
	7. Спортсмен занимается ежедневными пробежками.
	В первый день его результат составил a километров.
	Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
	Требуется определить номер дня, на который результат спортсмена составит
	не менее b километров. Программа должна принимать
	значения параметров "a" и "b" и выводить одно натуральное число — номер дня.

	Например: a = 2, b = 3.
	Результат:
	1-й день: 2
	2-й день: 2,2
	3-й день: 2,42
	4-й день: 2,66
	5-й день: 2,93
	6-й день: 3,22
	Ответ: на шестой день спортсмен достиг результата — не менее 3 км.
	:return:
	'''

	def input_to_int(string):
		try:
			clear_value = float(string)
		except Exception as err:
			print('Вы ввели не число!')
			print('Ошибка:', err)
			return seventh_task()
		return clear_value

	fitst_day_distanse_str = input('введите результат спортсмена в первый день (в километрах): ')
	fitst_day_distanse = input_to_int(fitst_day_distanse_str)
	target_distanse_str = input('введите необходимый результат спортсмена (в километрах): ')
	target_distanse = input_to_int(target_distanse_str)
	day = 1
	distanse = fitst_day_distanse
	while distanse <= target_distanse:
		distanse += (distanse * 0.1)
		day += 1
	else:
		print(f'на {day}й день спортсмен достигнет результата {target_distanse} км.')

	return


if __name__ == '__main__':
	try:
		seventh_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
