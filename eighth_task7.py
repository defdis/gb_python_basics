
class ComplexNumber:
	"""

	7. Реализовать проект «Операции с комплексными числами».
	Создайте класс «Комплексное число». Реализуйте перегрузку
	методов сложения и умножения комплексных чисел. Проверьте
	работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
	выполните сложение и умножение созданных экземпляров. Проверьте корректность
	полученного результата.

	"""

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		print(f'Сложение комплексных чисел')
		return f'x = {self.x + other.x} + {self.y + other.y}i'

	def __mul__(self, other):
		print(f'Умножение комплексных чисел')
		return f'x = {(self.x * other.x) + (self.y * other.y * -1)} + {self.x * other.y + self.y * other.x}i'

	def __str__(self):
		return f'x = {self.x} + {self.y} * i'


if __name__ == '__main__':
	try:
		x1 = ComplexNumber(1, -2)
		x2 = ComplexNumber(3, 4)
		print(x1 + x2)
		print(x1 * x2)

		x3 = ComplexNumber(5, 4)
		x4 = ComplexNumber(3, 2)
		print(x3 + x4)
		print(x3 * x4)
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
