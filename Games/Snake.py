import pygame, random, sys, time
pygame.init() # starts module

size = width, height = 600, 600 # 1440, 855 are the maximum dimensions of window
sqsize = 20
snake = [[40, 400]]
rate = 20
speed = [rate, 0]
foodsize = 10
foodloc = [random.randrange(1, int(width / sqsize)) * sqsize + (sqsize/4), random.randrange(1, int(height / sqsize)) * sqsize + (sqsize/4)]

scorefont = pygame.font.SysFont("comicsansms", 40)

high = 0

lightblue = 173, 216, 250
black = 0, 0, 0
red = 255, 0, 0
yellow = 255, 255, 0
blue = 110, 145, 232
white = 255, 255, 255
lightgreen = 169, 242, 142
# use hex codes on internet to find colors or https://htmlcolorcodes.com/

display = pygame.display.set_mode(size)

begin = True
game = True
replay = True
pygame.display.set_caption('SNAKE  BY: SRIRAG TATAVARTI')

while begin:
	display.fill(lightgreen)
	display.blit(scorefont.render("WELCOME TO SNAKE", True, white), [160, 200])
	display.blit(scorefont.render("Press C to continue or Q to quit", True, white), [100, 300])
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
				sys.exit()
		if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
				elif event.key == pygame.K_c:
					begin = False
					break
while replay:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				speed = [-abs(rate), 0]
			elif event.key == pygame.K_RIGHT:
				speed = [abs(rate), 0]
			elif event.key == pygame.K_UP:
				speed = [0, -abs(rate)]
			elif event.key == pygame.K_DOWN:
				speed = [0, abs(rate)]

	display.fill(lightgreen)
	display.blit(scorefont.render(f"Your Score: {len(snake) - 1}", True, white), [10, 10])
	display.blit(scorefont.render(f"High Score: {high}", True, white), [10, 50])

	if snake[-1][0] == foodloc[0] - (sqsize/4) and snake[-1][1] == foodloc[1] - (sqsize/4):
		snake.insert(0, list(snake[-1]))
		while True:
			count = 0
			foodloc[0] = random.randrange(1, int(width / sqsize)) * sqsize + (sqsize/4)
			foodloc[1] = random.randrange(1, int(height / sqsize)) * sqsize + (sqsize/4)
			for i in snake:
				if i != [foodloc[0] - (sqsize/4), foodloc[1] - (sqsize/4)]:
					count += 1
			if count == len(snake):
				break
	pygame.draw.rect(display, red, foodloc + [foodsize, foodsize])

	for i in range(len(snake) - 1):
		snake[i] = list(snake[i + 1])

	for i in snake:
		if [snake[-1][0] + speed[0], snake[-1][1] + speed[1]] == i:
			game = False
	snake[-1][0] += speed[0]
	snake[-1][1] += speed[1]
	for i in snake:
		alt = snake.index(i)
		if len(snake) % 2 == 0:
			alt += 1
		if alt % 2 == 0:
			pygame.draw.rect(display, black, i + [sqsize, sqsize])
		else:
			pygame.draw.rect(display, blue, i + [sqsize, sqsize])

	if snake[-1][0] - sqsize/2 < 0 or snake[-1][0] + sqsize/2 > width or snake[-1][1] - sqsize/2 < 0 or snake[-1][1] + sqsize/2 > height:
		game = False

	pygame.display.update()
	time.sleep(.03)

	while game == False:
		display.blit(scorefont.render("Press R to restart or Q to quit", True, white), [100, 300])
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
				elif event.key == pygame.K_r:
					if len(snake) - 1 > high:
						high = len(snake) - 1
					snake = [[40, 400]]
					speed = [abs(rate), 0]
					foodloc = [random.randrange(1, int(width / sqsize)) * sqsize + (sqsize/4), random.randrange(1, int(height / sqsize)) * sqsize + (sqsize/4)]
					game = True
					break