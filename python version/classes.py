'''
функции/методы - camelCase
переменные - snake_case
константы - CAPS_CASE
'''

class Player(object):
	"""docstring for Player"""

	# инициализация (активируется x = Player())
	def __init__(self, arg):
		super(Player, self).__init__() # хз что это
		
		# АТРИБУТЫ ######
		self.profit = 0 # доход
		# список с тем, что есть у игрока (просто список для рассчёта прибыли и т.д.) (элементы - экземпляры классов объектов)
		# мб сделать просто словарик с 'названием':'количесвтом' (всё равно всё храниться на карте)
		self.hold_list = []

		self.balance = 0


		self.color = (0, 0, 0)
		self.nick = 'NoName'

		
		

	def profitUpdate(self):
		# обновление (рассчёт) дохода изходя из того, что в холд листе
		None

	def addToHold(self, key:str, value = None):
		# функция добавления чего-либо в hold_list
		self.hold_list[key] = value

	def delToHold(self, key:str):
		# функция удаления чего-либо из hold_list по ключу
		res = self.hold_list.pop(key, None)
		return res # возвращает значение удалённого элемента



class Content(object):
	"""docstring for Content"""
	def __init__(self, arg):
		super(Content, self).__init__()
		self.arg = arg


class Pole(object):
	"""docstring for Pole"""
	def __init__(self, arg):
		super(Pole, self).__init__()
		self.arg = arg
		
		

'''
class Pole(object):
	"""docstring for Pole"""
	def __init__(self, pole = None):
		

		self.pole = pole
	
	def buildPole(self):
		# функция для сборки поля (или надо это делать во время инициализации пожалуй)
		None



class Cell(object):
	"""docstring for Cell
	одна ячейка поля

	"""
	def __init__(
		self, 
		container = None,
		sides = {
			1:None,
			2:None,
			3:None,
			4:None,
			5:None,
			6:None
		}):
		
		self.sides = sides
		self.belong = None # кому принадлежит => во что красить
		self.container = container # переменная в которой храниться объект содержащийся в ячейке
'''
						










