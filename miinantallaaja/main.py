import time
import logiikka as l
import kentta as k
import haravasto as h
import peli as p

#Tätä miinantallaaja-peliä ovat tehneet: Jeremias Nevalainen ja Jere Jacklin.

def main():
    """
    Lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän.
    """
    h.lataa_kuvat("spritet")
    h.luo_ikkuna(len(kentta[1] * 40), len(kentta * 40))
    h.aseta_piirto_kasittelija(k.piirra_kentta)
    h.aseta_hiiri_kasittelija(l.kasittele_hiiri)
    h.aseta_toistuva_kasittelija(l.toistuva_kasittelija)
    h.aloita()

def tallenna_tiedostoon(kesto, lopputulos, klikit):
    """
    Tallentaa pelin tulokset tiedostoon tulokset.txt 
    """
    with open("tulokset.txt", "a") as tulos:
        tulos.write("Aloitusaika: {}   Kesto: {}s   Miinojen määrä: {}   Kentän koko: {}x{}   Tulos: {} Klikkausten määrä: {}\n".format(
            l.tallennus["aloitus_aika"], 
            kesto, 
            l.tallennus["miinat"],  
            l.tallennus["kentan_koko"][0],
            l.tallennus["kentan_koko"][1], 
            lopputulos, 
            klikit
            ))

def kysy_numeroa(teksti):
    try:
        syote = int(input(teksti))
    except ValueError:
        print("Ole hyvä ja anna kokonaisluku.")
    return syote

if __name__ == "__main__":
    p.menu()
    while True:
        leveys = kysy_numeroa("Ole hyvä ja anna kentän leveys: ")
        korkeus = kysy_numeroa("Ole hyvä ja anna kentän korkeus: ")
        miinat = kysy_numeroa("Ole hyvä ja anna miinojen määrä: ")
        if leveys < 3 or korkeus < 3:
            print("Kenttä liian pieni, yritä uudestaan.")
        elif leveys > 20 or korkeus > 20:
            print("Kenttä liian suuri, yritä uudestaan.")
        else:
            break
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