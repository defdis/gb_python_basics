def sixth_task(goods=[]):
	'''
		* Реализовать структуру данных «Товары».
		Она должна представлять собой список кортежей.
		Каждый кортеж хранит информацию об отдельном товаре.
		В кортеже должно быть два элемента — номер товара и
		словарь с параметрами, то есть характеристиками
		товара: название, цена, количество, единица измерения.
		Структуру нужно сформировать программно, запросив все данные у пользователя.
		Пример готовой структуры: [
			(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
			(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
			(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
		]
	'''

	def num_check(value):
		try:
			clear_input = int(value)
			return clear_input
		except Exception as err:
			print('Вы ввели не число!')
			print('Ошибка:', err)
			return sixth_task(goods)

	print('заполните карточку товара!')
	input_name = input('введите название товара: ')
	input_price = num_check(input('введите цену товара: '))
	input_quantity = num_check(input('введите количество товара: '))
	input_unit = input('введите единицу измерения товара: ')
	goods.append(
		(len(goods) + 1, {
			'название': input_name,
			'цена': input_price,
			'количество': input_quantity,
			'eд': input_unit
		})
	)
	print([item for item in goods])
	analytics = {
		'название': [item[1].get('название') for item in goods],
		'цена': [item[1].get('цена') for item in goods],
		'количество': [item[1].get('количество') for item in goods],
		'eд': [item[1].get('eд') for item in goods]
	}
	print('аналитика: ', analytics)
	return sixth_task(goods)


if __name__ == '__main__':
	try:
		sixth_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
