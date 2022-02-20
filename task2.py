def second_task(list_to_change=[]):
	'''
		Для списка реализовать обмен значений соседних элементов.
		Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
		При нечётном количестве элементов последний сохранить на своём месте.
		Для заполнения списка элементов нужно использовать функцию input().
		:return:
	'''
	input_element = input('введите что-нибудь: ')
	list_to_change.extend(input_element.split())
	print(list_to_change)
	for idx, item in enumerate(list_to_change):
		if idx % 2:
			list_to_change[idx - 1], list_to_change[idx] = list_to_change[idx], list_to_change[idx - 1]
	print(list_to_change)
	return second_task(list_to_change)


if __name__ == '__main__':
	try:
		second_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
