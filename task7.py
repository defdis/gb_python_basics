import json


def seventh_task():
	'''
	7. Создать вручную и заполнить несколькими строками текстовый файл,
	в котором каждая строка будет содержать данные о фирме:
	название, форма собственности, выручка, издержки.

	Пример строки файла: firm_1 ООО 10000 5000.
	Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
	а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.

	Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
	а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).

	Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
	Итоговый список сохранить в виде json-объекта в соответствующий файл.

	Пример json-объекта:
	[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
	Подсказка: использовать менеджер контекста.
	'''
	all_profit = 0
	counter = 0
	profit_dict = {}
	with open('seventh_task.txt', "r") as file:
		print(f' name		 	ownership		revenue 		costs		    profit')
		print('-'*80)
		for line in file.readlines():
			name, ownership, revenue, costs = line.split()
			profit = float(revenue) - float(costs)
			profit_dict[name] = profit
			if profit > 0:  # а если 0 включать или нет, по условию не понятно?
				counter += 1
				all_profit += profit
			print(f'{name}			{ownership} 			{revenue}			{costs}			{profit}')
	average_profit_dict = {
		'average_profit': all_profit / counter
	}
	result_list = [profit_dict, average_profit_dict]
	print(result_list)
	with open('seventh_task_result.json', 'w') as wr_file:
		json.dump(result_list, wr_file, ensure_ascii=True, indent=4)

	return


if __name__ == '__main__':
	try:
		seventh_task()
	except KeyboardInterrupt:
		print('\n\nВы нажали Cntl + C\nпроцесс завершен!\n')
		exit()
