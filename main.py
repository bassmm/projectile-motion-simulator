import sys
import pygame

pygame.init()

window = width, height = 1200, 800
clock = pygame.time.Clock()
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Projectile Motion Simulator")  # window title
fps = 60

# SUVAT values (values are multiplied by framerate)
vert_distance = 800
grav = -9.81/fps
speed = [250.0/fps, -800/fps]  # pixels per second

ball = pygame.image.load("intro_ball.gif")
ball_rect = ball.get_rect()

ball_rect.bottomleft = (5, vert_distance)

while True:  # GAME LOOP ---------------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ball_rect = ball_rect.move(speed)

    speed[1] -= grav  # constant acceleration due to gravity

    if ball_rect.bottom > height - 5:
        speed[1] = -speed[1]*0.9
    if ball_rect.right > width - 5 or ball_rect.left < 5:
        speed[0] = -speed[0]+0.9
    screen.fill((0, 0, 0))
    screen.blit(ball, ball_rect)
    pygame.display.flip()
    clock.tick(fps)
