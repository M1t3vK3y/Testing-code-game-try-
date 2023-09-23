import pygame
import random

pygame.init()

ventana=pygame.display.set_mode((660,480))

pygame.display.set_caption("ejemplo 1")

ball=pygame.image.load("ball.png")

ballrect=ball.get_rect()

speed=[0,0]


bate=pygame.image.load("bate.png")
baterect=bate.get_rect()
baterect.move_ip((ventana.get_width()/2)-(bate.get_width()/2),ventana.get_height()-30)

ballrect.move_ip((ventana.get_width()/2)-(ball.get_width()/2),ventana.get_height()-55-bate.get_height())


nf=10
nc=11
ancho=list(range(nf))
alto=list(range(nc))
brick=[None]*nc
for i in alto:
	brick[i]=[None]*nf

recbrick=[None]*nc
for i in alto:
	recbrick[i]=[None]*nf



print(alto)
print(ancho)
print(brick)
print(brick[0][0])
for j in ancho:
	for i in alto:
		bricknum=random.randint(1,4)
		match bricknum:
			case 1:
				brick[i][j]=pygame.image.load("brickblue.png")
			case 2:
				brick[i][j]=pygame.image.load("brickgreen.png")
			case 3:
				brick[i][j]=pygame.image.load("brickyellow.png")
			case 4:
				brick[i][j]=pygame.image.load("brickred.png")
		recbrick[i][j]=brick[i][j].get_rect()
		if j % 2==0:
			recbrick[i][j].move_ip(brick[i][j].get_width()*(i),brick[i][j].get_height()*(j))
		else:
			if i > 0:
				recbrick[i][j].move_ip(-brick[i][j].get_width()/2+brick[i][j].get_width()*(i),brick[i][j].get_height()*(j))
			

print(brick)
print(recbrick)


jugando =True

while jugando:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			jugando=False
	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		baterect=baterect.move(-3,0)
	if keys[pygame.K_RIGHT]:
		baterect=baterect.move(3,0)
	if baterect.colliderect(ballrect):
		speed[1]=-speed[1]


	if keys[pygame.K_SPACE]:
		speed=[4,4]
	col=0
	for j in ancho:
		for i in alto:
			if recbrick[i][j].colliderect(ballrect):
				recbrick[i][j].move_ip(-ventana.get_width(),-ventana.get_height())
				if i==9 and recbrick[i+1][j].colliderect(ballrect) and col==0:
					speed[1]=-speed[1]
					col=1
				elif i==10 and recbrick[i-1][j].colliderect(ballrect):
					speed[1]=speed[1]
				elif i==1 and recbrick[i][j].colliderect(ballrect) and recbrick[i-1][j].colliderect(ballrect) and col==0:
					speed[1]=-speed[1]
					col=1
				elif i==0 and recbrick[i+1][j].colliderect(ballrect) and recbrick[i-1][j].colliderect(ballrect):
					speed[1]=speed[1]
				elif i<9 and recbrick[i+1][j].colliderect(ballrect) and col==0:
					speed[1]=-speed[1]
					col=1
				elif i>0 and recbrick[i-1][j].colliderect(ballrect) and col==0:
					speed[1]=-speed[1]
					col=1
				elif col==1:
					speed[1]=speed[1]
					col=0
				elif ballrect.top>recbrick[i][j].bottom:
					speed[1]=-speed[1]
				elif ballrect.bottom<recbrick[i][j].top:
					speed[1]=-speed[1]
				elif recbrick[i][j].right<ballrect.left:
					speed[0]=-speed[0]
				elif recbrick[i][j].leftt>ballrect.right:
					speed[0]=-speed[0]







	ballrect=ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right >ventana.get_width():
		speed[0]= - speed[0]
	if ballrect.top < 0 or ballrect.bottom >ventana.get_height():
		speed[1]= - speed[1]
	ventana.fill((255, 240, 200))
	ventana.blit(ball, ballrect)
	ventana.blit(bate, baterect)
	for j in ancho:
		for i in alto:
			ventana.blit(brick[i][j], recbrick[i][j])


	pygame.display.flip()
	pygame.time.Clock().tick(60)



pygame.quit()








