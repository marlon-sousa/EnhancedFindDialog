# Paranneltu Etsi-valintaikkuna 1.5.0
Paranneltu Etsi-valintaikkuna -lisäosa toteuttaa seuraavat haun parannukset:

* Hakuhistoria
* Profiilikohtainen haun aloittaminen alusta asiakirjan lopussa
* Profiilikohtainen kirjainkoko
* Tilannekohtaiset tiedot hakujen yhteydessä

## Lataaminen
Lataa [Paranneltu Etsi-valintaikkuna 1.5.0 -lisäosa](https://github.com/marlon-sousa/EnhancedFindDialog/releases/download/1.5.0/EnhancedFindDialog-1.5.0.nvda-addon)

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

Asenna lisäosa. Kun se on otettu käyttöön, voit liikkua Etsi-valintaikkunassa hakukentän aiempien hakusanojen luettelossa painamalla ylä- ja alanuolinäppäimiä.

Voit kirjoittaa uuden hakusanan tavalliseen tapaan milloin tahansa.

### Jatka hakua alusta

Jatka hakua alusta on toiminto, joka ei käytössä ollessaan ota huomioon nykyistä tekstikohtaa hakuja suoritettaessa.

Tämä tarkoittaa, että jos etsit jotain, mitä ei löydy nykyisen sijaintisi alapuolelta, haku suoritetaan tekstin alusta , jolloin hakusanaa etsitään koko tekstistä.

Tämä on erityisen tärkeää verkkopohjaisten järjestelmien parissa työskenteleville, jotka tarvitsevat mahdollisuuden tiettyjen painikkeiden tai tekstien löytämiseen sivun senhetkisestä kohdasta riippumatta.

Tämä asetus on profiilikohtainen, mikä tarkoittaa, että voit käyttää profiilia, jossa se on käytössä, ja toista profiilia, jossa se ei ole käytössä.

#### Miten se toimii?

Asenna lisäosa. Kun se on käytössä, Etsi-valintaikkunassa on "Jatka hakua alusta" -valintaruutu.

Kun se on valittuna:

1. Jos etsimäsi hakusana löytyy senhetkisen sijaintisi alapuolelta, kohdistus siirretään kyseiseen kohtaan.
2. Jos etsimääsi hakusanaa ei löydy senhetkisen sijaintisi alapuolelta, sitä etsitään yläpuolelta.
3. Jos hakusana löytyy, lisäosa ilmoittaa lyhyellä äänimerkillä, että löydetty teksti on senhetkisen sijainnin yläpuolella ja kohdistus siirretään sen kohdalle.
4. Jos hakusanaa ei löydy, siitä näytetään ilmoitus.

Tämän valintaruudun tilan muuttaminen ja haun suorittaminen tallentavat uuden tilan (valittu tai ei valittu) käytössä olevaan profiiliin. Haun peruuttaminen ei muuta valintaruudun tilaa käytössä olevassa profiilissa, vaikka muuttaisit sitä ennen haun peruuttamista.

### Sama kirjainkoko

NVDA tarjoaa jo "Sama kirjainkoko" -valintaruudun, jotta hakuja voidaan tehdä kirjainkoosta riippumatta. Tämä lisäosa laajentaa kyseistä toiminnallisuutta tallentamalla valintaruudun tilan käytössä olevaan profiiliin, joten voit luoda profiileja, joissa tämä on määritetty eri tavalla.

#### Miten se toimii?

Asenna lisäosa. "Sama kirjainkoko" -valintaruudun tilan muuttaminen ja haun suorittaminen tallentavat uuden tilan (valittu tai ei valittu) käytössä olevaan profiiliin. Haun peruuttaminen ei muuta valintaruudun tilaa käytössä olevassa profiilissa, vaikka muuttaisit sitä ennen haun peruuttamista.

### Hakujen tilannekohtaiset tiedot

NVDA käyttäytyy hakusanan löytyessä seuraavasti: kohdistus sijoitetaan hakusanan kohdalle ja rivi luetaan siitä eteenpäin.

Tämä on aina ollut ongelmallista suoritettaessa useita hakuja NVDA+F3-näppäinkomennolla, koska ensimmäinen kuulemasi asia on itse hakusana, mikä on täysin tarpeetonta, koska hait sitä juuri.

Tämä lisäosa sijoittaa kohdistimen hakusanan kohdalle, mutta sen sijaan että lukisi siitä eteenpäin, se lukee koko rivin, mikä antaa käsityksen siitä, mistä kohdasta kyseinen hakusana löytyi.

Oletetaan esimerkiksi, että etsit hakusanaa "Marlon", koska tiedät, että jossain on painike nimeltä "Kohdista Marlonille". Et halua etsiä hakusanaa "Kohdista", koska muitakin "kohdista XYZ" -nimisiä painikkeita on, ja haluat löytää vain "Kohdista Marlonille" -painikkeen.

Tässä on teksti:

Poista Marlonin kommentit

Vastaa suoraan Marlonille

Ilmoita Marlon roskapostittajaksi

Kohdista vastaus Marlonille

Jos etsisit hakusanaa "Marlon" ennen tätä lohkoa, kuulisit

Marlonin kommentit

Jos jatkaisit NVDA+F3:n painamista, kuulisit

Marlonille

Marlon roskapostittajaksi

vastaus Marlonille

Tämä vähentäisi tuottavuuttasi, koska ensin kuulisit vain "Marlon", etkä tietäisi mitään tästä esiintymästä.

Seuraavalla kerralla kuulisit "Marlon" ja sinun olisi odotettava, että "roskapostittajaksi" puhutaan, koska et tietäisi, miten tämä teksti liittyy Marloniin.

Samoin seuraavalla kerralla sinun olisi odotettava, että "vastaus" puhutaan, koska et olisi varma, mitä siinä tekstissä puhutaan Marlonista.

Lisäksi, jos painaisit nopeasti NVDA+F3, kuulisit "Marlon, Marlon, Marlon, Marlon...", mikä ei ole tuottavaa, koska tiedät etsiväsi Marlonia.

#### Miten se toimii?

Asenna lisäosa.

Kun se on asennettu, rivi, jolla senhetkinen löytynyt hakusana on, luetaan ja kohdistus siirretään hakusanan kohdalle.

Edellisessä esimerkissämme ensimmäisellä hakukerralla kuulisit

Poista Marlonin kommentit

Jos jatkaisit NVDA+F3:n painamista, kuulisit

Vastaa suoraan Marlonille

Ilmoita Marlon roskapostittajaksi

Kohdista vastaus Marlonille

Lisäksi, jos painaisit nopeasti NVDA+F3, kuulisit jokaisen rivin alun, mikä mahdollistaisi nopean Enterin painamisen kohderivillä, koska tiedät, että "Marlon" on myöhemmin samalla rivillä.

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
