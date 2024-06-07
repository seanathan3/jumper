import pygame
from player import Player

pygame.init()

screen_width = 1280
screen_height = 720
fps = 60

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jumper")
clock = pygame.time.Clock()
running = True

player_size = 15

blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
brown = (150, 75, 0)

x = 0
y = 0
dx = 0
dy = 0

player = Player(5, 5, 5, blue)
ground = pygame.Rect(0, screen_height - 50, screen_width, 50)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += dx    

    player = pygame.Rect(x, screen_height - 50 - player_size * 3, player_size, player_size * 3)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        dx = 5
    elif keys[pygame.K_LEFT]:
        dx = -5
    else:
        dx = 0

    screen.fill(black)
    pygame.draw.rect(screen, brown, ground)

    pygame.draw.rect(screen, green, player)

    pygame.display.flip()

    dt = clock.tick(fps) / 1000



pygame.quit()