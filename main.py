meme_dict = {
    "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
    "LOL": "Una risposta comune a qualcosa di divertente ed è inteso per (laughing over limits) stai ridendo oltre i limiti",
    "OMG": "Sostanzialmente vuol dire (oh mio dio) solo che è abbreviato e in inglese",
    "BRO": "Abbreviazione che significa brother(fratello) che in italiano si traduce (fra) spesso questo termine è un pò disprezzato dagli adulti",
    "LMAO": "una specie di sinonimo di LOL però qui significa (laughing my ass off) leggermente volgare ma significa che stai ridendo così tanto che ti fa male il fondoschiena",
    "XD": "Letteralmente una faccina che ride con gli occhi chiusi dal ridere usata spesso quando qualcosa è divertente, può essere un'altra alternativa a LOL",
    "CREEPY": "qualcosa di spaventoso,inquietante",
    "SHEESH": "una leggera disapprovazione",
    "BRUH": "usato quando si assiste ad una leggera delusione",
    "CAP": "quando vuoi esprimere che pensi che qualcuno stia mentendo o dicendo qualcosa di falso o poco credibile",
    "CHILL": "espressione usata per dire che si è calmi o rilassati/freschi come un ghiacciolo",
    
}


while True:
    parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")
    if parola in meme_dict.keys():
        print(parola, meme_dict[parola])
        # Cosa fare se la parola è stata trovata?
    else:
        print("la parola inserita non è presente all'interno del mio database")
        # Cosa fare se la parola non è stata trovata?
    
    x = input("Vuoi continuare? y or n")
    if x == "n":
        print("Arrivederci!")
        break
