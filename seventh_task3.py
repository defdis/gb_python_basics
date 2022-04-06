

class Cell:
	"""
	3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
	Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
	соответствующий количеству ячеек клетки (целое число). В классе должны быть
	реализованы методы перегрузки арифметических операторов: сложение (__add__()),
	вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
	Данные методы должны применяться только к клеткам и выполнять увеличение,
	уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

	Сложение. Объединение двух клеток. При этом число ячеек общей клетки
	должно равняться сумме ячеек исходных двух клеток.
	Вычитание. Участвуют две клетки. Операцию необходимо выполнять
	только если разность количества ячеек двух клеток больше нуля,
	иначе выводить соответствующее сообщение.
	Умножение. Создаётся общая клетка из двух. Число ячеек общей
	клетки определяется как произведение количества ячеек этих двух клеток.
	Деление. Создаётся общая клетка из двух. Число ячеек общей клетки
	определяется как целочисленное деление количества ячеек этих двух клеток.
	В классе необходимо реализовать метод make_order(),
	принимающий экземпляр класса и количество ячеек в ряду.
	Данный метод позволяет организовать ячейки по рядам.

	Метод должен возвращать строку вида *****\n*****\n*****...,
	где количество ячеек между \n равно переданному аргументу.
	Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

	Например, количество ячеек клетки равняется 12,
	количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку: *****\n*****\n**.
	Или, количество ячеек клетки равняется 15,
	количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку: *****\n*****\n*****.
	"""
	cell_box = 0

	def __init__(self, cell_box):
		self.cell_box = cell_box

	def __str__(self):
		return self.make_order(5)

	def __add__(self, other):
		return Cell(self.cell_box + other.cell_box)

	def __sub__(self, other):
		return Cell(self.cell_box - other.cell_box)

	def __mul__(self, other):
		return Cell(self.cell_box * other.cell_box)

	def __truediv__(self, other):
		return Cell(self.cell_box // other.cell_box)

	def make_order(self, row_len):
		cl = []
		for cb in range(self.cell_box):
			if len(cl) and len(cl) % row_len == 0:
				cl.append('\n*')
			else:
				cl.append('*')
		return ''.join(i for i in cl)


if __name__ == '__main__':
	try:
		cell = Cell(13)
		cell2 = Cell(15)
		cell3 = Cell(25)
		cell4 = Cell(5)
		cell5 = Cell(5)

		cell_sum = cell + cell2
		print(cell_sum)
		print('\n')
		print(cell_sum - cell3)
		print('\n')
		print(cell4 * cell5)
		print('\n')
		print(cell4 * cell5 / cell5)
	except KeyboardInterrupt:
		print('\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
