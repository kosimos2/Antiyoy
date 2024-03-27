'''
функции/методы - camelCase
переменные - snake_case
константы - CAPS_CASE
'''
import pygame, math

def load_textures(root, rotation = 30):

	hex_textures = {
		'algae':f'{root}/hex_algae.png',
		'aqua':f'{root}/hex_aqua.png',
		'blue':f'{root}/hex_blue.png',
		'brass':f'{root}/hex_brass.png',
		'brown':f'{root}/hex_brown.png',
		'cyan':f'{root}/hex_cyan.png',
		'gray':f'{root}/hex_gray.png',
		'green':f'{root}/hex_green.png',
		'ice':f'{root}/hex_ice.png',
		'lavender':f'{root}/hex_lavender.png',
		'mint':f'{root}/hex_mint.png',
		'orchid':f'{root}/hex_orchid.png',
		'purple':f'{root}/hex_purple.png',
		'red':f'{root}/hex_red.png',
		'rose':f'{root}/hex_rose.png',
		'whiskey':f'{root}/hex_whiskey.png',
		'yellow':f'{root}/hex_yellow.png'
	}
	hex_additional_textures = {
		'shadow':f'{root}/hex_shadow.png',
		'water':f'{root}/hex_water.png',
		'back':f'{root}/hex_background.png',
		None:f'{root}/hex_missing.png'
	}


	# переделываем все пути в текстуры списковым включением

	#pygame.image.load().convert_alpha()
	hex_textures = {k: pygame.image.load(v) for k, v in hex_textures.items()}
	hex_additional_textures = {k: pygame.image.load(v) for k, v in hex_additional_textures.items()}
	#hex_textures = [pygame.image.load(hex_textures[i]) for i in hex_textures]
	#hex_additional_textures = [pygame.image.load(hex_additional_textures[i]) for i in hex_additional_textures]

	# поворот всех текстур на 30 градусов
	hex_textures = {k: pygame.transform.rotate(v, rotation) for k, v in hex_textures.items()}
	hex_additional_textures = {k: pygame.transform.rotate(v, rotation) for k, v in hex_additional_textures.items()}

	return hex_textures, hex_additional_textures

hex_textures, hex_additional_textures = load_textures('./hex_textures')

class Content(object):
	"""docstring for Content"""
	def __init__(self, name:str, texture:str, center = (0, 0)):
		self.name = name
		self.texture = pygame.image.load(texture)

		self.hitbox = self.texture.get_rect()
		self.hitbox.center = center

class Cell(object):
	"""docstring for Cell"""
	def setTexture(self, team):
		# поиск текстуры в обоих словарях
		texture = hex_textures.get(team, None)
		texture2 = hex_additional_textures.get(team, None)

		if texture:
			self.texture = texture 
		elif texture2:
			self.texture = texture2
		else:
			self.texture = hex_additional_textures[None]


	def __init__(self, center, corners, team:str = 'back'):

		self.team = team
		# присваивание текстуры в зависимости от team, а иначе если None или невозможный ключ, то 'missing texture'

		self.setTexture(self.team)
		print("выдали текстуру команды", team, f"({self.texture})")
		

		# хитбокс на основе углов шестиугольника
		self.hitbox = corners # [(x, y), (x, y), (x, y), (x, y), (x, y), (x, y)]
		
		# координаты центра (черепашка)
		self.center = center # (x, y)

		

		# что внутри (человечки, деревца)
		self.content = None

	def regenTexture(self):
		self.setTexture(self.team)

	def setTeam(self, team, change_texture:bool = True):
		self.team = team

		if change_texture:
			self.regenTexture()

	def addContent(self, name:str, texture_path:str):
		self.content = Content(name, texture_path, self.center)

	def blit(self, screen, allow_hitbox:bool = False, allow_content:bool = True):

		h = self.texture.get_height()/2
		w = self.texture.get_width()/2

		x = self.center[0] - h
		y = self.center[1] - w

		screen.blit(self.texture, (x, y))

		if allow_hitbox:
			pygame.draw.polygon(screen, (255, 0, 0), self.hitbox, 2)

		if self.content and allow_content:
			screen.blit(self.content.texture, self.content.hitbox)

	
	def getTeamsList():
		return hex_textures.keys()


	# мб перевести на Cython
	def collideHex(self, point):
	    #center_x = sum(x for x, _ in hexagon) / len(hexagon)
	    #center_y = sum(y for _, y in hexagon) / len(hexagon)

	    #center_x = self.center[0]
	    #center_y = self.center[1]
	    hexagon = self.hitbox

	    x = point[0]
	    y = point[1]

	    inside = False
	    j = len(hexagon) - 1
	    for i in range(len(hexagon)):
	        if (hexagon[i][1] > y) != (hexagon[j][1] > y) and \
	                x < (hexagon[j][0] - hexagon[i][0]) * (y - hexagon[i][1]) / \
	                (hexagon[j][1] - hexagon[i][1]) + hexagon[i][0]:
	            inside = not inside
	        j = i

	    return inside

