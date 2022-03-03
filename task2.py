def second_task():
	'''
	2. Создать текстовый файл (не программно),
	сохранить в нём несколько строк, выполнить
	подсчёт строк и слов в каждой строке.
	'''
	with open('second_task.txt', 'r') as file:
		rows = file.readlines()
		print(f'всего строк: {len(rows)}')
		line = 0
		for row in rows:
			line += 1
			print(f'в строке {line} {len([word for word in row.split(" ") if len(word) > 2])} слов')
	return


if __name__ == '__main__':
	try:
		second_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
