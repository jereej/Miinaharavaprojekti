import logiikka as l
import kentta as k
import haravasto as h
import os

def main():
    """
    Lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän.
    """
    path = os.getcwd() + "\spritet"
    h.lataa_kuvat(path)
    h.luo_ikkuna(len(kentta[1] * 40), len(kentta * 40))
    h.aseta_piirto_kasittelija(k.piirra_kentta)
    h.aseta_hiiri_kasittelija(l.kasittele_hiiri)
    h.aloita()

if __name__ == "__main__":
    kentta = k.luo_kentta(9, 9)
    vapaat_ruudut = k.luo_vapaat_ruudut(kentta)
    l.miinoita(kentta, vapaat_ruudut, 5)
    l.tila["kentta"] = kentta
    main()
    k.piirra_kentta()
    