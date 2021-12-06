import time as t
import logiikka as l
import haravasto as h
import json

valinnat = {
    "lopetus": "q",
    "uusi": "u",
    "tilastot": "t"
}

def menu():
    print("""
Tervetuloa Miinantallaaja-peliin!
Pelissä on tarkoitus löytää kaikki kentälle piilotetut miinat tutkimalla
kentällä olevia ruutuja.

Hiiren vasemmalla näppäimellä voit tutkia ruutuja ja oikealla liputtaa miinoja.
Peli päättyy voittoon, jos löydät kaikki miinat. 
Peli päättyy häviöön, jos klikkaus osuu miinaan.

Aloittaaksesi uuden pelin, paina U.
Lopettaaksesi, paina Q.
Jos haluat katsella tilastojasi, paina T.
    """)
    while True:
        valinta = str(input("Ole hyvä ja valitse, mitä haluat tehdä: ")).strip().lower()
        if valinta == valinnat["uusi"]:
            break
        elif valinta == valinnat["tilastot"]:
            #tähän pitää kehittää tiedostolle semmonen juttu, joka tallentaa
            #pelistä pelin ajankohdatn (pvm+klo), keston minuuteissa, keston vuoroissa (klikkausten lkm??)
            #ja lopputuloksen (voitto/häviö, kentän koko ja miinojen lkm)
            with open("tulokset.txt", "w") as tulos:
                tulos.write("testi")
                tulos.read("tulokset.txt")
            print("testi että tässä tapahtuu jtn")
            h.lopeta()
            break
        #entiiä
        elif valinta == valinnat["lopetus"]:
            h.lopeta()
            break
        else:
            print("Tästä ei tapahdu mitään, kokeile uudestaan.")
