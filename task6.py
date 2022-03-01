def sixth_task():
	'''
		6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв
		и возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

		7. Продолжить работу над заданием. В программу должна попадать строка из слов,
		разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
		Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
		Используйте написанную ранее функцию int_func().

	'''

	def int_func(words_str: str):
		words_capitalized = ' '.join((word.capitalize() for word in words_str.split(' ')))
		print(words_capitalized)

	input_name = input('введите слова из маленьких латинских букв: ')
	int_func(input_name)

	return sixth_task()


if __name__ == '__main__':
	try:
		sixth_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
