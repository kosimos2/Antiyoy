'''
функции/методы - camelCase
переменные - snake_case
константы - CAPS_CASE
'''
import pygame


class Content(object):
	"""docstring for Content"""
	def __init__(self, name:str, texture:str, center = (0, 0)):
		self.name = name
		self.texture = pygame.image.load(texture)

		self.hitbox = self.texture.get_rect()
		self.hitbox.center = center


class Cell(object):
	"""docstring for Cell"""
	def __init__(self, center, corners):

		#self.number = number # (column, row)
		
		# координаты центров (черепашка)
		self.center = center # (x, y)
		
		# список координат углов (список) (чтобы рисовать стороны)
		self.corners = corners # [(x, y), (x, y), (x, y), (x, y), (x, y), (x, y)]

		# что внутри
		self.content = None

		self.belongs = None

	def addContent(self, name:str, texture:str):

		self.content = Content(name, texture, self.center)

	def blit(self, screen, color, width, allow_content:bool = True):

		pygame.draw.polygon(screen, color, self.corners, width)

		if self.content and allow_content:
			screen.blit(self.content.texture, self.content.hitbox)



class Pole(object):
	"""docstring for Pole"""
	def __init__(self, grid = None):

		self.grid = grid




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


		self.ip = ''

		
		
		

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

	def profitRelease(self):
		self.balance += self.profit






		
		

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
						



class GAME(object):
	"""docstring for GAME"""
	def __init__(self, pole, players = []):

		if isinstance(pole, Pole):
			self.pole = pole
		else:
			raise TypeError("Аргумент должен быть экземпляром класса Pole")
		
		self.players = players
		


	def addPlayer(self, pl):
		if isinstance(pl, Player):
			self.players.append(pl)
		else:
			raise TypeError("Аргумент должен быть экземпляром класса Player")
		

	def randomTree(self):
		None

	def profitUpdate(self):
		# перерасчёт дохода для всех игроков
		for i in self.players:
			i.profitUpdate()
