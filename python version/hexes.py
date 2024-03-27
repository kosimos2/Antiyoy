import math, pygame, classes
# для переводчика

def main():
	bg_menu_color = (55, 55, 55)
	WIDTH = 500  #переменная с шириной
	HEIGHT = 500 #переменная с высотой
	pygame.init() #Инициализация PyGame
	screen = pygame.display.set_mode((WIDTH, HEIGHT)) #создаём окно с размерами

	# создание
	pole = classes.Pole(
		(35,35), # координаты нулегого шестиугольника на экране
		30, # длина стороны шестиугольника
		7, 4 # размеры поля шестиугольников
	)

	pole.grid[0][0].addContent('elka', './textures/pine_low.png')
	pole.grid[3][3].addContent('palma', './textures/palm_low.png')
	pole.grid[1][4].addContent('man', './textures/spearman_low.png')

	#основной цикл игры
	running = True
	while running: 
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				pygame.quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE: 
					risuj = True
		
		

		screen.fill(bg_menu_color)

		pole.select(pygame.mouse.get_pos())

		for row in pole.grid:
			for i in row:
				i.blit(screen, True)

		pygame.display.flip()
				

if __name__ == '__main__':
	main()
