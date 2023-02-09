
import random
import pygame
import time
class gracz:
    def __init__(self):
        self.karty = {
        1: ["wioska", "4", "akcja"],

        2: ["miedziaki", "0", "skarb", "1"],

        3: ["posiadlosci", "2", "zwyciestwo", "1"]
        }
        self.deck = {}
        for i in range(1, 8):
            self.deck[i] = self.karty[2]
        for i in range(8, 11):
            self.deck[i] = self.karty[3]
        self.deckcopy = {}
        for i in range(len(self.deck)):
            self.deckcopy[i + 1] = self.deck[i + 1]
        self.reka = {}
        self.odrzucone = {}
        self.zagrane = {}
        self.akcja = 0
        self.pieniadz = 0
        self.t = []
        
        
        for i in range(len(self.deckcopy)):
            self.t.append(i + 1)
        random.shuffle(self.t)

    def tasowanie(self):

        print("check")
        self.deckcopy.clear()
        for i in range(len(self.odrzucone)):
            self.deckcopy[len(self.deckcopy)+1] = self.odrzucone.pop(i+1)
        self.t.clear()
        for i in range(len(self.deckcopy)):
            self.t.append(i+1)
        random.shuffle(self.t)

    def dobieraniereki(self):
        if len(self.deckcopy)<5:
            for i in range(len(self.deck)):
                try:
                    self.reka[len(self.reka)+1] = self.deckcopy.pop(int(self.t[i]))
                    self.t[i] = 0
                except:
                    pass
            self.tasowanie(self)
        while len(self.reka)<5:
            for i in range(len(self.deck)):
                try:
                    if len(self.reka)==5:
                        break
                    self.reka[len(self.reka)+1]=self.deckcopy.pop(int(self.t[i]))
                    self.t[i] = 0
                except:
                    pass
    def zrzucanie(self):
        for i in range(len(self.t)):
            try:
                self.odrzucone[len(self.odrzucone)+1] = self.reka.pop(i+1)
                self.odrzucone[len(self.odrzucone)+1] = self.zagrane.pop(i+1)
            except:
                pass
    def dobieranie(self):
        for i in range(int(len(self.t))):          
            if self.t[i]!=0:
                for j in range(len(self.deck)):
                    try:
                        test =self.reka[j+1]
                    except:
                        print("dobierasz karte: ",self.deckcopy[int(self.t[i])][0])
                        self.reka[j+1] =self.deckcopy.pop(int(self.t[i]))
                        break
                self.t[i] = 0
                break
    def akcjacheck(self):
        self.licznik =0
        for i in range(len(self.deck)):
            try:
                if self.reka[i][2]=="akcja":
                    self.licznik+=1
                    return True
            except:
                pass
        if self.licznik==0:
            return False

    def coto(self,akcja):
        falsz=0
        akcjadod = -1
        self.to = 0
        for i in range(len(self.karty)):
            if self.karty[i+1][1] == str(akcja):
                i= self.to
        if self.to+1==1:
            akcjadod+=2
            print("Zagrales karte: 'wioska'. Dostajesz:")
            print("+2 akcje")
            print("+1 karte")
            for i in range(len(self.t)):
                if self.t[i]!=0:
                    print("falsz!=0")
                    falsz+=1
            if falsz>0:
                    self.dobieranie()
            if falsz==0:
                    self.tasowanie()
                    self.dobieranie()
            for i in range(len(self.deck)):
                try:
                    if self.reka[i+1][0]=="wioska":
                        self.zagrane[len(self.zagrane)+1] = self.reka.pop(i+1)
                except:
                    pass
            print(self.reka,self.zagrane)
            

class karta:
    def __init__(self,x,y,wys,szer):
        self.kwadrat = pygame.rect.Rect(x,y,szer,wys)

def rysuj(nazwa):
    pygame.draw.rect(okno,RED, nazwa.kwadrat)

def ruchcheck(nazwa,sy,ktora,jaka):
    
    mouse_position = pygame.mouse.get_pos() 
    if nazwa.kwadrat.collidepoint(mouse_position):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(int(ktora),str(jaka))
            time.sleep(1)
            gracz1.coto(gracz1.reka[ktora][0])

        if sy>1000-szer-50:
            
            sy-=1
            
    else:
        
        if sy < 1000-szer:
            sy+=1
    
    return sy


szer = 200

check =0
RED   = (255,   0,   0)
starty = 1000-szer
startyb = 1000-szer
pygame.init()
okno = pygame.display.set_mode((1920,1000))
pygame.display.set_caption("moja gra")

run = True
checkb =0
y=1000-szer
yb = 1000-szer
yc =1000-szer
yd= 1000-szer
ye=1000-szer
gracz1 = gracz()

gracz1.dobieraniereki()
gracz1.reka[2] = gracz1.karty[1]
wys = 960/len(gracz1.reka)-10
print(gracz1.t)
print(gracz1.deck)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    okno.fill((0,0,0))
    a= karta(480,y,szer,wys)
    i=1
    b = karta(480 + (i*960/len(gracz1.reka)),yb,szer,wys)
    i+=1
    c = karta(480 + (i*960/len(gracz1.reka)),yc,szer,wys)
    i+=1
    d = karta(480 + (i*960/len(gracz1.reka)),yd,szer,wys)
    i+=1
    e = karta(480 + (i*960/len(gracz1.reka)),ye,szer,wys)


    pygame.draw.rect(okno, RED, a.kwadrat)
    pygame.draw.rect(okno,RED,b.kwadrat)
    pygame.draw.rect(okno,RED,c.kwadrat)
    pygame.draw.rect(okno,RED,d.kwadrat)
    pygame.draw.rect(okno,RED,e.kwadrat)

    pygame.display.flip()
    if gracz1.akcjacheck():
        print("jest akcja")
    
        i= 1
        zmienna = ruchcheck(a,y,i,gracz1.reka[i][0])
        i+=1
        zmianna2 = ruchcheck(b,yb,i,gracz1.reka[i][0])
        i+=1
        zmienna3 = ruchcheck(c,yc,i,gracz1.reka[i][0])
        i+=1
        zmienna4 = ruchcheck(d,yd,i,gracz1.reka[i][0])
        i+=1
        zmienna5 = ruchcheck(e,ye,i,gracz1.reka[i][0])
        yb = zmianna2
        y =  zmienna
        yc = zmienna3
        yd = zmienna4
        ye = zmienna5
        
