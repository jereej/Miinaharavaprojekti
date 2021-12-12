import logiikka as l
import haravasto as h

def luo_kentta(x, y):
    """ Luo kentän jonka leveys on x ja korkeus y. Palauttaa kentän listana."""
    kentta = []
    for i in range(y):
        rivi = []
        for j in range(x):
            rivi.append(" ")
        kentta.append(rivi)
    return kentta

def luo_vapaat_ruudut(kentta):
    """Luo listan vapaista ruuduista ja palauttaa sen."""
    vapaat_ruudut = []
    for i, rivi in enumerate(kentta):
        for j, ruutu in enumerate(rivi):
            pari = [j, i]
            vapaat_ruudut.append(pari)
    return vapaat_ruudut

def piirra_kentta():
    """
Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
ruudun näkymän päivitystä.
"""
    h.tyhjaa_ikkuna()
    h.piirra_tausta()
    h.aloita_ruutujen_piirto()
    for i, sarake in enumerate(l.tila["kentta"]):
        for j, rivi in enumerate(sarake):
            h.lisaa_piirrettava_ruutu(" ", j * 40, i * 40)
    for k in l.piirretyt_ruudut["kentta"]:
        h.lisaa_piirrettava_ruutu(k[2], k[0] * 40, k[1] * 40)
    for m in l.tila["liput"]:
        h.lisaa_piirrettava_ruutu("f", m[0] * 40, m[1] * 40)
    h.piirra_ruudut()
    for j in l.piirretyt_ruudut["teksti"]:
        h.piirra_tekstia(j[2], j[0], j[1])