import logiikka as l
import kentta as k
import haravasto as h
import peli as p
import os
import time

def main():
    """Funktio luo peli-ikkunan, asettaa piirron ja hiiren käsittelijät
    sekä aloittaa pelin."""

    h.lataa_kuvat("spritet")
    h.luo_ikkuna(len(kentta[1] * 40), len(kentta * 40))
    h.aseta_piirto_kasittelija(k.piirra_kentta)
    h.aseta_hiiri_kasittelija(l.kasittele_hiiri)
    h.aloita()

def tallenna_tiedostoon(kesto, lopputulos, klikit):
    """Funktio tallentaa pelatun pelin tiedot tiedostoon. Aikaisemmat pelit myös näkyvät tiedostossa."""
    with open("tulokset.txt", "a") as tulos:
        tulos.write("Aloitusaika: {}   Kesto: {} min   Miinojen määrä: {}   Kentän koko: {}x{}   Tulos: {} Klikkausten määrä: {}\n".format(
            l.tallennus["aloitus_aika"], 
            kesto, 
            l.tallennus["miinat"],  
            l.tallennus["kentan_koko"][0],
            l.tallennus["kentan_koko"][1], 
            lopputulos, 
            klikit
            ))




if __name__ == "__main__":
    p.menu()
    try:
        leveys = int(input("Ole hyvä ja anna kentän leveys: "))
        korkeus = int(input("Ole hyvä ja anna kentän korkeus: "))
        miinat = int(input("Ole hyvä ja anna miinojen määrä: "))
    except ValueError:
        print("Ole hyvä ja anna kokonaisluku.")
    kentta = k.luo_kentta(leveys, korkeus)
    vapaat_ruudut = k.luo_vapaat_ruudut(kentta)
    l.miinoita(kentta, vapaat_ruudut, miinat)
    l.tila["kentta"] = kentta
    aloitus_aika = time.strftime("%d.%m.%Y  klo %H:%M:%S")
    l.tallennus["aloitus_aika_s"] = time.time()
    l.tallennus["aloitus_aika"] = aloitus_aika
    l.tallennus["kentan_koko"] = [leveys, korkeus]
    l.tallennus["miinat"] = miinat
    main()
    k.piirra_kentta()


    