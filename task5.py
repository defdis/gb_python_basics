def fifth_task(sum=0):
	'''
	5. Программа запрашивает у пользователя строку чисел,
	разделённых пробелом. При нажатии Enter должна выводиться сумма чисел.
	Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
	Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

	Но если вместо числа вводится специальный символ, выполнение программы завершается.
	Если специальный символ введён после нескольких чисел,
	то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
	'''
	exit_flag = False
	input_num_row = input('введите строку чисел, разделённых пробелом: ')
	if len(input_num_row) and not input_num_row[0].isdigit() and not input_num_row[0].isalpha():
		print('Сумма:', sum)
		exit()
	try:
		clear__num_row = input_num_row.split(' ')
		for num in clear__num_row:
			if num.isalpha():
				pass
			elif num.isdigit():
				sum += float(num)
			else:
				exit_flag = True

	except Exception as err:
		print('Вы ввели не числа!')
		print('Ошибка:', err)
	print('Сумма:', sum)
	if exit_flag:
		exit()
	return fifth_task(sum=sum)


if __name__ == '__main__':
	try:
		fifth_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
