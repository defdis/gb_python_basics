import random


def fifth_task():
	'''
	5. Создать (программно) текстовый файл, записать в него программно набор чисел,
	разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
	'''

	with open('fifth_task.txt', "a") as file:
		list_num = (str(random.randrange(1, 100)) for i in range(1, 10))
		res_str = ' '.join(list(list_num)) + ' '
		file.write(res_str)

	with open('fifth_task.txt', "r") as file_read:
		line_sum = 0
		for file_str_line in file_read.readlines():
			for num in file_str_line.split(' '):
				if num:
					line_sum += int(num)
		print(f'сумма чисел в файле: {line_sum}')
	return


if __name__ == '__main__':
	try:
		fifth_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
