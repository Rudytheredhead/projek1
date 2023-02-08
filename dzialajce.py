import pygame
class karta:
    def __init__(self,x,y,wys,szer):
        self.kwadrat = pygame.rect.Rect(x,y,szer,wys)
def rysuj(nazwa):
    pygame.draw.rect(okno,RED, nazwa.kwadrat)

def ruchcheck(nazwa,sy):
    print("test czy" , str(nazwa))
    mouse_position = pygame.mouse.get_pos() 
    if nazwa.kwadrat.collidepoint(mouse_position):
        if sy>1000-szer-50:
            print("test if")
            sy-=1
    else:
        print("test else")
        if sy < 1000-szer:
            sy+=1
    return sy
szer = 200
wys = 150
check =0
RED   = (255,   0,   0)
starty = 1000-szer
startyb = 1000-szer
pygame.init()
okno = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("moja gra")
a= karta(0,starty,szer,wys)
b = karta(0,starty,szer,wys)
run = True
checkb =0
y=1000-szer
yb = 1000-szer
while run:
    okno.fill((0,0,0))
    a= karta(0,y,szer,wys)
    b = karta(300,yb,szer,wys)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.rect(okno, RED, a.kwadrat)
    pygame.draw.rect(okno,RED,b.kwadrat)
    pygame.display.flip()
    zmienna = ruchcheck(a,y)
    zmianna2 = ruchcheck(b,yb)
    yb = zmianna2
    y= zmienna
