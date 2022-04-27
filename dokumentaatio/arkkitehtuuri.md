# Arkkitehtuurikuvaus
## Rakenne
Ohjelman osien suhdetta kuvaava pakkauskaavio:
![Screenshot](./kuvat/arkkitehtuuri.png)

Pakkaus *ui* sisältää käyttöliittymästä, *services* sovelluslogiikasta ja *repositories* tietojen pysyväistallennuksesta vastaavan koodin. Pakkaus *entities* sisältää luokat *User* ja *Review*, jotka kuvastavat sovelluksen käyttämiä tietokohteita.
## Käyttöliittymä
Käyttöliittymä sisältää neljä erillistä näkymää:
- kirjautuminen
- uuden käyttäjän luonti
- lista arvosteluista
- uuden arvostelun luonti

Nämä kaikki on toteutettu omana luokkanaan, ja näkymistä yksi on kerrallaan näkyvissä. Näkymien välillä vaihtamisesta vastaa [UI](https://github.com/janikakalliokoski/ot-harjoitustyo/blob/master/src/ui/ui.py)-luokka. Käyttöliittymä on eriytetty sovellusluokasta, ja se ainoastaan kutsuu [ReviewService](https://github.com/janikakalliokoski/ot-harjoitustyo/blob/master/src/services/service.py)-luokan metodeja
## Tietojen pysyväistallennus
Pakkauksen *repositories* luokka UserRepository huolehtii tietojen tallettamisesta, ja tallentaa tietoa SQLite-tietokantaan.
### Tiedostot
Käyttäjät tallennetaan SQLite-tietokantaan users, joka alustetaan [initialize_database.py](https://github.com/janikakalliokoski/ot-harjoitustyo/blob/master/src/initialize_database.py)-tiedostossa.
## Päätoiminnallisuudet
Sekvenssikaavio käyttäjän sisäänkirjautumisesta:
![Screenshot](./kuvat/login_sekvenssi.png)
Kirjautumisnäkymässä kenttiin kirjoitetaan tunnus ja salasana, ja klikataan "Login" painiketta, ja tapahtumankäsittelijä kutsuu sovelluslogiikan ReviewService:n avulla, onko käyttäjätunnusta olemassa, ja jos on, niin täsmääkö salasana. Jos tunnus ja salasana täsmäävät, kirjautuminen onnistuu ja käyttöliittymä vaihtaa näkymäksi ReviewsView:n.

Sekvenssikaavio käyttäjän luomisesta:
