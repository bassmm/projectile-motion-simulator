import sys
import pygame

pygame.init()

window = width, height = 1200, 800
clock = pygame.time.Clock()
screen = pygame.display.set_mode(window)
fps = 60 

ball = pygame.image.load("/home/bassam/Projects/projectile-motion-simulator/intro_ball.gif")
ballrect = ball.get_rect()

# suvat values (values are multiplied by framerate)
grav = -9.81/fps 
speed = [250.0/fps,0] # pixels per second
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    
    speed[1] -= grav # constant acceleration due to gravity

    if ballrect.bottom > height:
        speed[1] = -speed[1]*0.9
    if ballrect.right > width or ballrect.left < 0:
        speed[0] = -speed[0]+0.9
    screen.fill((0,0,0))
    screen.blit(ball, ballrect)
    pygame.display.flip()
    clock.tick(fps)
