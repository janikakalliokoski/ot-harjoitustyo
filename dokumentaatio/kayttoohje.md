### Käyttöohje
Lataa projektin viimeisimmän [releasen](https://github.com/janikakalliokoski/ot-harjoitustyo/releases/tag/viikko5) lähdekoodi valitsemalla *Assets*-osion alta *Source code*.
## Ohjelman käynnistäminen
1. Asenna riippuvuudet komennolla poetry install
2. Suorita alustustoimenpiteet komennolla poetry run invoke build
3. Nyt ohjelman voi käynnistää komennolla poetry run invoke start

## Kirjautuminen
Sovellus käynnistyy kirjautumisnäkymään:

![Screenshot]

Jos on olemassaoleva käyttäjätunnus, tunnus ja salasana kirjoitetaan syötekenttiin ja painamalla "Login"-painiketta, pääsee kirjautumaan sisään.
## Uuden käyttäjän luominen
Kirjautumisnäkymästä voi siirtyä uuden käyttäjän luomisnäkymään painamalla painiketta "Create user".

![Screenshot]

Uusi käyttäjä luodaan syöttämällä tiedot syötekenttiin ja painamalla "Create"-painiketta. Jos käyttäjä luotiin onnistuneesti, saa käyttäjä tästä ilmoituksen, ja vastaavasti virhetilanteissa käyttäjä saa ilmoituksen.
Takaisin kirjautumisnäkymään siirrytään painamalla painiketta "Back".
## Arvosteluiden lista
Sisäänkirjautumisen jälkeen siirrytään käyttäjän luomien arvosteluiden listaavaan näkymään:

***kesken***

Näkymästä voi kirjautua ulos painamalla painiketta "Log out", joka vie takaisin kirjautumisnäkymään. 
Painamalla painiketta "Create review" siirrytään näkymään, jossa voidaan luoda arvostelu ravintolasta.
## Arvosteluiden luonti
![Screenshot]

Ravintolan nimi ja arvostelu kirjoitetaan syötekenttiin. Jos kentät ovat tyhjät, saa käyttäjä tästä ilmoituksen.
Painamalla painiketta "Back" pääsee takaisin listaan arvosteluista.
