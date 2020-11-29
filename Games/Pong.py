import pygame, random, sys
pygame.init() # starts module

size = width, height = 900, 720 # 1440, 855 are the maximum dimensions of window
speed = [random.choice([15, 20, 21]) * random.choice([-1, 1]), random.randint(15, 25) * random.choice([-1, 1])]
ballcoord = [450, 360]
paddle1 = [25, 330]
paddle2 = [870, 330]
points1 = 0
points2 = 0
pointstowin = 5

black = 0, 0, 0
white = 255, 255, 255
# use hex codes on internet to find colors or https://htmlcolorcodes.com/

beginfont = pygame.font.Font("bit5x5.ttf", 35)
scorefont = pygame.font.Font("bit5x5.ttf", 80)
playerfont = pygame.font.Font("bit5x5.ttf", 20)
welcomefont = pygame.font.Font("bit5x5.ttf", 70)

display = pygame.display.set_mode(size)

begin = True
game = True
pygame.display.set_caption('PONG  BY: SRIRAG TATAVARTI')

while begin:
	display.fill(black)
	display.blit(welcomefont.render("WELCOME TO PONG", True, white), [90, 255])
	display.blit(beginfont.render(f"FIRST TO {pointstowin} POINTS WINS!", True, white), [195, 375])
	display.blit(beginfont.render("Press C to continue or Q to quit", True, white), [100, 475])
	display.blit(playerfont.render("Player 1", True, white), [140, 50])
	display.blit(playerfont.render("(W and S Keys)", True, white), [110, 75])
	display.blit(playerfont.render("Player 2", True, white), [640, 50])
	display.blit(playerfont.render("(UP and DOWN Keys)", True, white), [580, 75])
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

while game:
	if pygame.event.get(pygame.QUIT):
		sys.exit()
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP] and paddle2[1] - 30 >= 0:
		paddle2[1] -= 30
	if keys[pygame.K_DOWN] and paddle2[1] + 75 < height:
		paddle2[1] += 30
	if keys[pygame.K_w] and paddle1[1] - 30 >= 0:
		paddle1[1] -= 30
	if keys[pygame.K_s] and paddle1[1] + 75 < height:
		paddle1[1] += 30

	display.fill(black)
	pygame.draw.line(display, white, (450, 0), (450, 720))
	display.blit(scorefont.render(str(points1), True, white), [200, 50])
	display.blit(scorefont.render(str(points2), True, white), [655, 50])
	pygame.draw.rect(display, white, paddle1 + [5, 75])
	pygame.draw.rect(display, white, paddle2 + [5, 75])

	if ballcoord[0] >= 25 and ballcoord[0] <= 30 and ballcoord[1] <= paddle1[1] + 80 and ballcoord[1] >= paddle1[1]:
		speed[0] = -speed[0]
	elif ballcoord[0] >= 870 and ballcoord[0] <= 875 and ballcoord[1] <= paddle2[1] + 80 and ballcoord[1] >= paddle2[1]:
		speed[0] = -speed[0]
	if ballcoord[1] - 2.5 < 0 or ballcoord[1] + 2.5 > height:
		speed[1] = -speed[1]
	if ballcoord[0] - 2.5 < 0:
		game = False
		points2 += 1
	elif ballcoord[0] + 2.5 > width:
		game = False
		points1 += 1
	ballcoord[0] += speed[0]
	ballcoord[1] += speed[1]
	pygame.draw.circle(display, white, ballcoord, 5)
	pygame.display.update()
	
	while game == False:
		speed = [random.choice([15, 20, 21]) * random.choice([-1, 1]), random.randint(15, 25) * random.choice([-1, 1])]
		ballcoord = [450, 360]
		game = True
		break

	if points1 == pointstowin or points2 == pointstowin:
		loop = True
		while loop:
			display.fill(black)
			display.blit(beginfont.render(f"PLAYER {max({'1': points1, '2': points2}, key = {'1': points1, '2': points2}.get)} WINS!!", True, white), [290, 275])
			display.blit(beginfont.render("Press R to restart or Q to quit", True, white), [120, 375])
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
						sys.exit()
				if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_q:
							sys.exit()
						elif event.key == pygame.K_r:
							loop = False
							points1 = 0
							points2 = 0
							break