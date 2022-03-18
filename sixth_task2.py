'''
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв.
метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500т.
'''


class Road:
	_length = 0
	_width = 0

	_height = 5
	_weight = 25
	mass = 0

	def __init__(self, length: int, width: int, height: int = 5, weight: int = 25):
		self._length = length
		self._width = width

		self.height = height or self._height
		self.weight = weight or self._weight
		self.mass = self.height * self.weight

	def road_weight_calculation(self):
		return self._length * self._width * self.mass

	def show_calculation(self):
		print(f'{self._width}м * {self._length}м * {self.weight}кг * {self.height}см = {int(self.road_weight_calculation()/1000)}т')


if __name__ == '__main__':
	try:
		road1 = Road(length=5000, width=20, height=5)
		road2 = Road(length=5000, width=10, height=3)
		road3 = Road(length=10000, width=50, height=1)

		road1.show_calculation()
		road2.show_calculation()
		road3.show_calculation()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
