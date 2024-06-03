import pygame

pygame.init()

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jumper")
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

player = pygame.Rect(10, screen_height - 50 - player_size, player_size, player_size)
ground = pygame.Rect(0, screen_height - 50, screen_width, 50)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += dx    

    player = pygame.Rect(x, screen_height - 50 - player_size, player_size, player_size)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        dx = 1
    elif keys[pygame.K_LEFT]:
        dx = -1
    else:
        dx = 0

    screen.fill(black)
    pygame.draw.rect(screen, brown, ground)

    pygame.draw.rect(screen, green, player)

    pygame.display.flip()



pygame.quit()