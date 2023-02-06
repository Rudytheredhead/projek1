
import pygame
import time
SCREEN_WIDTH = 430
SCREEN_HEIGHT = 410
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
FPS = 30
startx = 0
starty = 0
i=0
check =0
list = [1,2,3,4,5,6,7],["a","b","c","d","e","f","g"]

class kwadrta:
    def __init__(self,x,y,wys,szer):
        self.rectangle = pygame.rect.Rect(x,y,szer,wys)
def ruchcheck(sx,sy,c):
    
    if sx==0:
            x,y = pygame.mouse.get_pos()
            if x>sx and x<sx+50 and y>sy and y<sy +50:
                print("test if 1")
                while sx<50:
                    a = kwadrta(sx,sy,50,50)
                    win.fill((0,0,0))
                    sx +=0.1
                    sy +=0.1
                    pygame.draw.rect(win,RED,a.rectangle)
                    pygame.draw.rect(win,RED,b.rectangle)
                    pygame.display.flip()
                    c = 1
                sx = 50
                sy =50
                time.sleep(0.5)

    else :
            x,y = pygame.mouse.get_pos()
            if x>sx and x<sx+50 and y>sy and y<sy +50:
                print("test jest")
                pass
            else:
                print("test if 2")
                while sx>0:
                    a = kwadrta(sx,sy,50,50)
                    win.fill((0,0,0))
                    sx -=0.1
                    sy -=0.1
                    pygame.draw.rect(win,RED,a.rectangle)
                    pygame.draw.rect(win,RED,b.rectangle)
                    pygame.display.flip()

                    c = 0 
                sx = 0
                sy = 0
    if event.type == pygame.MOUSEBUTTONDOWN:
        if c ==1:
            print("click test")
            time.sleep(2)
    return sx,sy,c
x= 1000
wys = 100
szer =50
a = kwadrta(x,200,wys,szer)
b = kwadrta(x,300,wys,szer)
c = kwadrta(x,400,wys,szer)
d = kwadrta(x,500,wys,szer)
e = kwadrta(x,600,wys,szer)
def rysuj():
    pygame.draw.rect(win,RED,a.rectangle)
    pygame.draw.rect(win,RED,b.rectangle)
    pygame.draw.rect(win,RED,c.rectangle)
    pygame.draw.rect(win,RED,d.rectangle)
    pygame.draw.rect(win,RED,e.rectangle)
pygame.init()
win = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("tak")
rectangle = pygame.rect.Rect(176,134,30,30)
rectangle_draging = False
clock = pygame.time.Clock()
running = True

while running:
    print("test")
    a = kwadrta(startx,starty,50,50)
    b = kwadrta(200,200,50,50)
    i+=1
    if i==1:
        pygame.draw.rect(win,RED,a.rectangle)
        pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
    
    dod = ruchcheck(startx,starty,check)
    startx = dod[0]
    starty = dod[1]
    check = dod[2]
    pygame.draw.rect(win,RED,b.rectangle)
    pygame.display.flip()
   

    
    pygame.display.flip()