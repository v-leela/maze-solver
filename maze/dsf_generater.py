import pygame
import random
pygame.init()

screen = pygame.display.set_mode((666, 666))
pygame.display.set_caption("The Maze")

box_x = 3
box_y = 3
box_width = 18
box_height = 18
speed = 1
j=1

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

    ###random movement
    direction=random.randint(1,4)
    moved=False
    old_x, old_y = box_x, box_y

    if direction==1 and box_y>=4:
        if (box_x,box_y-20) not in [(x,y) for x,y,a,b in path]:
            box_y-=20
            moved=True
    if direction==2 and box_y<=640:
       if (box_x,box_y+20) not in [(x,y) for x,y,a,b in path]:
           box_y+=20
           moved=True
    if direction==3 and box_x>=4:
        if (box_x-20,box_y) not in [(x,y) for x,y,a,b in path]:
           box_x-=20
           moved=True
    if direction==4 and box_x<=640:
        if (box_x+20,box_y) not in [(x,y) for x,y,a,b in path]:
           box_x+=20
           moved=True
    
    ###back tracking at the previous junction
    while moved==False:
        j+=1
        box_x,box_y=path[-j][0],path[-j][1]


    ###coloring the path
    if moved:
        path.append((box_x, box_y, old_x, old_y))
        j=0

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
