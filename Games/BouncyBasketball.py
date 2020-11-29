import pygame, sys
pygame.init() # starts module

size = width, height = 1000, 750 # 1440, 855 are the maximum dimensions of window
speed = [40, 40]
color = 173, 216, 230 # light blue
# use hex codes on internet to find colors

display = pygame.display.set_mode(size)

basketball = pygame.image.load("basketball.png")
ballrect = basketball.get_rect()
# finds pixel dimensions of image

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	ballrect = ballrect.move(speed)

	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]

	display.fill(color)
	display.blit(basketball, ballrect)
	pygame.display.flip()
