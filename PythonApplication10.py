import random
jakaakcja = 0
x=0
test = 0

                 
def tasowanie():

    deckcopy = odrzucone
    odrzucone.clear()
    dlugosc = len(deckcopy)
    t.clear()
    for i in range(dlugosc):
        t.append(i+1)
    random.shuffle(t)
def dobieraniereki():
    
    if len(deckcopy)<5:
        
        for i in range(len(deck)):
            try:
                reka[len(reka)+1] = deckcopy.pop(int(t[i]))
                t[i] = 0
                
            except:
                pass
        tasowanie()
    while len(reka)<5:
        
        for i in range(len(deck)):
            try:
                if len(reka) ==5:
                    break
                reka[len(reka)+1] = deckcopy.pop(int(t[i]))
                t[i] =0
                print("test")
                
            except:
                pass
               
        if len(reka) == 5:
            break
def zrzucanie():
    for i in range(len(deck)):
        try:
            odrzucone[len(odrzucone)+1] = reka[i+1]
            odrzucone[len(odrzucone)+1] = zagrane[i+1]
           
        except:
            pass
    reka.clear()
    zagrane.clear()
def dobieranie():
    
    for i in range(int(len(t))):
        if t[i] !=0:
            
            for j in range(10):
                try:
                    test = reka[j+1]
                    

                except:
                    
                    print("dobierasz karte: " ,deckcopy[int(t[i])][0])
                    reka[j+1]=deckcopy.pop(int(t[i]))
                    
                    break
            
            t[i] = 0
            
            
            break
def cosiedzieje(o):
    

    akcjadod = -1

    if o ==1:
        falsz = 0
        akcjadod += 2
        print()
        print("zagrales karte 'wioska'. Dostajesz:")
        print("+2 akcje")
        print("+1 karte")

        for i in range(int(len(t))):
            if t[i]!=0:
                falsz+=1
        if falsz>0:
           
            dobieranie()


                
        if falsz==0:
            tasowanie()
            dobieranie()
        for i in range(10):
            
            try:
                if reka[i+1][0] == "wioska":
                    

                    zagrane[int(len(zagrane))+1] = reka.pop(i+1)
                    
                   
                    break
            except:
                pass
                

    return akcjadod



            

def akcjacheck(akcheck,pcheck,zcheck):
    a = akcheck
    p = pcheck
    z = zcheck
    
    k=0
    
    
    while True:
        check =0
        
        ile = 0
        
        try:
                        
                        print("twoja reka to:")
                        print()
                        for i in range(10):
                            try:
                                print(reka[i][0],end=" ")
                            except:
                                pass
                        for i in range(10):
                            try:
                                if reka[i+1][2]=="akcja":
                                    check+=1
                                    
                            except:
                                pass
                        
                        if check==0:
                            print()
                            print("nie zadnych akcji")
                            break
                        
                        for i in range(10):
                            try:
                                if reka[i+1][2]=="akcja":
                                    print()
                                    print("mozliwe akcje to: ")
                                    break
                            except:
                                pass
                        
                        
                        
                        for u in range(10):
                                try:    
                                    
                                    if reka[u+1][2] == "akcja":
                                        print(reka[u+1][0],end=" ")
                                        
                                        ile+=1
                                        
                                except:pass
                        if ile==0:
                            print("nie masz na rece zadnych akcji")
                            break
                        print()
                        print("masz",a,"akcje")
                        print("czy chcesz zagrac akcje?")
                        wynik = str(input("tak('t')/nie('n')"))
                        if wynik =="t":
                            jakaakcja = input("podaj nazwe akcji")
                            x=0
                            
                            while x==0:
                                for i in range(10):
                                    print(jakaakcja)
                                    if karty[i+1][0] == str(jakaakcja):
                                        x=1
                                        coto = i+1
                                        
                           
                           
                                        break


                            a = a+ cosiedzieje(coto)
                            
                    

        
                        if wynik == "n":
                            break
                        k+=1
                        
        except:
                        pass
            

    
    return a,p,z

def zakupchceck(z):
    zchech = z
    
    for i in range(10):
        try:
            
            if reka[i][2] == "skarb":
                
                zchech += int(reka[i][3]) 
                
        except:
            pass
    return zchech
def zakupczy(a,p,z):
    akcje =a
    pieniadze = p
    zakupy = z
    ok = 1
    ok1=1
    koniec =" "
    strike = 0
    ktora = 0
    while zakupy>0:
        
        print("masz ", pieniadze,"pieniedzy. Czy chcesz cos kupic?")
        while ok1 == 1:
            czy = str(input("tak('t')/nie('n')"))
            if czy =="t" or czy =="n":
                ok1 =0
            else:
                print("wystapil blad; sprubuj ponownie")
        if czy=="n":
            break
        for i in range(int(len(karty))):
            print(karty[i+1][0], ",koszt :", karty[i+1][1])
        while ok == 1:
            co = str(input("Co chcesz kupic?"))
            for j in range(int(len(karty))):
                if co == karty[j+1][0]:
                    deck[int(len(deck))+1] = karty[j+1]
                    odrzucone[int(len(odrzucone))+1] = karty[j+1]
                    ktora +=int(karty[j+1][1])
                    zakupy-=1
                    ok = 0
                elif int(karty[i+1][1])>pieniadze:
                    print("nie masz wystarczajacej ilosci pieniadzy.")
                    koniec = str(input("wpisz 'stop' jezeli nie chcesz kupic innej karty"))
                    if koniec == "stop":
                        ok ==0
                        break
                else:
                    strike+=1
                
                    
        if koniec =="stop":
            break
    if zakupy==0:
        print("nie masz juz zakupow")
    pieniadze -=ktora
    return akcje,pieniadze,zakupy


karty = {
    1:["wioska","3","akcja"],


    2:["miedziaki","0","skarb","1"],

    3:["posiadlosci","2","zwyciestwo","1"]
    }
deck ={}
for i in range(1,8):
    deck[i] = karty[2]
for i in range(8,11):
    deck[i]=karty[3]

deckcopy = {}
for i in range(len(deck)):
    deckcopy[i+1]  = deck[i+1]
dlugosc = len(deck)
reka = {}
odrzucone = {}
zagrane = {}
akcja = 0
pieniadz = 0
t=[]


dlugosc = len(deckcopy)
t.clear()
for i in range(dlugosc):

        t.append(i+1)
random.shuffle(t)
print(t)
for _ in range(2):

    
    dobieraniereki()
    
    
    
    akcja = 1
    pieniedz = 0
    zakup= 1
    
    dod = []
    dod = akcjacheck(akcja,pieniadz,zakup)
    akcja = dod[0]
    pieniadz = dod[1]
    zakup = dod[2]
    pieniadz =pieniadz + zakupchceck(pieniadz)
    print()
    dod = zakupczy(akcja,pieniadz,zakup)
    akcja = dod[0]
    pieniadz = dod[1]
    zakup = dod[2]
    zrzucanie()
    dobieraniereki()
  

print("koniec ",reka)
print(zagrane)

print(akcja,pieniadz,zakup)
print(deck)
print(odrzucone)