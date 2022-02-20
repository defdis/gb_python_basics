def first_task():
	'''
		Создать список и заполнить его элементами различных типов данных.
		Реализовать скрипт проверки типа данных каждого элемента. Использовать
		функцию type() для проверки типа. Элементы списка можно не запрашивать
		у пользователя, а указать явно, в программе.

		:return: list item type
		'''
	chaotic_list = [
		"String", 12,
		[4, 'xyz'],
		(12, 32),
		('255', '255', '255'),
		'22',
		{'name': 'Вася', "age": 22},
		[item for item in range(0, 1023, 2)],
		None
	]

	for item in chaotic_list:
		print(f"item type::{type(item)}, item:: {item}")

	return

if __name__ == '__main__':
	try:
		first_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
