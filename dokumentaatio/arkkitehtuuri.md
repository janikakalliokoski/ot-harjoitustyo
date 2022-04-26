Ohjelman osien suhdetta kuvaava pakkauskaavio:
![Screenshot](./kuvat/arkkitehtuuri.png)

## Päätoiminnallisuudet
Sekvenssikaavio käyttäjän sisäänkirjautumisesta:
![Screenshot](./kuvat/login_sekvenssi.png)
Kirjautumisnäkymässä kenttiin kirjoitetaan tunnus ja salasana, ja klikataan "Login" painiketta, ja tapahtumankäsittelijä kutsuu sovelluslogiikan ReviewService:n avulla, onko käyttäjätunnusta olemassa, ja jos on, niin täsmääkö salasana. Jos tunnus ja salasana täsmäävät, kirjautuminen onnistuu ja käyttöliittymä vaihtaa näkymäksi ReviewsView:n.
