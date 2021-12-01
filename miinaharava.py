import haravasto as h
import random as rand
import os

tila = {
    "kentta": []
}

piirretyt_ruudut = {
    "kentta": []
}

def rand_num(z=1):
    '''Palauttaa satunnaisen kokonaisluvun nollasta z:aan'''
    randomi = int((rand.random() * z))
    return randomi

def luo_kentta(x, y):
    ''' 
    Luo kentän jonka leveys on x ja korkeus y. Palauttaa kentän listana.
'''
    kentta = []
    for i in range(y):
        rivi = []
        for j in range(x):
            rivi.append(" ")
        kentta.append(rivi)
    return kentta
        
def luo_vapaat_ruudut(kentta):
    '''
    Luo listan vapaista ruuduista ja palauttaa sen.
'''
    vapaat_ruudut = []
    for i, rivi in enumerate(kentta):
        for j, ruutu in enumerate(rivi):
            pari = [j, i]
            vapaat_ruudut.append(pari)
    return vapaat_ruudut

def lisaa_piirretty_ruutu(x, y, merkki):
    lista = [x, y, merkki]
    if lista not in piirretyt_ruudut["kentta"]:
        piirretyt_ruudut["kentta"].append(lista)
        
    
def miinoita(kentta, ruudut, miinat):
    """
Asettaa kentälle "miinat" kpl miinoja satunnaisiin paikkoihin.
"""

    for i in range(miinat):
        ruutu = rand_num(len(ruudut) - 1)
        for i, sarake in enumerate(kentta):
            if i == ruudut[ruutu][1]:
                for j, rivi in enumerate(sarake):
                    if j == ruudut[ruutu][0]:
                        kentta[i][j] = "x"
                        
                        luo_numerot(j, i, kentta)
                        
        ruudut.remove(ruudut[ruutu])
        
def luo_numerot(x, y ,kentta):
    """
Laskee annetussa huoneessa yhden ruudun ympärillä olevat ninjat ja palauttaa
niiden lukumäärän. Funktio toimii sillä oletuksella, että valitussa ruudussa ei
ole ninjaa - jos on, sekin lasketaan mukaan.
"""
     
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
        
def laske_miinat(x, y ,huone, lista1):
    """
Laskee annetussa huoneessa yhden ruudun ympärillä olevat ninjat ja palauttaa
niiden lukumäärän. Funktio toimii sillä oletuksella, että valitussa ruudussa ei
ole ninjaa - jos on, sekin lasketaan mukaan.
"""
     
    for i, kolo in enumerate(huone):
        if i <= y+1 and i >= y-1:
            for j, piste in enumerate(kolo):
                if j <= x+1 and j >= x-1:
                    if piste == " ":
                        ruutu = [j, i]
                        if ruutu not in lista1:
                            lista1.append(ruutu)
                    elif piste != "f":
                        lisaa_piirretty_ruutu(j, i, piste)


    return lista1
    
def kasittele_hiiri(x, y, painike, muokkaus):
    """
    Tätä funktiota kutsutaan kun käyttäjä klikkaa sovellusikkunaa hiirellä.
    Tulostaa hiiren sijainnin sekä painetun napin terminaaliin.
    """
    if h.HIIRI_VASEN:
        tulvataytto(kentta, int(x / 40), int(y / 40))
    elif h.HIIRI_OIKEA:
        lisaa_piirretty_ruutu(int(x / 40), int(y / 40), "f")
        print("OIKEAPAINKI")

def piirra_kentta():
    """
Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
ruudun näkymän päivitystä.
"""
    h.tyhjaa_ikkuna()
    h.piirra_tausta()
    h.aloita_ruutujen_piirto()
    for i, sarake in enumerate(tila["kentta"]):
        for j, rivi in enumerate(sarake):
                h.lisaa_piirrettava_ruutu(" ", j * 40, i * 40)
    for k in piirretyt_ruudut["kentta"]:
        if k[2] != "x":
            h.lisaa_piirrettava_ruutu(k[2], k[0] * 40, k[1] * 40)
    
    h.piirra_ruudut()

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
            if maa[lista[0][1]][lista[0][0]] == " ":
                maa[lista[0][1]][lista[0][0]] = "0"
                lista = laske_miinat(lista[0][0], lista[0][1], maa, lista)
                lisaa_piirretty_ruutu(lista[0][0], lista[0][1], maa[lista[0][1]][lista[0][0]])
                lista.pop(0)


def main():
    """
    Lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän.
    """
    path = os.getcwd() + "\spritet"
    h.lataa_kuvat(path)
    h.luo_ikkuna(len(kentta[1] * 40), len(kentta * 40))
    h.aseta_piirto_kasittelija(piirra_kentta)
    h.aseta_hiiri_kasittelija(kasittele_hiiri)
    h.aloita()
    
if __name__ == "__main__":
    kentta = luo_kentta(9, 9)
    vapaat_ruudut = luo_vapaat_ruudut(kentta)
    piirra_kentta()
    miinoita(kentta, vapaat_ruudut, 5)
    tila["kentta"] = kentta
    for i in tila["kentta"]:
        print(i)
    main()
    piirra_kentta()
    
    
