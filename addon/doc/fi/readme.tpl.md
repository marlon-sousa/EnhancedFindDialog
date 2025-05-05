# Paranneltu Etsi-valintaikkuna ${addon_version}
Paranneltu Etsi-valintaikkuna -lisäosa toteuttaa seuraavat haun parannukset:

* Hakuhistoria
* Haku säännöllisillä lausekkeilla
* Profiilikohtainen haun aloittaminen alusta asiakirjan lopussa
* Profiilikohtainen kirjainkoko
* Tilannekohtaiset tiedot hakujen yhteydessä

## Lataaminen
Lataa [Paranneltu Etsi-valintaikkuna ${addon_version} -lisäosa](https://github.com/marlon-sousa/EnhancedFindDialog/releases/download/${addon_version}/EnhancedFindDialog-${addon_version}.nvda-addon)

## Ominaisuudet

### Hakuhistoria
Nopein tapa päästä tiettyihin kohtiin monilla sivustoilla ja verkkopohjaisissa sovelluksissa on hakutoiminto, jonka näppäinkomento on yleensä Ctrl+NVDA+F.

Etsi-valintaikkuna mahdollistaa haettavan tekstin kirjoittamisen ja kyseisen tekstin seuraavaan esiintymään siirtymisen, mikäli sellainen löytyy.

Saatat usein huomata vierailevasi samoilla sivustoilla useita kertoja saman NVDA-istunnon aikana. Monilla näistä verkkosivuista sinun on etsittävä samaa tekstiä, erityisesti jos se on ainoa tapa päästä nopeasti kyseisellä sivulla olevaan linkkiin tai osioon.

Tämä pätee erityisesti sellaisten henkilöiden kohdalla, jotka työskentelevät päivittäin verkkopohjaisten järjestelmien parissa.

Valitettavasti NVDA ei säilytä luetteloa aiemmista hakusanoista. Tämä hidastaa tuottavuutta, koska ellet etsi täsmälleen samaa hakusanaa kuin edellisellä kerralla, sinun on kirjoitettava se uudelleen.

Tämä lisäosa säilyttää hakuhistorian niin kauan kuin NVDA on käynnissä. Joten voit suorittaa uuden haun vain avaamalla Etsi-valintaikkunan ja valitsemalla aiemmin haetun hakusanan painamalla alanuolinäppäintä.

Voit tietenkin myös kirjoittaa uusia hakusanoja. Ne näkyvät luettelossa seuraavalla Etsi-valintaikkunan avaamiskerralla.

#### Miten se toimii?

Kun tämä lisäosa on käytössä, voit liikkua Etsi-valintaikkunassa hakukentän aiempien hakusanojen luettelossa painamalla ylä- ja alanuolinäppäimiä.

Voit kirjoittaa uuden hakusanan tavalliseen tapaan milloin tahansa.

### Haku säännöllisillä lausekkeilla

Tämän lisäosan avulla voit käyttää NVDA:n tavallisen haun lisäksi myös säännöllisiin lausekkeisiin perustuvaa hakua. Lisätietoa säännöllisistä lausekkeista löydät esimerkiksi [Pythonin säännöllisten lausekkeiden oppaasta (englanniksi)](https://docs.python.org/3/howto/regex.html), mutta internetissä on saatavilla myös monia muita aihetta käsitteleviä oppaita.

Säännölliset lausekkeet ovat erityisen hyödyllisiä silloin, kun haluat etsiä verkkosivulta tekstiä, jonka kirjoitusasu vaihtelee.

Tämä asetus on profiilikohtainen, eli voit ottaa sen käyttöön yhdessä profiilissa ja pitää sen poissa käytöstä toisessa.

Huom: Teknisten toteutuserojen vuoksi tämä toiminto ei ole käytettävissä kaikkialla, missä NVDA:n hakua tuetaan (esim. Microsoft Word -asiakirjoissa).

#### Miten se toimii?

Kun tämä lisäosa on käytössä, NVDA:n Etsi-valintaikkunassa näkyy uusi valintaryhmä nimeltä Haun tyyppi, jossa on kaksi vaihtoehtoa:

* **Tavallinen** suorittaa NVDA:n oletushakutoiminnon.

* **Säännöllinen lauseke** suorittaa haun säännöllisillä lausekkeilla. Kirjoita tekstikenttään haluamasi säännöllinen lauseke, ja NVDA siirtää kohdistuksen seuraavaan osumaan.


Valinnan muuttaminen ja haun suorittaminen tallentaa uuden tilan (tavallinen tai säännöllinen lauseke) käytössä olevaan profiiliin. Jos peruutat haun, valinta ei tallennu profiiliin, vaikka olisit muuttanut haun tyyppiä ennen peruutusta.

### Jatka hakua alusta

Jatka hakua alusta on toiminto, joka ei käytössä ollessaan ota huomioon nykyistä tekstikohtaa hakuja suoritettaessa.

Tämä tarkoittaa, että jos etsit jotain, mitä ei löydy nykyisen sijaintisi alapuolelta, haku suoritetaan tekstin alusta , jolloin hakusanaa etsitään koko tekstistä.

Tämä on erityisen tärkeää verkkopohjaisten järjestelmien parissa työskenteleville, jotka tarvitsevat mahdollisuuden tiettyjen painikkeiden tai tekstien löytämiseen sivun senhetkisestä kohdasta riippumatta.

Tämä asetus on profiilikohtainen, mikä tarkoittaa, että voit käyttää profiilia, jossa se on käytössä, ja toista profiilia, jossa se ei ole käytössä.

#### Miten se toimii?

Kun tämä lisäosa on käytössä, Etsi-valintaikkunassa on "Jatka hakua alusta" -valintaruutu.

Kun se on valittuna:

1. Jos etsimäsi hakusana löytyy senhetkisen sijaintisi alapuolelta, kohdistus siirretään kyseiseen kohtaan.
2. Jos etsimääsi hakusanaa ei löydy senhetkisen sijaintisi alapuolelta, sitä etsitään yläpuolelta.
3. Jos hakusana löytyy, lisäosa ilmoittaa lyhyellä merkkiäänellä, että löydetty teksti on senhetkisen sijainnin yläpuolella ja kohdistus siirretään sen kohdalle.
4. Jos hakusanaa ei löydy, siitä näytetään ilmoitus.

Valintaruudun tila tallennetaan käytössä olevaan profiiliin hakutoiminnon suorittamisen yhteydessä. Jos haku peruutetaan, muutoksia ei tallenneta, vaikka valintaruudun tilaa olisi vaihdettu.

### Sama kirjainkoko

NVDA tarjoaa jo "Sama kirjainkoko" -valintaruudun, jotta hakuja voidaan tehdä kirjainkoosta riippumatta. Tämä lisäosa laajentaa kyseistä toiminnallisuutta tallentamalla valintaruudun tilan käytössä olevaan profiiliin, joten voit luoda profiileja, joissa tämä on määritetty eri tavalla.

#### Miten se toimii?

Kun muutat "Sama kirjainkoko" -valintaruudun tilaa ja suoritat haun, uusi tila (valittu tai ei valittu) tallennetaan aktiiviseen profiiliin. Jos peruutat haun, muutosta ei tallenneta, vaikka olisit muuttanut valintaruudun tilaa.

### Hakujen tilannekohtaiset tiedot

Tavallisesti NVDA siirtää kohdistimen haetun sanan kohdalle ja lukee siitä eteenpäin rivin loppuun.

Tämä on ongelmallista suoritettaessa useita hakuja NVDA+F3-näppäinkomennolla, koska kuulet aina ensin vain käyttämäsi hakusanan, vaikka tiedät jo mikä se on.

Tämä lisäosa parantaa käytettävyyttä siten, että kun hakusana  löytyy, NVDA lukee koko rivin alusta alkaen, vaikka kohdistin siirretään edelleen itse hakusanan kohdalle. Näin saat heti tiedon, missä yhteydessä hakusana esiintyy.

Oletetaan, että etsit sanaa Marlon, koska haluat löytää painikkeen nimeltä Target Marlon. Et halua hakea pelkkää "target"-sanaa, koska muita vastaavia painikkeita voi olla useita.

Alla on esimerkkiteksti:

Delete Marlon comments

Reply directly to Marlon

Report Marlon as spammer

Target Marlon on a response

Ilman tätä lisäosaa kuulisit haun suoritettuasi esimerkiksi vain:

Marlon comments

Marlon

Marlon as spammer

Marlon on a response

Tämä hidastaa käyttöä, koska et saa heti tietoa siitä, missä yhteydessä "Marlon" esiintyy.

Tätä lisäosaa käytettäessä NVDA lukee jokaisen rivin alusta alkaen:

Delete Marlon comments

Reply directly to Marlon

Report Marlon as spammer

Target Marlon on a response

Jos painat nopeasti NVDA+F3, kuulet jokaisen rivin alun, mikä mahdollistaa sen, että voit painaa Enteriä heti kuullessasi oikean rivin alun (esim. "Target"), tietäen että "Marlon" esiintyy myöhemmin kyseisellä rivillä.

#### Miten se toimii?

Kun tämä lisäosa on käytössä, NVDA lukee aina koko rivin, vaikka kohdistin siirretään löytyneen hakusanan kohdalle.

Edellistä esimerkkiä käyttääksemme kuulisit ensimmäisellä hakukerralla:

Delete Marlon comments

Jos jatkat NVDA+F3:n painamista, kuulet:

Reply directly to Marlon

Report Marlon as spammer

Target Marlon on a response

Jos siis painat toistuvasti NVDA+F3, kuulet jokaisen rivin alun, mikä auttaa nopeasti löytämään halutun kohdan ja painamaan Enteriä oikeassa kohdassa.

## Kehitykseen osallistuminen ja kääntäminen eri kielille

Mikäli haluat osallistua tämän lisäosan kehitykseen tai kääntää sen jollekin kielelle, mene [projektin koodivarastoon](https://github.com/marlon-sousa/EnhancedFindDialog) ja katso ohjeet tiedostosta contributing.md, joka löytyy englanninkielisen dokumentaation hakemistosta.

## Osallistujat

Erityiskiitokset seuraaville:


* Ângelo Miguel Abrantes - portugalinkielinen käännös
* Rémy Ruiz - ranskankielinen käännös
* Rémy Ruiz - espanjankielinen käännös
* Tarik Hadžirović - kroaatinkielinen käännös
*  Thiago Seus - brasilianportugalinkielinen käännös, NVDA 2024.1 -yhteensopivuus
* Umut KORKMAZ - turkinkielinen käännös
* Valentin Kupriyanov - venäjänkielinen käännös
* Ivan Shtefuriak - ukrainankielinen käännös
* Jani Kinnunen - suomenkielinen käännös
* Leonardo Marenda - italiankielinen käännös
