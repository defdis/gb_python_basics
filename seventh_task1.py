import time
import os


class Matrix:
	"""
	1. Реализовать класс Matrix (матрица). Обеспечить перегрузку
	конструктора класса (метод __init__()), который должен принимать
	данные (список списков) для формирования матрицы.

	Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

	Далее реализовать перегрузку метода __add__() для реализации операции
	сложения двух объектов класса Matrix (двух матриц). Результатом сложения
	должна быть новая матрица.
	"""

	def __init__(self, mtx: list):
		assert isinstance(mtx, list) and len(mtx), \
			'список должен содержать минимум два вложенных списка'
		self.matrix = mtx

	def __str__(self):
		return self.visual_normalization(self.matrix)

	def __add__(self, other):
		result_matrix = []
		for pair_row in zip(self.matrix, other):
			result_matrix.append(self.row_sum(pair_row))
		return result_matrix
		# return [result_matrix.append(self.row_sum(pair_row)) for pair_row in zip(self.matrix, other)]

	@staticmethod
	def visual_normalization(list_mtx):
		result_string = ''
		for row in list_mtx:
			for item in row:
				result_string += str(item) + '\t'
			result_string += '\n'
		return result_string

	@staticmethod
	def row_sum(row):
		list_result = []
		for idx, itm in enumerate(row[0]):
			list_result.append(row[0][idx]+row[1][idx])
		return list_result


if __name__ == '__main__':
	list_mtx = [
			[1, 2, 34, 3],
			[5, 2, 6,  4],
			[9, 4, 11, 2],
			[9, 4, 11, 2],
	]
	try:
		matrix = Matrix(list_mtx)
		print(matrix)
		mtx_sum = matrix + [
			[34, 21, 4, 3],
			[6, 43, 28, 4],
			[11, 54, 3, 2],
			[11, 54, 3, 2],
		]
		print(matrix.visual_normalization(mtx_sum))
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
