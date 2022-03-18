'''
3. Реализовать базовый класс Worker (работник).

определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени
сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры
класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''


class Worker:
	_income = {}

	def __init__(self, name: str = '', surname: str = '', position: str = '', wage: int = 0, bonus: int = 0):
		self.name = name
		self.surname = surname
		self.position = position
		self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
	def __init__(self, name: str = '', surname: str = '', position: str = '', wage: int = 0, bonus: int = 0):
		super().__init__(name, surname, position, wage, bonus)

	def get_full_name(self):
		return f'{self.name} {self.surname}'

	def get_total_income(self):
		total = 0

		for key, val in self._income.items():
			total += val
		return total


list_of_data = [
	{
		"name": 'Егор',
		"surname": 'Васильев',
		"position": 'директор',
		"wage": 125000,
		"bonus": 15000,

	},
	{
		"name": 'Николай',
		"surname": 'Пётров',
		"position": 'бухгалтер',
		"wage": 74000,
		"bonus": 9600,
	},
	{
		"name": 'Пётр',
		"surname": 'Николаев',
		"position": 'разработчик',
		"wage": 82000,
		"bonus": 5800,
	},
	{
		"name": 'Василий',
		"surname": 'Егоров',
		"position": 'курьер',
		"wage": 34500,
		"bonus": 15400,
	},
]


if __name__ == '__main__':
	try:
		for worker in map(lambda obj: Position(**obj), list_of_data):
			print(f'{worker.get_full_name()} - {worker.position} : {worker.get_total_income()}')
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
