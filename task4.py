def fourth_task():
	'''
	4. Создать (не программно) текстовый файл со следующим содержимым:
	One — 1
	Two — 2
	Three — 3
	Four — 4
	Напишите программу, открывающую файл на чтение и считывающую построчно данные.
	При этом английские числительные должны заменяться на русские.
	Новый блок строк должен записываться в новый текстовый файл.
	'''

	with open('fourth_task_input.txt', "r") as file_read, open('fourth_task_output.txt', "a") as file_write:
		for row in file_read:
			f_str = row.replace('One', 'Один').replace('Two', 'Два').replace('Three', 'Три').replace('Four', 'Четыре')
			file_write.write(f_str)
	return


if __name__ == '__main__':
	try:
		fourth_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
