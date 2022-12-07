import random
import math
##import plotly.figure_factory as ff
import plotly.express as ff
import pandas as pd
import plotly


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

def cMaxGant(rendlista,munkaSzamSzam,gepekSzamSzam):
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
    return lista


def valamilista(vegleges,sorrend,cmax):
    vegleges.append([sorrend,cmax])
    return vegleges

def mutacio(sorrend, munkaSzamSzam):
    melyik = 0
    hova = 0
    while melyik == hova:
        melyik = random.randint(0,munkaSzamSzam-1)
        hova = random.randint(0,munkaSzamSzam-1)
    lista = []
    for i in range(munkaSzamSzam):
        lista.append(sorrend[i])

    tmp = lista[hova]
    lista[hova]=lista[melyik]
    lista[melyik] = tmp
    return lista
   
def optimum(veglegeslista):
    elem = []
    for i in range(len(veglegeslista)):
        elem.append(veglegeslista[i][1])
    minimum = min(elem)

    lista = []
    for i in range(len(veglegeslista)):
        if veglegeslista[i][1] == minimum:
            lista.append([veglegeslista[i]])
    return lista[0]
    

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
    veg = optimum(vegleges)
    print("optimális sorrend:",veg)
    ertekek = []
    jobok = []
    for i in range(munkaSzam):
        for j in range(munkaSzam):
            if veg[0][0][i] == alaplista[j][0][0]:
                ertekek.append(alaplista[j][1])
                jobok.append(veg[0][0][i])
    ertekek = cMaxGant(ertekek,munkaSzam,gepekSzam)

    ganttLista = []
    for i in range(munkaSzam):
        for j in range(gepekSzam):
            tempLista = []
            if i ==0:
                if j==0:
                    start=0
                    bef=ertekek[i][j]
                    tempLista.append(jobok[i])
                    tempLista.append(start)
                    tempLista.append(bef)
                    tempLista.append("Green")
                    ganttLista.append(tempLista)
                else:
                    start = ertekek[i][j-1]
                    bef = ertekek[i][j]
                    tempLista.append(jobok[i])
                    tempLista.append(start)
                    tempLista.append(bef)
                    tempLista.append("Green")
                    ganttLista.append(tempLista)
            else:
                if j==0:
                    start = ertekek[i-1][j]
                    bef = ertekek[i][j]
                    tempLista.append(jobok[i])
                    tempLista.append(start)
                    tempLista.append(bef)
                    tempLista.append("Green")
                    ganttLista.append(tempLista)
                else:
                    start = ertekek[i][j-1]
                    bef = ertekek[i][j]
                    tempLista.append(jobok[i])
                    tempLista.append(start)
                    tempLista.append(bef)
                    tempLista.append("Green")
                    ganttLista.append(tempLista)
                    
      

##    print(ganttLista)
    df = pd.DataFrame(ganttLista,columns=['name','start','end', 'color'])
    print(df)

    fig = ff.timeline(df, x_start=df['start'], x_end=df['end'],y=df['name'], color=df['color'], title='Flow-shop')
    fig.update_yaxes(autorange="reversed")
    fig.show()
    plotly.offline.plot(fig, filename='Task_Flowshop_Gantt.html')
    


def main():
    genAlsoHatar = 1
    genFelsoHatar = 10
    munkaSzam = 10
    gepekSzam = 4
    
    leallasiFeltetl = int(input("Adja meg a leállási feltételt: ")) 

    alaplista =(generalas(genAlsoHatar,genFelsoHatar,munkaSzam,gepekSzam))
    print("alaplista")
    for i in range(len(alaplista)):
        print(alaplista[i])
    print("feladatmegoldas")
    feladat(alaplista,munkaSzam,leallasiFeltetl,gepekSzam)
    

    
if __name__ == "__main__":
    main()







