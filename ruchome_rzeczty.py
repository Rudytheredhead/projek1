
import pygame
import time

def kwadrat(a,b):
    pygame.draw.rect(win,(255,0,0),(a,b,50,50))

pygame.init()
# definiowanie okna gry
win = pygame.display.set_mode((500, 500))
# wyœwietlanie okna gry
pygame.display.set_caption("Moja Gra")
run = True
# pêtla g³ówna
startx = 0
starty = 0
check = 0
check =0
i=0
while run:
    # obs³uga zdarzeñ 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    i+=1
    
    if i ==1:
        kwadrat(startx,starty)
        pygame.display.flip()
    print("test")
    x,y = pygame.mouse.get_pos()
    print(x,y)
    print(startx)
    if startx==0:
        if x>startx and x<startx+50 and y>starty and y<starty +50:
            if startx  <50:
                while startx <50:
            
               
                    win.fill((0,0,0))
                    startx += 0.1
                    starty +=0.1
                    kwadrat(startx,starty)
                    pygame.display.flip()
                    check = 1
                    print("teste 2")
                time.sleep(1)
    else:
        
        if x>startx and x<startx+50 and y>starty and y<starty +50:
            
            print("test if")
        else:
           
                while startx >=0:
            
          
               
                    win.fill((0,0,0))
                    startx -= 0.1
                    starty -=0.1
                    kwadrat(startx,starty)
                    pygame.display.flip()
                    print("test 3")
                    check = 0
                startx =0
                starty =0
    
    print(pygame.mouse.get_pos())
    x,y = pygame.mouse.get_pos()
    
   

    pygame.display.flip()