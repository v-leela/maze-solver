import pygame
import random
pygame.init()

screen = pygame.display.set_mode((666, 666))
pygame.display.set_caption("The Maze")

box_x = 3
box_y = 3
box_width = 18
box_height = 18

cell_size=20

pt_x=3
pt_y=3
pt_width = 18
pt_height = 18

ways={}
visited={(box_x,box_y)}
coordinates = [(box_x, box_y, None, None)]
solver_coordinates=[(pt_x,pt_y,None,None)]
solver_path=[(pt_x,pt_y,None,None)]
path = [(box_x, box_y, None, None)]

move_cooldown=-1

def add_passage(x1,y1,x2,y2):
    ways.setdefault((x1,y1), set()).add((x2,y2))
    ways.setdefault((x2,y2), set()).add((x1,y1))

def can_move(frm_x,frm_y,to_x,to_y):
    return (frm_x,frm_y) in ways and (to_x,to_y) in ways[(frm_x,frm_y)]

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
    neighbours=get_unvisited_neighbors(box_x, box_y)
    if neighbours:
        old_x,old_y=box_x,box_y
        box_x,box_y=random.choice(neighbours)
        add_passage(box_x,box_y,old_x,old_y)
        visited.add((box_x,box_y))
        path.append((box_x,box_y,old_x,old_y))
        coordinates.append((box_x, box_y, old_x, old_y))

    ###back tracking at the previous cell
    elif len(path)>=2:
        box_x, box_y = path[-1][2],path[-1][3]
        old_x, old_y=path[-1][0],path[-1][1]
        path.pop()

    ###coloring the path(creating the maze)
    for x, y, from_x, from_y in coordinates:
        if from_x is None and from_y is None:
            pygame.draw.rect(screen, (0,130,0), (x, y, box_width, box_height))
        elif from_y != y:  
            if from_y > y:  
                pygame.draw.rect(screen, (0,130,0), (x, y, box_width, box_height + 2))
            else: 
                pygame.draw.rect(screen, (0,130,0), (x, y-2, box_width, box_height+2))
        elif from_x != x:  
            if from_x > x:  
                pygame.draw.rect(screen, (0,130,0), (x, y, box_width + 2, box_height))
            else:  
                pygame.draw.rect(screen, (0,130,0), (x-2, y, box_width+2 , box_height))

    ###box
    pygame.draw.rect(screen, (0,200,0), (box_x, box_y, box_width, box_height))

    ###movement of solver
    move_cooldown -= 1
    if move_cooldown<0:
        keys=pygame.key.get_pressed()
        moved=False
        oldpt_x,oldpt_y=pt_x,pt_y
        if keys[pygame.K_UP] and pt_y>=4:
            if can_move(pt_x, pt_y, pt_x, pt_y - 20):
                pt_y-=20
                moved=True
        elif keys[pygame.K_DOWN] and pt_y<=640:
            if can_move(pt_x, pt_y, pt_x, pt_y+20):
                pt_y+=20
                moved=True
        elif keys[pygame.K_LEFT] and pt_x>=4:
            if can_move(pt_x-20, pt_y, pt_x, pt_y):
                pt_x-=20
                moved=True
        elif keys[pygame.K_RIGHT] and pt_x<=640:
            if can_move(pt_x+20, pt_y, pt_x, pt_y):
                pt_x+=20
                moved=True        
        if moved:
            solver_coordinates.append((oldpt_x,oldpt_y,pt_x,pt_y))
            move_cooldown=120

    ###coloring the path(of the solver)
    for x, y, from_x, from_y in solver_coordinates:
        if from_x is None and from_y is None:
            pygame.draw.rect(screen, (250,250,0), (x, y, box_width, box_height))
        elif from_y != y:  
            if from_y > y:  
                pygame.draw.rect(screen, (250,250,0), (x, y, box_width, box_height + 2))
            else: 
                pygame.draw.rect(screen, (250,250,0), (x, y-2, box_width, box_height+2))
        elif from_x != x:  
            if from_x > x:  
                pygame.draw.rect(screen, (250,250,0), (x, y, box_width + 2, box_height))
            else:  
                pygame.draw.rect(screen, (250,250,0), (x-2, y, box_width+2 , box_height))

    ###solver
    pygame.draw.rect(screen, (234,0,234), (pt_x, pt_y, pt_width, pt_height))
    
    pygame.display.flip()
#    pygame.time.delay(100)
pygame.quit()