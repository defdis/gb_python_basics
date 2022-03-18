def sixth_task():
	'''
	6. Сформировать (не программно) текстовый файл.
	В нём каждая строка должна описывать учебный предмет и наличие лекционных,
	практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
	Необязательно, чтобы для каждого предмета были все типы занятий.

	Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

	Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
	Физика: 30(л) — 10(лаб)
	Физкультура: — 30(пр) —
	Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
	'''
	discipline_dict = {}

	with open('sixth_task.txt', 'r') as file:
		for line in file.readlines():
			discipline = line.split(":")[0]
			hours = 0
			for i in line.split(":")[1].split():
				num_str = ''
				for symbol in i:
					if symbol.isnumeric():
						num_str += symbol
				if num_str:
					print(num_str)
					hours += int(num_str)
			discipline_dict[discipline] = hours

	print(discipline_dict)
	return


if __name__ == '__main__':
	try:
		sixth_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
