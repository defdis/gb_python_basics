def third_task():
	'''
	3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
	Подсказка: используйте функцию range() и генератор.
	'''

	gen = (num for num in range(20, 241) if num % 20 == 0 or num % 21 == 0)
	print(list(gen))
	return


if __name__ == '__main__':
	try:
		third_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
