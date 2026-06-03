import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("The Maze")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

#    pygame.draw.line(screen, (0,3,0), 10, 1)
    pygame.draw.line(screen, (0,234,0), (0, 50), (600, 50),6)

    pygame.display.flip()
pygame.quit()  