import math, pygame, random, classes
# для переводчика

def coords(raw, number, side):
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

def calculate_hexagon_sides(center, side_length, rotation = 30):
	center_x = center[0]
	center_y = center[1]


	sides = []
	angle = 60  # угол между сторонами шестиугольника

	for i in range(6):
		start_x = center_x + side_length * math.cos(math.radians(angle * i + rotation))
		start_y = center_y + side_length * math.sin(math.radians(angle * i + rotation))
		
		sides.append((float(start_x), float(start_y)))

	return sides

def generateGrid(wight:int = None, height:int = None):

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

def toHexGrid(main_coords, grid, side_length):
	
	res = []
	for row in grid:
		
		interim = []
		for i in row:

			# вычисляем координаты центра шестиугольника, зная его номер и координаты №0,0
			center = coords(main_coords, i, side_length)
			# вычисляем координаты его углов, зная координаты центра и длину стороны
			corners = calculate_hexagon_sides(center, side_length)
			# создаём экземпляр класса с заданными параметрами
			interim.append(classes.Cell(center, corners))
		res.append(interim)
	return res


def main():
	bg_menu_color = (55, 55, 55)
	WIDTH = 500  #переменная с шириной
	HEIGHT = 500 #переменная с высотой
	pygame.init() #Инициализация PyGame
	screen = pygame.display.set_mode((WIDTH, HEIGHT)) #создаём окно с размерами

	# создание
	grid = generateGrid(7, 4)
	gridHex = toHexGrid((35,35), grid, 30)

	gridHex[0][2].addContent('elka', './textures/pine_low.png')
	gridHex[3][3].addContent('palma', './textures/palm_low.png')
	gridHex[1][4].addContent('man', './textures/spearman_low.png')

	#основной цикл игры
	risuj = False
	running = True
	while running: 
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				pygame.quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE: 
					risuj = True 
		
		

		if risuj:
			screen.fill(bg_menu_color)
			

			for row in gridHex:
				for i in row:
					i.blit(screen, (253, 255, 11), 5)

			



			pygame.display.flip()
			risuj = False
				

if __name__ == '__main__':
	main()
