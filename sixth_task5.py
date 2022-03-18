import random

'''
5. Реализовать класс Stationery (канцелярская принадлежность).

определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

'''


class Stationery:
	_title = ''

	@staticmethod
	def draw():
		print("«Запуск отрисовки чем-то»")


class Pen(Stationery):
	_title = 'ручка'

	@staticmethod
	def draw():
		print("«Запуск отрисовки ручкой»")


class Pencil(Stationery):
	_title = 'карандаш'

	@staticmethod
	def draw():
		print("«Запуск отрисовки карандашом»")


class Handle(Stationery):
	_title = 'маркер'

	@staticmethod
	def draw():
		print("«Запуск отрисовки маркером»")


if __name__ == '__main__':
	try:
		pen = Pen()
		pencil = Pencil()
		handle = Handle()
		pen.draw()
		pencil.draw()
		handle.draw()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
