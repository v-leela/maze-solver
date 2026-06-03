import pygame
pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Box")


RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0,0,0)


box_x = 350
box_y = 250
box_width = 10
box_height = 10
speed=1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys=pygame.key.get_pressed()

    if keys[pygame.K_w]:
        box_y-=speed
    if keys[pygame.K_s]:
        box_y+=speed
    if keys[pygame.K_a]:
        box_x-=speed
    if keys[pygame.K_d]:
        box_x+=speed

    if box_x > screen.get_width():
        box_x = -box_width
    if box_x + box_width < 0:
        box_x = screen.get_width()
    if box_y > screen.get_height():
        box_y = -box_height
    if box_y < -box_height:
        box_y = screen.get_height()
    

    
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (box_x, box_y, box_width, box_height))

    pygame.display.flip()
pygame.quit()
