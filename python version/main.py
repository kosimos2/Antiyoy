import classes

# основной цикл
def main():
	pole = classes.Pole()
	print(pole.grid)

	pole.generatePole(5)
	print(pole.grid)







# точка входа
if __name__ == '__main__':
	main()