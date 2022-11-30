import random
import math

def generalas(gen_genAlsoHatar, gen_genFelsoHatar, munkaSzam_szam, gepekSzam_szam):
    alapLista=[]
    for i in range(1,munkaSzam_szam+1):
        alapLista1 = []
        alapLista2 = []
        alapLista3 = []
        
        alapLista1.append("w"+str(i))
        for a in range(0,gepekSzam_szam):
            alapLista2.append(random.randint(gen_genAlsoHatar, gen_genFelsoHatar))
        alapLista3.append(alapLista1)
        alapLista3.append(alapLista2)
        alapLista.append(alapLista3)
        
    return alapLista

def sorGeneralas(alapLista, munkaSzamak_szama):
    generate_list = []
    while len(generate_list)<munkaSzamak_szama:
        randNum = random.randint(1,munkaSzamak_szama)
        if len(generate_list) == 0:
            generate_list.append("w"+str(randNum))
        else:
            for i in range(0,len(generate_list)):
                if generate_list.count("w"+str(randNum)) == 0:
                    generate_list.append("w"+str(randNum))
                else:
                    continue
    return generate_list

def ertekRendezes(alapLista,generate_list, munkaSzamszam):
    rendezettalapLista = []
    for k in range(0,munkaSzamszam):
        szam = 0
        for i in alapLista:
            for j in i[0]:
                if j != generate_list[k]:
                    szam+=1
                else:
                    rendezettalapLista.append(alapLista[szam][1])
    return rendezettalapLista

def cMax(rendlista,munkaSzamSzam,gepekSzamSzam):
    lista = []
    
    for i in range(munkaSzamSzam):
        temp = []
        for j in range(gepekSzamSzam):
            if i == 0:
                if j == 0:
                    temp.append(rendlista[i][j])
                else:
                    ertek = rendlista[i][j]+temp[j-1]
                    temp.append(ertek)
                    
                if j == gepekSzamSzam-1:
                    lista.append(temp)
            else:
                if j == 0:
                    ertek = lista[i-1][j]+rendlista[i][j]
                    temp.append(ertek)
                else:
                    if temp[j-1]-lista[i-1][j] >= 0:
                        ertek = rendlista[i][j]+temp[j-1]
                        temp.append(ertek)
                    else:
                        var=lista[i-1][j]-temp[j-1]
                        ertek = rendlista[i][j]+temp[j-1]+var
                        temp.append(ertek)
                if j == gepekSzamSzam-1:
                    lista.append(temp)

    cmax=lista[munkaSzamSzam-1][gepekSzamSzam-1]
    return cmax

def valamilista(vegleges,sorrend,cmax):
    vegleges.append([sorrend,cmax])
    return vegleges

def mutacio(sorrend, munkaSzamSzam):
    melyik = 0
    hova = 0
    while melyik == hova:
        melyik = random.randint(0,munkaSzamSzam-1)
        hova = random.randint(0,munkaSzamSzam-1)
##    print(melyik, hova)
    lista = []
    for i in range(munkaSzamSzam):
        lista.append(sorrend[i])
##    print("csere előt")
##    print(lista)
    tmp = lista[hova]
    lista[hova]=lista[melyik]
    lista[melyik] = tmp
##    print("csere után")
##    print(lista)
    return lista
   
def optimum(veglegeslista):
    elem = []
    for i in range(len(veglegeslista)):
        elem.append(veglegeslista[i][1])
    minimum = min(elem)

    for i in range(len(veglegeslista)):
        if veglegeslista[i][1] == minimum:
            print("az optimum:", veglegeslista[i])

def feladat(alaplista,munkaSzam,leallasiFeltetl,gepekSzam):
    vegleges=[]
    sorok = []
    elsosor= sorGeneralas(alaplista,munkaSzam)
    rendezettlista = ertekRendezes(alaplista,elsosor,munkaSzam)
    cmax = cMax(rendezettlista,munkaSzam,gepekSzam)
    vegleges = valamilista(vegleges,elsosor,cmax)
    temp = mutacio(elsosor,munkaSzam)
    sorok.append(elsosor)
   
    while len(sorok)<leallasiFeltetl:
        if sorok.count(temp) < 1:
            sorok.append(temp)
            rendezettlista = ertekRendezes(alaplista,temp,munkaSzam)
            cmax = cMax(rendezettlista,munkaSzam,gepekSzam)
            vegleges = valamilista(vegleges,temp,cmax)
        else:
            temp = mutacio(temp,munkaSzam)
            
    
    
    
    return vegleges



def main():
    genAlsoHatar = 1
    genFelsoHatar = 10
    munkaSzam = 50
    gepekSzam = 10
    leallasiFeltetl = 1000 ## ezt fixen el tudja kezelni


    alaplista =(generalas(genAlsoHatar,genFelsoHatar,munkaSzam,gepekSzam))
##    print(alaplista)
    print("alaplista")
    for i in range(len(alaplista)):
        print(alaplista[i])
    print("feladatmegoldas")
    veg = feladat(alaplista,munkaSzam,leallasiFeltetl,gepekSzam)
    optimum(veg)
    
if __name__ == "__main__":
    main()








