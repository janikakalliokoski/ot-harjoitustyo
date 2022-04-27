# Ravintoloiden arvostelusovellus

Sovellus, jossa käyttäjä voi kirjata ylös missä ravintoloissa on käynyt ja antaa niille arvostelut

## Release
[linkki release1](https://github.com/janikakalliokoski/ot-harjoitustyo/releases/tag/viikko5)seen

## Dokumentaatio

[vaatimusmaarittely.md](https://github.com/janikakalliokoski/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[tyoaikakirjanpito.md](https://github.com/janikakalliokoski/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[changelog.md](https://github.com/janikakalliokoski/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[arkkitehtuuri.md](https://github.com/janikakalliokoski/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[kayttoohje.md](https://github.com/janikakalliokoski/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

## Asennus
1. asenna riippuvuudet komennolla poetry install
2. suorita vaadittavat alustustoimenpiteet komennolla poetry run invoke start
3. käynnistä sovellus komennolla poetry run invoke start

## Komentorivitoiminnot

1. Ohjelman voi suorittaa komennolla poetry run invoke start
2. Testit voi suorittaa komennolla poetry run invoke test
3. Testikattavuuden saa komennolla poetry run invoke coverage-report
4. Koodin voi automaattisesti formatoida komennolla poetry run invoke format
5. Pylintin laatutarkistuksen saa komennolla poetry run invoke lint
