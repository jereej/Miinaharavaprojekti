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
    
    valinta = str(input("Ole hyvä ja valitse, mitä haluat tehdä: ")).strip().lower()
    if valinta == valinnat["uusi"]:
        pass
    elif valinta == valinnat["tilastot"]:
        with open("tulokset.txt", "r") as tulos:
            t = tulos.read()
            print(t)
        input("Paina mitä tahansa näppäintä palataksesi alkuvalikkoon.")
        menu()
    elif valinta == valinnat["lopetus"]:
        exit()
    else:
        print("Tästä ei tapahdu mitään, kokeile uudestaan.")
        menu()


