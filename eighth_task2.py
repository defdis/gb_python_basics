
class ZeroDivision:
	"""
	2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
	Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
	делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
	"""

	def __init__(self, divider, denominator):
		self.divider = divider
		self.denominator = denominator

	@staticmethod
	def zero_divide(divider, denominator):
		try:
			return divider / denominator
		except:
			return f"нельзя делить на ноль"

	def __str__(self):
		return f'{self.zero_divide(self.divider, self.denominator)}'


if __name__ == '__main__':
	try:
		print(ZeroDivision.zero_divide(15, 0.1))
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
