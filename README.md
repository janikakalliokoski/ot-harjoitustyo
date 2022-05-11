# Ravintoloiden arvostelusovellus

Sovellus, jossa käyttäjä voi kirjata ylös missä ravintoloissa on käynyt ja antaa niille arvostelut sekä nähdä muiden käyttäjien luomat arvostelut ravintoloista.

## Release
[linkki release1](https://github.com/janikakalliokoski/ot-harjoitustyo/releases/tag/viikko5):seen

[linkki release2](https://github.com/janikakalliokoski/ot-harjoitustyo/releases/tag/viikko6):seen

## Dokumentaatio

[vaatimusmaarittely.md](https://github.com/janikakalliokoski/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[tyoaikakirjanpito.md](https://github.com/janikakalliokoski/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[changelog.md](https://github.com/janikakalliokoski/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[arkkitehtuuri.md](https://github.com/janikakalliokoski/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[kayttoohje.md](https://github.com/janikakalliokoski/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

### ⚠️ TÄRKEÄ: Python version täytyy olla vähintään 3.8.12., jotta sovelluksen voi käynnistää.

## Asennus

1. asenna riippuvuudet komennolla:
```bash
poetry install
```
2. suorita vaadittavat alustustoimenpiteet komennolla: 
```bash 
poetry run invoke build
```
3. käynnistä sovellus komennolla:
```bash
 poetry run invoke start
 ```

## Komentorivitoiminnot

1. Ohjelman voi suorittaa komennolla:
```bash
 poetry run invoke start
 ```
2. Testit voi suorittaa komennolla:
```bash
 poetry run invoke test
 ```
3. Testikattavuuden saa komennolla:
```bash
 poetry run invoke coverage-report
 ```
4. Koodin voi automaattisesti formatoida komennolla:
```bash
 poetry run invoke format
 ```
5. Pylintin laatutarkistuksen saa komennolla:
```bash
 poetry run invoke lint
 ```
