from gomba import Gomba
gomba_lista = []

def beolvas():
    fajl = open("gombak_jav.txt", "r", encoding="UTF-8")
    fajl.readline()
    sorok = fajl.readlines()
    fajl.close()
    gombak_szama(sorok)
    papsapka(sorok)
    tinoru(sorok)

def gombak_szama(sorok):
    print(f"III/A, B:\n\tA gombák száma: {len(sorok)}.")

def papsapka(sorok):
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("@")
        Gomba(sor)
        gomba_lista.append(Gomba(sor))
        i+=1

    x = 0
    while x < len(gomba_lista):
        if gomba_lista[x].nemzetseg == "papsapkagombák ":
            print(f"III/C:\n\tAz első papsapkagomba neve: {gomba_lista[x].nev}.")
            x = len(gomba_lista)
        x += 1

def tinoru(sorok):
    i = 0
    tinorudb = 0
    while i < len(gomba_lista):
        if gomba_lista[i].nemzetseg == "tinóru":
            tinorudb += 1
        i += 1

    print(f"III/D:\n\tA tinóru gombák száma: {tinorudb}.")