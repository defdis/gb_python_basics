from abc import ABC, abstractmethod

"""
	4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
	А также класс «Оргтехника», который будет базовым для классов-наследников.
	Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе
	определите параметры, общие для приведённых типов. В классах-наследниках реализуйте
	параметры, уникальные для каждого типа оргтехники.

	5. Продолжить работу над первым заданием. Разработайте методы,
	которые отвечают за приём оргтехники на склад и передачу в определённое
	подразделение компании. Для хранения данных о наименовании и количестве
	единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).

	6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
	вводимых пользователем данных. Например, для указания количества принтеров,
	отправленных на склад, нельзя использовать строковый тип данных.

	Подсказка: постарайтесь реализовать в проекте «Склад оргтехники»
	максимум возможностей, изученных на уроках по ООП.

"""


class OfficeEquipment(ABC):
	def __init__(self, model: str, price: int, quantity: int):
		self.model = model
		self.price = price
		self.quantity = quantity

	@abstractmethod
	def add(self):
		pass


class Printer(OfficeEquipment):

	def __init__(self, *args):
		super().__init__(*args)
		self.printing_type = 'laser'

	def add(self):
		printers = []
		for item in range(self.quantity):
			printers.append({
				'model': self.model,
				"price": self.price,
				"quantity": self.quantity,
				"printing_type": self.printing_type
			})
		return printers


class Scanner(OfficeEquipment):

	def __init__(self, *args):
		super().__init__(*args)
		self.scanner_type = 'MFU'

	def add(self):
		scanners = []
		for item in range(self.quantity):
			scanners.append({
				'model': self.model,
				"price": self.price,
				"quantity": self.quantity,
				"scanner_type": self.scanner_type})
		return scanners


class Copier(OfficeEquipment):

	def __init__(self, *args):
		super().__init__(*args)
		self.copier_type = 'digital'

	def add(self):
		copiers = []
		for item in range(self.quantity):
			copiers.append({
				'model': self.model,
				"price": self.price,
				"quantity": self.quantity,
				"copier_type": self.copier_type
			})
		return copiers


class Stock:
	max_quantity: int
	printers: list
	scanners: list
	copiers: list

	def __init__(self, max_quantity=10):
		print('Stock.__init__')
		self.max_quantity = max_quantity
		self.printers = []
		self.scanners = []
		self.copiers = []

	def store(self, instance_list, instance_type):
		print('instance_type:', instance_type, ', len:', len(self.printers) + len(self.scanners) + len(self.copiers))
		if len(self.printers) + len(self.scanners) + len(self.copiers) > self.max_quantity:
			f'\nStock is fool!\n'
		else:
			if instance_type == 1:
				self.printers.extend(instance_list)
			elif instance_type == 2:
				self.scanners.extend(instance_list)
			elif instance_type == 3:
				self.copiers.extend(instance_list)
		print(f'printers:{self.printers}, scanners:{self.scanners}, copiers:{self.copiers}')

	def __str__(self):
		return f'printers:{self.printers}, scanners:{self.scanners}, copiers:{self.copiers}'


class Office(Stock):
	money: int
	office_equipment: list


class Run:
	run_loop = True
	office = Office(15000)

	def __init__(self, stock_max_quantity=5):
		print('для выхода в любой момент напишите "stop"')
		self.stock = Stock(max_quantity=stock_max_quantity)
		self.loop()

	def check_quit(self, raw_str):
		if raw_str == 'stop':
			self.run_loop = False
		return raw_str

	def loop(self):
		if self.run_loop:
			print('\n1-принтер\n2-сканер\n3-ксерокс')
			try:
				item_type = int(self.check_quit(input('введите тип устройства: ')))
				assert item_type > 0 and item_type < 4
				if item_type == 1:
					instance = Printer
				elif item_type == 2:
					instance = Scanner
				else:
					instance = Copier

				item_name = self.check_quit(input(f'модель: '))
				item_price = int(self.check_quit(input(f'цена: ')))
				item_quantity = int(self.check_quit(input(f'количество: ')))
				item = instance(item_name, item_price, item_quantity)
				instance_list = item.add()
				self.stock.store(instance_list, item_type)
				print('added to stock\n')
				print(self.stock)
			except:
				print('\n', '-'*100)
				print('\nвведите число!\n')
				print('-'*100, '\n')
			self.loop()
		else:
			print(self.stock)
			print('exit')


if __name__ == '__main__':
	try:
		Run()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
