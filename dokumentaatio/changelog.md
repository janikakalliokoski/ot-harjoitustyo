# Changelog

## Viikko 3

- alustava käyttöliittymärakenne (login näkymä, create user näkymä, reviews näkymä) ja käyttöliittymille luokat
- lisätty User luokka, missä attribuutteina username & password
- lisätty UserRepository luokka, jossa lisätään tietokantaan uusi käyttäjä ja jossa voi hakea käyttäjän tunnuksen ja salasanan käyttäjänimellä
- testi, mikä testaa onko käyttäjä asetettu tietokantaan

## Viikko 4
- sovelluslogiikka yhdistetty käyttöliittymään käyttäjän luonnin ja sisäänkirjautumisen suhteen
- käyttäjää luodessa sovellus ilmoittaa, jos tunnus tai salasana on liian lyhyt tai jos tunnus on jo olemassa
- kirjautuessa sisään sovellus ilmoittaa, jos käyttäjätunnus tai salasana on virheellinen / sitä ei löydy
- testit, löytyykö kaikki käyttäjät tietokannasta ja löytyykö käyttäjä käyttäjänimellä

## Viikko 5
- kun käyttäjätunnus luodaan, saa käyttäjä tästä ilmoituksen
- testeille oma testitietokanta
- create review näkymä
- virheilmoitukset messageboxeihin

## Viikko 6
- tekstien fontteja ja värjeä muutettu
- arvioille oma tietokanta
- arviot tallentuvat omaan tietokantaansa
- käyttäjä saa virheilmoituksen jos jättää tyhjiksi arvioiden kenttiä

## Viikko 7
- arvostelut näkyvät näkymässä, johon pääsee kun kirjautuu sisään. Arvostelut näkyvät kaikille käyttäjille, ja arvostelussa lukee, mikä käyttäjä on luonut kyseisen arvostelun.
