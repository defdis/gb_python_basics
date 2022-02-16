def first_task():
	'''
	1. Поработайте с переменными, создайте несколько, выведите на экран.
	Запросите у пользователя некоторые числа и строки
	и сохраните в переменные, затем выведите на экран.
	'''

	param1 = 'test'
	param2 = 30
	print(f'введите значения переменных, например: param1 => {param1}, param2 =>: {param2}')
	user_param1 = input('param1:')
	user_param2 = input('param2:')
	print(f'вы ввели: param1 => {user_param1}, param2 => {user_param2}')
	return


if __name__ == '__main__':
	try:
		first_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
