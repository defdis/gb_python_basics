def fourth_task():
	'''
		Пользователь вводит строку из нескольких слов, разделённых пробелами.
		Вывести каждое слово с новой строки. Строки нужно пронумеровать.
		Если слово длинное, выводить только первые 10 букв в слове.
	'''
	input_long_string = input('введите строку из нескольких слов: ')
	if len(input_long_string.split()) > 1:
		input_long_string_list = input_long_string.split()
	else:
		print('Ошибка! Необходимо ввести несколько слов!\n')
		return third_task()
	for idx, item in enumerate(input_long_string_list):
		print(idx + 1, f'{item.replace(".", "").replace(",", ""):.10s}')
	print('\n')
	return fourth_task()


if __name__ == '__main__':
	try:
		fourth_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
