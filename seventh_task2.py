from abc import ABC, abstractmethod


class Clothes(ABC):
	"""
	2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
	Основная сущность (класс) этого проекта — одежда, которая может иметь определённое
	название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
	одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут
	быть обычные числа: V и H, соответственно.

	Для определения расхода ткани по каждому типу одежды использовать формулы:
	для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих
	методов на реальных данных.

	Реализовать общий подсчет расхода ткани. Проверить на практике полученные
	на этом уроке знания: реализовать абстрактные классы для основных классов
	проекта, проверить на практике работу декоратора @property.
	"""

	_fabric_consumption_count = 0

	@abstractmethod
	def fabric_consumption(self):
		pass


class Overcoat(Clothes):
	def __init__(self, size):
		self.size = size
		Overcoat._fabric_consumption_count += self.fabric_consumption

	@property
	def fabric_consumption(self):
		fabric_consumption = self.size / 6.5 + 0.5
		return float(f'{fabric_consumption:.02f}')


class Suit(Clothes):
	def __init__(self, rise):
		self.rise = rise
		Suit._fabric_consumption_count += self.fabric_consumption

	@property
	def fabric_consumption(self):
		fabric_consumption = self.rise * 2 + 0.3
		return float(f'{fabric_consumption:.02f}')


if __name__ == '__main__':
	try:
		s = Suit(rise=1.8)
		c = Overcoat(size=50)
		print("Suit fabric consumption:", s.fabric_consumption)
		print("Overcoat fabric consumption:", c.fabric_consumption)
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
