import math, pygame, random

def coords(a:int, b:int, rad):
	x = a * (rad*2)
	y = 0
	for i in range(b):
		x += 1*rad
		y += 2*rad
	res = (x, y)
	return res

def find_rectangle_sides(radius):
    side_length = 2 * radius  # Длина стороны шестиугольника
    width = side_length * math.sqrt(3)  # Ширина прямоугольника
    length = 2 * radius + width  # Длина прямоугольника

    return length, width


def calculate_hexagon_vertices(center_x, center_y, side_length):
    vertices = []
    angle = 2 * math.pi / 6  # Угол между сторонами шестиугольника

    for i in range(6):
        x = center_x + side_length * math.cos(i * angle)
        y = center_y + side_length * math.sin(i * angle)
        vertices.append((int(x), int(y)))

    return vertices


def calculate_hexagon_sides(center_x, center_y, side_length):
    sides = []
    angle = 60  # угол между сторонами шестиугольника

    for i in range(6):
        start_x = center_x + side_length * math.cos(math.radians(angle * i))
        start_y = center_y + side_length * math.sin(math.radians(angle * i))
        end_x = center_x + side_length * math.cos(math.radians(angle * (i + 1)))
        end_y = center_y + side_length * math.sin(math.radians(angle * (i + 1)))


        sides.append((float(start_x), float(start_y), float(end_x), float(end_y)))


    return sides




bg_menu_color = (55, 55, 55)
WIDTH = 500  #переменная с шириной
HEIGHT = 500 #переменная с высотой
pygame.init() #Инициализация PyGame
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #создаём окно с размерами



center_x = WIDTH/2
center_y = HEIGHT/2
side_length = 10

hex1 = calculate_hexagon_sides(0, 0, side_length)
print(hex1)


#button = pygame.Rect(WIDTH/2 - 25, HEIGHT/2 - 15,50,30)




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
        #pygame.draw.rect(screen, (211, 211, 211), button)
        screen.fill(bg_menu_color)


        for i in hex1:
        	
        	pygame.draw.line(screen, (0, 0, 0), [i[0], i[1]], [i[2], i[3]], 5)

        pygame.display.flip()
        risuj = False
        	


print(hexagon_vertices)


