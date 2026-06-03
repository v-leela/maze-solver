import pygame
pygame.init()

screen = pygame.display.set_mode((666, 666))
pygame.display.set_caption("The Maze")

box_x = 3
box_y = 3
box_width = 18
box_height = 18
speed = 1

cell_size=20
grid_width=666//cell_size
grid_height=666//cell_size

path = [(box_x, box_y, None, None)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    ###lines
    for i in range(1,666,cell_size):
        pygame.draw.line(screen, (0,234,0), (1, i), (662, i),2)
        pygame.draw.line(screen, (0,234,0), (i,1), (i,662),2)

    ###movement
    keys=pygame.key.get_pressed()
    moved=False
    old_x, old_y = box_x, box_y

    if keys[pygame.K_UP] and box_y>=4:
        box_y-=20
        moved = True
    if keys[pygame.K_DOWN] and box_y<=640:
        box_y+=20
        moved = True
    if keys[pygame.K_LEFT] and box_x>=4:
        box_x-=20
        moved = True
    if keys[pygame.K_RIGHT] and box_x<=640:
        box_x+=20
        moved = True

    ###coloring the path
    if moved:
        path.append((box_x, box_y, old_x, old_y))

    for x, y, from_x, from_y in path:
        if from_x is None and from_y is None:
            pygame.draw.rect(screen, (150, 45, 45), (x, y, box_width, box_height))
        elif from_y != y:  
            if from_y > y:  
                pygame.draw.rect(screen, (150, 45, 45), (x, y, box_width, box_height + 2))
            else: 
                pygame.draw.rect(screen, (150, 45, 45), (x, y-2, box_width, box_height+2))
        elif from_x != x:  
            if from_x > x:  
                pygame.draw.rect(screen, (150, 45, 45), (x, y, box_width + 2, box_height))
            else:  
                pygame.draw.rect(screen, (150, 45, 45), (x-2, y, box_width+2 , box_height))

    ###box
    pygame.draw.rect(screen, (239,45,92), (box_x, box_y, box_width, box_height))

    pygame.display.flip()
    pygame.time.delay(100)
pygame.quit()  