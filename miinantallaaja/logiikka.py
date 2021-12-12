import random as rand
from time import time
import haravasto as h
from main import tallenna_tiedostoon

tila = {
    "kentta": [],
    "miinat": [],
    "liput": []
}

tallennus = {
    "aloitus_aika": " ",
    "aloitus_aika_s": 0,
    "kesto": 0,
    "kentan_koko": [0, 0],
    "klikkaukset": 0,
    "miinat": 0,
    "lopputulos": " "
}

piirretyt_ruudut = {
    "kentta": [],
    "xy" : [],
    "teksti" : []
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
    """Palauttaa satunnaisen kokonaisluvun nollasta z:aan"""
    luku = int((rand.random() * z))
    return luku

def lisaa_ruutu(x, y, merkki):
    """Lisää annetun ruudun piirretyihin tuuruihin, sekä lisää annetun ruudun kordinaatit 
    piirrettyjen ruutujen xy listaan."""
    lista = [x, y, merkki]
    if lista not in piirretyt_ruudut["kentta"]:
        piirretyt_ruudut["kentta"].append(lista)
    xy = [x, y]
    if xy not in piirretyt_ruudut["xy"]:
        piirretyt_ruudut["xy"].append(xy)

def luo_numerot(x, y, kentta):
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
    for k in range(miinat):
        ruutu = rand_num(len(ruudut) - 1)
        for i, sarake in enumerate(kentta):
            if i == ruudut[ruutu][1]:
                for j, rivi in enumerate(sarake):
                    if j == ruudut[ruutu][0]:
                        kentta[i][j] = "x"
                        luo_numerot(j, i, kentta)
                        tila["miinat"].append([j, i])
                        
        ruudut.remove(ruudut[ruutu])

def laske_miinat(x, y, alue, lista):
    """
    Laskee ruudun ympärillä olevat tyhjät ruudut ja lisää ne listaan. Palauttaa täydennetyn listan.
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
Merkitsee kentällä olevat tuntemattomat alueet tunnetuiksi siten, että
täyttö aloitetaan annetusta x, y -pisteestä.
"""
    lista = [(x, y)]
    while len(lista) > 0:
        kord_x = lista[0][0]
        kord_y = lista[0][1]
        if maa[kord_y][kord_x] == " ":
            maa[kord_y][kord_x] = "0"
            lista = laske_miinat(kord_x, kord_y, maa, lista)
            lisaa_ruutu(kord_x, kord_y, maa[kord_y][kord_x])
            lista.pop(0)
        elif maa[kord_y][kord_x] != "0":
            if maa[kord_y][kord_x] == "x":
                lisaa_ruutu(kord_x, kord_y, maa[kord_y][kord_x])
                peli_poikki(False)
                break
            else:
                lisaa_ruutu(kord_x, kord_y, maa[kord_y][kord_x])
                lista.pop(0)

def kasittele_hiiri(x, y, painike, muokkaus):
    """
    Tätä funktiota kutsutaan kun käyttäjä klikkaa sovellusikkunaa hiirellä.
    Tulostaa hiiren sijainnin sekä painetun napin terminaaliin.
    """
    if tallennus["lopputulos"] != " ":
        h.lopeta()
    if hiiri[painike] == "vasen":
        if [int(x / 40), int(y / 40)] not in tila["liput"]:
            if [int(x/40), int(y/40)]not in piirretyt_ruudut["xy"]:
                klikit["lukumäärä"] += 1
                tulvataytto(tila["kentta"], int(x / 40), int(y / 40))
    elif hiiri[painike] == "oikea":
        if [int(x / 40), int(y / 40)] not in piirretyt_ruudut["xy"]:
            if [int(x / 40), int(y / 40)] in tila["liput"]:
                z = tila["liput"].index([int(x / 40), int(y / 40)])
                tila["liput"].pop(z)
            else:
                tila["liput"].append([int(x / 40), int(y / 40)])

def toistuva_kasittelija(aika):
    if len(piirretyt_ruudut["teksti"]) < 1:     
        if len(piirretyt_ruudut["kentta"]) >= tallennus["kentan_koko"][0]*tallennus["kentan_koko"][1]-tallennus["miinat"]:
            peli_poikki(True)

def peli_poikki(voitto):
    """Kutsutaan pelin päättyessä. Tulostaa pelin lopputuloksen komentoikkunaan
     ja pelikentälle."""
    if voitto:
        tallennus["lopputulos"] = "Voitto"
    else:
        tallennus["lopputulos"] = "Häviö"
    tallennus["klikkaukset"] = klikit["lukumäärä"]
    aika = time() - tallennus["aloitus_aika_s"]
    tallenna_tiedostoon(round(aika, 1), tallennus["lopputulos"], klikit["lukumäärä"])
    print("Lopputulos: ", tallennus["lopputulos"], " ajassa: ", round(aika, 1), "s")
    piirretyt_ruudut["teksti"].append([0, 100, "Paina hiiren"])
    piirretyt_ruudut["teksti"].append([0, 50, "näppäintä"])
    piirretyt_ruudut["teksti"].append([0, 0, "poistuaksesi"])
    piirretyt_ruudut["teksti"].append([0, tallennus["kentan_koko"][0]*40 - 50, tallennus["lopputulos"]])