import pygame
import sys
import random
from pygame.locals import *

def get_new_position(pos, vel):
	return (pos[0]+vel[0],pos[1]+vel[1])


def main():
	pygame.init()
	pygame.font.init()
	myfont = pygame.font.SysFont('Comic Sans MS',60)

	SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (1920, 1000)
	screen = pygame.display.set_mode(SCREEN_SIZE)
	pygame.display.set_caption('Boing')

	screen.fill((255,255,255))

	midline=pygame.draw.line(screen,(0,0,0),(SCREEN_WIDTH/2,0),(SCREEN_WIDTH/2,SCREEN_HEIGHT),10)
	ball_centre = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	ball_radius = 20
	ball = pygame.draw.circle(screen,(255,0,0), ball_centre, ball_radius)
	
	score1=0
	score2=0

	PADDLE_LENGTH = 100
	PADDLE_WIDTH = 10

	paddle1_top = (4, (SCREEN_HEIGHT/2) - (PADDLE_LENGTH/2))
	paddle1_bottom = (4, (SCREEN_HEIGHT/2) + (PADDLE_LENGTH/2))
	paddle2_top = (SCREEN_WIDTH-4, (SCREEN_HEIGHT/2) - (PADDLE_LENGTH/2))
	paddle2_bottom = (SCREEN_WIDTH-4, (SCREEN_HEIGHT/2) + (PADDLE_LENGTH/2))
	paddle1 = pygame.draw.line(screen,(0,0,0),paddle1_top,paddle1_bottom,PADDLE_WIDTH)
	paddle2 = pygame.draw.line(screen,(0,0,0),paddle2_top,paddle2_bottom,PADDLE_WIDTH)

	ball_velocity = (1, random.choice([-1,1]))
	paddle1_velocity = (0,0)
	paddle2_velocity = (0,0)

	pygame.display.update()

	while 1:
		for event in pygame.event.get():
			if event.type==QUIT:
				return
			elif event.type==pygame.KEYDOWN:
				if event.key==pygame.K_UP:
					paddle2_velocity=(0,-3)
				if event.key == pygame.K_DOWN:
					paddle2_velocity=(0,3)
				if event.key == pygame.K_w:
					paddle1_velocity=(0,-3)
				if event.key==pygame.K_s:
					paddle1_velocity=(0,3)
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or pygame.K_DOWN:
					paddle2_velocity = (0,0)
				if event.key == pygame.K_w or pygame.K_s:
					paddle1_velocity=(0,0)




		ball_centre=get_new_position(ball_centre,ball_velocity)
		if (ball_centre[1]+ball_radius > SCREEN_HEIGHT or ball_centre[1]-ball_radius < 0):
			ball_velocity =(ball_velocity[0],-ball_velocity[1])
			ball_centre=get_new_position(ball_centre,ball_velocity)

		######################################################
		
		# if (ball_centre[0] + ball_radius > SCREEN_WIDTH or ball_centre[0] -ball_radius <0):
		# 	ball_velocity =(-ball_velocity[0],ball_velocity[1])
		# 	ball_centre=get_new_position(ball_centre,ball_velocity)
		###############################




		screen.fill((255,255,255))
		circ=pygame.draw.circle(screen,(0,0,0),(SCREEN_WIDTH/2,SCREEN_HEIGHT/2),40)
		cir=pygame.draw.circle(screen,(255,255,255),(SCREEN_WIDTH/2,SCREEN_HEIGHT/2),32)
		midline=pygame.draw.line(screen,(0,0,0),(SCREEN_WIDTH/2,0),(SCREEN_WIDTH/2,SCREEN_HEIGHT),6)

		ball = pygame.draw.circle(screen,(255,0,0), ball_centre, ball_radius)
		
		p1_new_top = get_new_position(paddle1_top, paddle1_velocity)
		p1_new_bottom = get_new_position(paddle1_bottom, paddle1_velocity)

		p2_new_top = get_new_position(paddle2_top, paddle2_velocity)
		p2_new_bottom = get_new_position(paddle2_bottom, paddle2_velocity)

		if(p1_new_top[1]>0 and p1_new_bottom[1]<SCREEN_HEIGHT):
			paddle1_top=p1_new_top
			paddle1_bottom=p1_new_bottom

		if(p2_new_top[1]>0 and p2_new_bottom[1]<SCREEN_HEIGHT):
			paddle2_top=p2_new_top
			paddle2_bottom=p2_new_bottom

		if ball_centre[0] + ball_radius > SCREEN_WIDTH:
			if (paddle2_top[1] < ball_centre[1] and paddle2_bottom[1] > ball_centre[1]):
				ball_velocity = (-ball_velocity[0], ball_velocity[1])
			else:
				ball_centre = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
				ball_velocity = (0,0)
				text=myfont.render('Player 1 Wins!',False,(0,0,0))
				textrect = text.get_rect()
				textrect.centerx = screen.get_rect().centerx
				textrect.centery = screen.get_rect().centery
				
				screen.fill((255, 255, 255))
				screen.blit(text, textrect)
				 
				pygame.display.update()
				while 1:
					pausef=1
					for event in pygame.event.get():
						if event.type==QUIT:
							return
						elif event.type==pygame.KEYDOWN:
							if event.key==pygame.K_r:
								screen.fill((255,255,255))
								circ=pygame.draw.circle(screen,(0,0,0),(SCREEN_WIDTH/2,SCREEN_HEIGHT/2),40)
								cir=pygame.draw.circle(screen,(255,255,255),(SCREEN_WIDTH/2,SCREEN_HEIGHT/2),32)
								midline=pygame.draw.line(screen,(0,0,0),(SCREEN_WIDTH/2,0),(SCREEN_WIDTH/2,SCREEN_HEIGHT),6)
								ball_centre = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
								ball = pygame.draw.circle(screen,(255,0,0), ball_centre, ball_radius)
								ball_velocity = (1, random.choice([-1,1]))
								paddle1_top = (4, (SCREEN_HEIGHT/2) - (PADDLE_LENGTH/2))
								paddle1_bottom = (4, (SCREEN_HEIGHT/2) + (PADDLE_LENGTH/2))
								paddle2_top = (SCREEN_WIDTH-4, (SCREEN_HEIGHT/2) - (PADDLE_LENGTH/2))
								paddle2_bottom = (SCREEN_WIDTH-4, (SCREEN_HEIGHT/2) + (PADDLE_LENGTH/2))
								paddle1 = pygame.draw.line(screen,(0,0,0),paddle1_top,paddle1_bottom,PADDLE_WIDTH)
								paddle2 = pygame.draw.line(screen,(0,0,0),paddle2_top,paddle2_bottom,PADDLE_WIDTH)
								pausef=0	
					if pausef==0:
						break

		if ball_centre[0]-ball_radius<0:
			if (paddle1_top[1]<ball_centre[1] and paddle1_bottom[1]>ball_centre[1]):
				ball_velocity = (-ball_velocity[0], ball_velocity[1])

			else:
				ball_centre = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
				ball_velocity = (0,0)
				text=myfont.render('Player 2 Wins!',False,(0,0,0))
				
				textrect = text.get_rect()
				textrect.centerx = screen.get_rect().centerx
				textrect.centery = screen.get_rect().centery
				 
				screen.fill((255, 255, 255))
				screen.blit(text, textrect)
				pygame.display.update()
				while 1:
					pausef=1
					for event in pygame.event.get():
						if event.type==QUIT:
							return
						elif event.type==pygame.KEYDOWN:
							if event.key==pygame.K_r:
								screen.fill((255,255,255))
								circ=pygame.draw.circle(screen,(0,0,0),(SCREEN_WIDTH/2,SCREEN_HEIGHT/2),40)
								cir=pygame.draw.circle(screen,(255,255,255),(SCREEN_WIDTH/2,SCREEN_HEIGHT/2),32)
								midline=pygame.draw.line(screen,(0,0,0),(SCREEN_WIDTH/2,0),(SCREEN_WIDTH/2,SCREEN_HEIGHT),6)
								ball_centre = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
								ball = pygame.draw.circle(screen,(255,0,0), ball_centre, ball_radius)
								ball_velocity = (1, random.choice([-1,1]))
								paddle1_top = (4, (SCREEN_HEIGHT/2) - (PADDLE_LENGTH/2))
								paddle1_bottom = (4, (SCREEN_HEIGHT/2) + (PADDLE_LENGTH/2))
								paddle2_top = (SCREEN_WIDTH-4, (SCREEN_HEIGHT/2) - (PADDLE_LENGTH/2))
								paddle2_bottom = (SCREEN_WIDTH-4, (SCREEN_HEIGHT/2) + (PADDLE_LENGTH/2))
								paddle1 = pygame.draw.line(screen,(0,0,0),paddle1_top,paddle1_bottom,PADDLE_WIDTH)
								paddle2 = pygame.draw.line(screen,(0,0,0),paddle2_top,paddle2_bottom,PADDLE_WIDTH)
								pausef=0

					if pausef==0:
						break


		paddle1 = pygame.draw.line(screen,(0,0,0),paddle1_top,paddle1_bottom,PADDLE_WIDTH)
		paddle2 = pygame.draw.line(screen,(0,0,0),paddle2_top,paddle2_bottom,PADDLE_WIDTH)
		pygame.time.Clock().tick(360)
		pygame.display.update()

if __name__ == '__main__': main()		


