

def beker():
    korok = []
    for egeszszam in range(4):
        egeszszam= input("Kérem adjon meg 5 egész számot, melyek az egyes személyek korát jelentik! [0,120] : ")
        while not 120 >= int(egeszszam) >= 0 :
            egeszszam = input("Kérem helyes értéket adjon meg [0,120] : ")
        korok.append(egeszszam)

    egeszszam = input("Kérem adjon meg 5 egész számot, melyek az egyes személyek korát jelentik! [0,120] : ")
    egeszszam = int(egeszszam)
    while not 120 >= int(egeszszam) >= 0:
        egeszszam = input("Kérem helyes értéket adjon meg [0,120] : ")
    korok.append(egeszszam)

    i=0

    print("II/A, B, C:")

    while i <= 3:
        print(korok[int(i)], end=":")
        i+=1

    print(korok[4])

    elso = elso_idos(korok)
    konzolra_ir(elso)
    fajl_ir(elso)

def elso_idos(korok):
    i = 0
    hely = 0

    while i < len(korok):
        if int(korok[i]) > 70:
            hely = i
            i = len(korok)
        i+=1

    return hely


def konzolra_ir(elso):
    print(f"II/D, E:\n\tElső idős ember korának helye a listában: {elso}.")

def fajl_ir(elso):
    fajlir = open("oreg.txt", "w", encoding="utf-8")
    fajlir.write(f"II/F:\n\tElső idős ember korának helye a listában: {elso}.")
    fajlir.close()








