
class Date:
	"""
	1. Реализовать класс «Дата», функция-конструктор которого должна принимать
	дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
	Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
	год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
	должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
	Проверить работу полученной структуры на реальных данных.
	"""

	date = ''
	day = 0
	month = 0
	year = 0

	def __init__(self, date: str):
		print(date)
		assert len(date.split('-')) > 2, 'неверный формат даты'
		self.date = date
		self.date_validate(self.date)

	@classmethod
	def date_validate(cls, date):
		print(cls.date)
		cls.day = int(date.split('-')[0])
		cls.month = int(date.split('-')[1])
		cls.year = int(date.split('-')[2])
		cls.day_month_validate(date)

	@staticmethod
	def day_month_validate(date):
		day, month, year = date.split('-')
		assert 0 < int(day) < 32, 'день даты неверен'
		assert 0 < int(month) < 13, 'месяц даты неверен'

	def __str__(self):
		return f'{self.day} {self.month} {self.year}'


if __name__ == '__main__':
	try:
		print(Date('10-10-1985'))
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
