#Napiš skript v Pythonu, který otevře soubor alice.txt 
#(Alice’s Adventures in Wonderland od Lewise Carrolla) - ke stažení 
#v [1] a spočítá četnost (počet výskytů) všech znaků. 
# Velká písmena převeď za malá a ignoruj mezery a znaky 
# nového řádku (ostatní znaky jako čárky nebo závorky zařaď do výsledku).


slovnik = {}
with open("Výuka/alice.txt",encoding="utf-8") as soubor:
    for radek in soubor:
        for znak in radek:
            znak = znak.lower()
            if znak != " " and znak != '\n':
                slovnik[znak] = slovnik.get(znak,0)+1             

import json

with open("Výuka/ukol1_output.json", mode="w", encoding="utf-8") as soubor:
    slovnik = dict(sorted(slovnik.items()))
    json.dump(slovnik,soubor,indent=4,ensure_ascii=False) 
    