class Pole(object):
	"""docstring for Pole"""
	def __generateGrid(self, wight:int = None, height:int = None):

		if height is None and wight is None:
			raise Exception("Высота и ширина не могут быть одновременно пустыми!")
		elif height is None:
			height = wight
		elif wight is None:
			wight = height

		# генерация
		grid = []
		for h in range(height):
			interim = []
			for w in range(wight):
				interim.append((w,h))
			grid.append(interim)

		return grid

	def __coords(self, raw, number, side):
		raw_x = raw[0]
		raw_y = raw[1]

		a = number[0]
		b = number[1]


		# вычисляем радиус зная сторону
		rad = (side * math.sqrt(3)) / 2

		# вычисляем x зная радиус и номер ячейки
		x = (rad*2) * a + raw_x
		# поправляем если это нечётная строка
		if b % 2 != 0:
			x += rad


		gipotenusa = rad * 2
		katet = rad
		# вычисляем y через теорему пифагора
		y = (math.sqrt(gipotenusa**2 - katet**2)) * b +raw_y
		

		res = (x, y)
		return res


	def __calculate_hexagon_sides(self, center, side_length, rotation = 30):
		center_x = center[0]
		center_y = center[1]


		sides = []
		angle = 60  # угол между сторонами шестиугольника

		for i in range(6):
			start_x = center_x + side_length * math.cos(math.radians(angle * i + rotation))
			start_y = center_y + side_length * math.sin(math.radians(angle * i + rotation))
			
			sides.append((float(start_x), float(start_y)))

		return sides



	def __toHexGrid(self, main_coords, grid, side_length):
		res = []
		for row in grid:
			
			interim = []
			for i in row:

				# вычисляем координаты центра шестиугольника, зная его номер и координаты №0,0
				center = self.__coords(main_coords, i, side_length)
				# вычисляем координаты его углов, зная координаты центра и длину стороны
				corners = self.__calculate_hexagon_sides(center, side_length)
				# создаём экземпляр класса с заданными параметрами
				interim.append(Cell(center, corners))
			res.append(interim)
		return res
	
	def __init__(self, zeros_coords, side_length, wight:int = None, height:int = None):

		grid = self.__generateGrid(wight, height)
		grid = self.__toHexGrid(zeros_coords, grid, side_length)
		self.grid = grid


		self.selected = (None, None)
		self.__last_selected = self.selected

	# мб перевести на Cython
	# функция возвращает координаты шестиугольника на сетке, соприкасающегося с точкой
	def collideHexes(self, point):
		for n, row in enumerate(self.grid):
			for n2, i in enumerate(row):

				if i.collideHex(point):
					return n, n2
		return None, None
	
	# функция опредляет выбранный шестиугольник, с помощью collideHexes
	def select(self, point):

		# определяем на какой навелись
		select_x, select_y = self.collideHexes(point)
		last_x = self.__last_selected[0]
		last_y = self.__last_selected[1]

		# если прошлая была другая
		if (select_x != last_x or select_y != last_y):

			if last_x != None and last_y != None:
				self.grid[last_x][last_y].regenTexture()
			
			if select_x != None and select_y != None:
				self.grid[select_x][select_y].setTexture('shadow')
			
			#print("\nнавелись на", (select_x, select_y))
			#print("перестали наводиться на", (last_x, last_y))

			self.selected = (select_x, select_y)
			self.__last_selected = (select_x, select_y)

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
