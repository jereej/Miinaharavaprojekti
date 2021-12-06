import haravasto as h
import random as rand

tila = {
    "kentta": []
}

piirretyt_ruudut = {
    "kentta": []
}

klikit = {
    "lukumäärä": 0
}

hiiri = {
    h.HIIRI_VASEN: "vasen",
    h.HIIRI_KESKI: "keski",
    h.HIIRI_OIKEA: "oikea",
}

def rand_num(z=1):
    '''Palauttaa satunnaisen kokonaisluvun nollasta z:aan'''
    luku = int((rand.random() * z))
    return luku

def lisaa_ruutu(x, y, merkki):
    lista = [x, y, merkki]
    if lista not in piirretyt_ruudut["kentta"]:
        piirretyt_ruudut["kentta"].append(lista)

def luo_numerot(x, y ,kentta):
    """Luo kentälle pelissä käytettävät numerot."""   

    for i, rivi in enumerate(kentta):
        if i <= y+1 and i >= y-1:
            for j, piste in enumerate(rivi):
                if j <= x+1 and j >= x-1:
                    if piste != "x":
                        if piste == " ":
                            kentta[i][j] = "1"
                        else:
                            luku = int(piste)
                            luku += 1
                            kentta[i][j] = str(luku)

def miinoita(kentta, ruudut, miinat):
    """Asettaa kentälle parametrin "miinat" verran miinoja satunnaisesti."""

    for i in range(miinat):
        ruutu = rand_num(len(ruudut) - 1)
        for i, sarake in enumerate(kentta):
            if i == ruudut[ruutu][1]:
                for j, rivi in enumerate(sarake):
                    if j == ruudut[ruutu][0]:
                        kentta[i][j] = "x"
                        luo_numerot(j, i, kentta)
                        
        ruudut.remove(ruudut[ruutu])

def laske_miinat(x, y , alue, lista):
    """
    Laskee ruudun ympärillä olevien miinojen määrän. Jos ympärillä on miinoja, se
    lisää niiden lukumäärän listaan.
    """

    for i, k in enumerate(alue):
        if i <= y+1 and i >= y-1:
            for j, piste in enumerate(k):
                if j <= x+1 and j >= x-1:
                    if piste == " ":
                        ruutu = [j, i]
                        if ruutu not in lista:
                            lista.append(ruutu)
                    else:
                        lisaa_ruutu(j, i, piste)
    return lista

def tulvataytto(maa, x, y):
    """
Merkitsee planeetalla olevat tuntemattomat alueet turvalliseksi siten, että
täyttö aloitetaan annetusta x, y -pisteestä.
"""
    lista=[]
    ruutu = [x , y]
    lista.append(ruutu)
    for k in range(len(maa)):
        for l in range(len(maa[k])):
            kord_x = lista[0][0]
            kord_y = lista[0][1]
            if maa[kord_y][kord_x] == " ":
                maa[kord_y][kord_x] = "0"
                lista = laske_miinat(kord_x, kord_y, maa, lista)
                lisaa_ruutu(kord_x, kord_y, maa[kord_y][kord_x])
                lista.pop(0)

def kasittele_hiiri(x, y, painike, muokkaus):
    """
    Tätä funktiota kutsutaan kun käyttäjä klikkaa sovellusikkunaa hiirellä.
    Tulostaa hiiren sijainnin sekä painetun napin terminaaliin.
    """
    if hiiri[painike] == "vasen":
        klikit["lukumäärä"] += 1
        print("klikkien lkm:", klikit["lukumäärä"])
        tulvataytto(tila["kentta"], int(x / 40), int(y / 40))
    elif hiiri[painike] == "oikea":
        if [int(x / 40), int(y / 40), "f"] in piirretyt_ruudut["kentta"]:
            z = piirretyt_ruudut["kentta"].index([int(x / 40), int(y / 40), "f"])
            piirretyt_ruudut["kentta"].pop(z)
        elif [int(x / 40), int(y / 40)] in piirretyt_ruudut["kentta"]:
            print("ei voi liputtaa")
        else:
            lisaa_ruutu(int(x / 40), int(y / 40), "f")