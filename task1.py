def first_task():
	'''
	1. Создать программный файл в текстовом формате,
	записать в него построчно данные, вводимые пользователем.
	Об окончании ввода данных будет свидетельствовать пустая строка.
	'''

	ipt = input('введите новую строку: ')
	if ipt:
		with open('first_task.txt', 'a') as file:
			file.write(ipt + '\n')
	else:
		exit()
	return first_task()


if __name__ == '__main__':
	try:
		first_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
