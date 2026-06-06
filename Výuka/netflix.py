#V tomto úkolu budeš pracovat se souborem netflix_titles.tsv. 
#Jedná se o textový soubor ve formátu TSV (Tabulator Separated Values), 
#kde jsou jako oddělovače sloupců použity tabulátory (“\t”).
#Tvým úkolem bude soubor načíst, vytáhnout z něj některé údaje a 
#uložit je ve formátu JSON.
#Z každého řádku nás budou zajímat tyto údaje: 
#PRIMARYTITLE (název),DIRECTOR (režisér/režiséři),CAST (herci),GENRES (seznam žánrů),STARTYEAR (rok vydani).
#Údaje o filmech převeď do seznamu, kde bude každý film reprezentován 
#jako slovník obsahující následující položky:
#title (název filmu),directors (seznam všech režisérů nebo prázdný seznam, 
#pokud není režisér uveden),cast (seznam všech herců nebo prázdný seznam, 
#pokud není žádný herec uveden), genres (seznam všech žánrů, 
#do kterých byl film zařazen),decade (dekáda, ve které film vznikl).


import json
netflix = []

with open("Výuka/netflix_titles.tsv",encoding="utf-8") as soubor:
    netflix_prehled = soubor.readlines()


#next(netflix_prehled)
for radek in netflix_prehled[1:]:
  seznam = radek.split("\t")
  primarytitle = seznam[2]
  director = seznam[15]
  if director == "":
    director = []
  else:
     director = director.split(", ")
  cast = seznam[16]
  if cast == "":
    cast = []
  else:
     cast = cast.split(", ")
  genres = seznam[8]
  if genres == "":
    genresenres = []
  else:
    genres = genres.split(", ")
  startyear = int(seznam[5])
  decade = (startyear//10)*10
  filmy = {
           "title": primarytitle,
           "directors": director,
           "cast": cast,
           "genres": genres,
           "decade": decade
           }
  netflix.append(filmy)     
     



with open("Výuka/movies.json", mode="w", encoding="utf-8") as soubor:
    json.dump(netflix,soubor,indent=4,ensure_ascii=False) 