'''
функции/методы - camelCase
переменные - snake_case
константы - CAPS_CASE
'''
import pygame

hex_textures = {
	'algae':'./hex_textures/hex_algae.png',
	'aqua':'./hex_textures/hex_aqua.png',
	'blue':'./hex_textures/hex_blue.png',
	'brass':'./hex_textures/hex_brass.png',
	'brown':'./hex_textures/hex_brown.png',
	'cyan':'./hex_textures/hex_cyan.png',
	'gray':'./hex_textures/hex_gray.png',
	'green':'./hex_textures/hex_green.png',
	'ice':'./hex_textures/hex_ice.png',
	'lavender':'./hex_textures/hex_lavender.png',
	'mint':'./hex_textures/hex_mint.png',
	'orchid':'./hex_textures/hex_orchid.png',
	'purple':'./hex_textures/hex_purple.png',
	'red':'./hex_textures/hex_red.png',
	'rose':'./hex_textures/hex_rose.png',
	'whiskey':'./hex_textures/hex_whiskey.png',
	'yellow':'./hex_textures/hex_yellow.png'
}
hex_additional_textures = {
	'shadow':'./hex_textures/hex_shadow.png',
	'water':'./hex_textures/hex_water.png',
	'back':'./hex_textures/hex_background.png',
	None:'./hex_textures/hex_missing.png'
}
# переделываем все пути в текстуры списковым включением

#pygame.image.load().convert_alpha()
hex_textures = {k: pygame.image.load(v) for k, v in hex_textures.items()}
hex_additional_textures = {k: pygame.image.load(v) for k, v in hex_additional_textures.items()}
#hex_textures = [pygame.image.load(hex_textures[i]) for i in hex_textures]
#hex_additional_textures = [pygame.image.load(hex_additional_textures[i]) for i in hex_additional_textures]


class Content(object):
	"""docstring for Content"""
	def __init__(self, name:str, texture:str, center = (0, 0)):
		self.name = name
		self.texture = pygame.image.load(texture)

		self.hitbox = self.texture.get_rect()
		self.hitbox.center = center



# использует отрисовку текстурами
class Cell(object):
	"""docstring for Cell"""
	def __init__(self, center, corners, team:str = None):

		self.team = team
		# присваивание текстуры в зависимости от team, а иначе если None или невозможный ключ, то 'missing texture'
		self.texture = hex_textures.get(team, hex_additional_textures[None])
		

		# хитбокс на основе углов шестиугольника
		self.hitbox = corners # [(x, y), (x, y), (x, y), (x, y), (x, y), (x, y)]
		
		# координаты центра (черепашка)
		self.center = center # (x, y)

		

		# что внутри (человечки, деревца)
		self.content = None



	def addContent(self, name:str, texture_path:str):
		self.content = Content(name, texture_path, self.hitbox.center)

	def blit(self, screen, allow_content:bool = True, allow_hitbox:bool = False):

		h = self.texture.get_heigth()/2
		w = self.texture.get_width()/2

		x = self.center[0] - h
		y = self.center[1] - w

		screen.blit(self.texture, (x, y))

		if allow_hitbox:
			pygame.draw.polygon(screen, (255, 0, 0), self.corners, 3)

		if self.content and allow_content:
			screen.blit(self.content.texture, self.content.hitbox)

	
	def getTeamsList():
		return hex_textures.keys()


# старая не используемая технология отрисовки математикой
class CellColor(object):
	"""docstring for Cell"""
	def __init__(self, center, corners, team=None):

		#self.number = number # (column, row)
		
		# координаты центров (черепашка)
		self.center = center # (x, y)
		
		# список координат углов (список) (для расссчёта колизии)
		self.corners = corners # [(x, y), (x, y), (x, y), (x, y), (x, y), (x, y)]
		
		self.team = team


		# что внутри
		self.content = None

	def addContent(self, name:str, texture:str):

		self.content = Content(name, texture, self.center)

	def blit_color(self, screen, color, width, allow_content:bool = True):

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
