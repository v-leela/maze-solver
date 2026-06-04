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

cell_size=20
grid_width=666//cell_size
grid_height=666//cell_size

visited={(box_x,box_y)}
coordinates = [(box_x, box_y, None, None)]
path = [(box_x, box_y, None, None)]

def get_unvisited_neighbors(x, y):
    neighbors = []
    if y >= 23 and (x, y - 20) not in visited:        #up
        neighbors.append((x, y - 20))
    if y <= 623 and (x, y + 20) not in visited:       #down
        neighbors.append((x, y + 20))
    if x >= 23 and (x - 20, y) not in visited:        #left
        neighbors.append((x - 20, y))
    if x <= 623 and (x + 20, y) not in visited:       #right
        neighbors.append((x + 20, y))
    return neighbors

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    ###grid
    for i in range(1,666,cell_size):
        pygame.draw.line(screen, (0,234,0), (1, i), (662, i),2)
        pygame.draw.line(screen, (0,234,0), (i,1), (i,662),2)

    ###random movement
    """ direction=random.randint(1,4)
    moved=False
    old_x, old_y = box_x, box_y

    if direction==1 and box_y>=4:
        if (box_x,box_y-20) not in [(x,y) for x,y,a,b in coordinates]:
            box_y-=20
            moved=True
    if direction==2 and box_y<=640:
       if (box_x,box_y+20) not in [(x,y) for x,y,a,b in coordinates]:
           box_y+=20
           moved=True
    if direction==3 and box_x>=4:
        if (box_x-20,box_y) not in [(x,y) for x,y,a,b in coordinates]:
           box_x-=20
           moved=True
    if direction==4 and box_x<=640:
        if (box_x+20,box_y) not in [(x,y) for x,y,a,b in coordinates]:
           box_x+=20
           moved=True """
    neighbours=get_unvisited_neighbors(box_x, box_y)
    if neighbours:
        old_x,old_y=box_x,box_y
        box_x,box_y=random.choice(neighbours)
        visited.add((box_x,box_y))
        path.append((box_x,box_y,old_x,old_y))
        coordinates.append((box_x, box_y, old_x, old_y))


    
    ###back tracking at the previous junction
    elif len(path)>=2:
        box_x, box_y = path[-1][2],path[-1][3]
        path.pop()

    ###coloring the path
    for x, y, from_x, from_y in coordinates:
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
    pygame.time.delay(30)
pygame.quit()  
