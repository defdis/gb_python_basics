'''
4. Реализуйте базовый класс Car.

у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
'''


class Car:

	def __init__(self, speed: int, color: str, name: str, is_police: bool):
		self.speed, self.color, self.name, self.is_police = speed, color, name, is_police

	@property
	def is_moving(self):
		return self.speed > 0

	def show_speed(self):
		if self.speed > 110:
			print("превышение скорости")
		print(f'скорость автомобиля {self.name}: {self.speed} км/ч')

	def turn(self, direction):
		print(f'автомобиль {self.name} повернул {direction}')

	def go(self, speed):
		self.speed = speed
		print(f'автомобиль {self.name} поехал')
		self.show_speed()

	def stop(self):
		self.speed = 0
		print(f'автомобиль {self.name} остановился')


class TownCar(Car):
	def show_speed(self):
		if self.speed > 60:
			print("превышение скорости")
		print(f'скорость автомобилья {self.name}: {self.speed} км/ч')


class WorkCar(Car):
	def show_speed(self):
		if self.speed > 40:
			print(f"{self.name} превышение скорости")
		print(f'скорость: {self.speed} км/ч')


class SportCar(Car):
	pass


class PoliceCar(Car):
	def __init__(self, speed: int, color: str, name: str, *args):
		super().__init__(speed, color, name, is_police=True)


list_of_cars = [
	[56, 'черный', 'VW', False],
	[75, 'зеленый', 'Lada', False],
	[86, 'белый', 'BMW', False],
	[35, 'синий', 'Skoda', True],
]

town_car = TownCar(*list_of_cars[0])
work_car = WorkCar(*list_of_cars[1])
sport_car = SportCar(*list_of_cars[2])
police_car = PoliceCar(*list_of_cars[3])


# TownCar, SportCar, WorkCar, PoliceCar;


if __name__ == '__main__':
	try:
		town_car.show_speed()
		town_car.turn('влево')
		town_car.stop()
		town_car.go(90)
		sport_car.turn('вправо')
		sport_car.stop()
		sport_car.go(150)
		police_car.show_speed()
		work_car.show_speed()
		town_car.stop()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
