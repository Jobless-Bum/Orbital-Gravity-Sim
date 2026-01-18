import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dirTick = 0
fps = 60

while running:
    screen.fill('white')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    dt = clock.tick(fps) / 1000

pygame.quit()