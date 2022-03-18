import time
import os


class TrafficLight:
	'''
	определить у него один атрибут color (цвет) и метод running (запуск);
	атрибут реализовать как приватный;
	в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
	продолжительность первого состояния (красный) составляет 7 секунд,
	второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
	переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
	проверить работу примера, создав экземпляр и вызвав описанный метод.
	'''
	__color = "red"

	def __init__(self):
		os.system("clear")
		self.color = self.__color

	@staticmethod
	def light_on():
		ret_str = '      (ooo)      \n'\
				  '  (ooooooooooo)  \n'\
				  '(ooooooooooooooo)\n' \
				  '(ooooooooooooooo)\n' \
				  '  (ooooooooooo)  \n' \
				  '      (ooo)     '
		print(ret_str)

	@staticmethod
	def light_off():
		ret_str = '      (   )     \n'\
				  '  (           )  \n'\
				  '(               )\n' \
				  '(               )\n' \
				  '  (           )  \n' \
				  '      (   )     '
		print(ret_str)

	def light_red(self):
		self.color = "red"
		self.light_on()
		self.light_off()
		self.light_off()
		print(f'Traffic light collor {self.color}')
		time.sleep(7)

	def light_yellow(self):
		self.color = "yellow"
		self.light_off()
		self.light_on()
		self.light_off()
		print(f'Traffic light collor {self.color}')
		time.sleep(2)

	def light_green(self):
		self.color = "green"
		self.light_off()
		self.light_off()
		self.light_on()
		print(f'Traffic light collor {self.color}')
		time.sleep(7)

	def running(self):
		self.light_red()
		os.system("cls||clear")
		self.light_yellow()
		os.system("cls||clear")
		self.light_green()
		os.system("cls||clear")
		return


if __name__ == '__main__':
	try:
		tr_light = TrafficLight()
		tr_light.running()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
