from itertools import count, cycle


def sixth_task():
	'''
	6. Реализовать два небольших скрипта:
	итератор, генерирующий целые числа, начиная с указанного;
	итератор, повторяющий элементы некоторого списка, определённого заранее.

	Подсказка: используйте функцию count() и cycle() модуля itertools.
	Обратите внимание, что создаваемый цикл не должен быть бесконечным.
	Предусмотрите условие его завершения. #### Например, в первом задании
	выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
	Вторым пунктом необходимо предусмотреть условие,
	при котором повторение элементов списка прекратится.
	'''

	def first_iterator():
		start_num = input('укажите начало итератора (число)')
		try:
			start_num = int(start_num)
		except Exception as err:
			print('укажите число!')
			sixth_task()

		iterator = (count(start=start_num))

		for idx in range(10):
			val = next(iterator)
			print(val)
			if val == 10:
				break

	def second_iterator():
		print('для выхода введите q')
		list_num = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
		iterator = cycle(list_num)
		exit_flag = False
		while exit_flag != 'q':
			print(next(iterator), end='')
			exit_flag = input()

	first_iterator()
	second_iterator()
	return


if __name__ == '__main__':
	try:
		sixth_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
