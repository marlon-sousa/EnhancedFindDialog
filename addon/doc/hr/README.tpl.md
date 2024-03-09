# Poboljšani dijaloški okvir traženja za NVDA${addon_version}
Poboljšani dijaloški okvir traženja dodatak za NVDA implementira poboljšano pretraživanje:

* povijest pretraživanja
* prelamanje pretraživanja, konfigurirano po profilu
* osjetljivost na velika i mala slova, konfigurirano po profilu
* kontekstualne informacije o pretraživanjima

## Preuzimanje
Preuzmite Poboljšani dijaloški okvir traženja ${addon_version} dodatak](https://github.com/marlon-sousa/EnhancedFindDialog/releases/download/${addon_version}/EnhancedFindDialog-${addon_version}.nvda-addon)

## Značajke

### Povijest pretraživanja
Na mnogim web-mjestima i web-aplikacijama, najbrži način za pristup određenim mjestima je pomoću naredbe za pretraživanje, često vezane na tipke NVDA + Control + F.

Dijaloški okvir za pretraživanje omogućuje nam upisivanje teksta i postavljanje na sljedeće pojavljivanje tog teksta ako postoji.

U mnogim slučajevima, naći ćete se kako posjećujete iste web stranice nekoliko puta tijekom iste NVDA sesije. Na mnogim od ovih web stranica morat ćete tražiti iste pojmove, posebno ako je to jedini način da brzo dođete do poveznice ili odjeljka te web stranice.

To je posebno slučaj s ljudima koji svakodnevno rade sa sustavima koji se temelje na webu kao dijelom svog posla.

Međutim, NVDA ne čuva prethodne pojmove koje ste tražili na popisu. To usporava vašu produktivnost, jer osim ako ne tražite točno isti pojam kao što ste prošli put tražili, morate ga ponovno upisati.

Ovaj dodatak čuva povijest pretraživanja koja traje sve dok je NVDA pokrenut. Dakle, prilikom aktivacije samo trebate pritisnuti strelicu prema dolje i odabrati prethodno tražene pojmove za izvođenje nove pretrage.

Naravno, možete upisati nove pojmove. Oni će također biti dodani na popis sljedeći put kada aktivirate dijaloški okvir za pretraživanje.

#### Kako radi?

Jednostavno instalirajte dodatak. Kada je aktiviran, pritiskanje strelica prema dolje i gore na polju za uređivanje u dijaloškom okviru za pretraživanje omogućit će vam navigaciju kroz popis prethodno pretraživanih pojmova.

U svakom trenutku možete upisati novi pojam kao i obično.

### Prelamanje pretraživanja

Prelamanje pretraživanja je značajka koja, ako je konfigurirana, ne uzima u obzir trenutni položaj na kojem se nalazite u tekstu prilikom pretraživanja.

To znači da ako tražite nešto čega nema ispod vaše trenutne pozicije, pretraga će se izvršiti od početka teksta kako bi se provjerilo postoji li taj pojam negdje u cijelom tekstu.

Ovo je posebno važno ljudima koji rade sa sustavima temeljenim na webu i trebaju pronaći određeni gumb ili dio teksta bez obzira na to gdje se na stranici nalaze.

Ova je opcija specifična za profil, što znači da možete imati profil tamo gdje je aktivan, a drugi gdje nije.

#### Kako radi?

Jednostavno instalirajte dodatak. Kada je aktiviran, dijaloški okvir za traženje ponudit će potvrdni okvir pod nazivom prelamanje pretraživanja.

Ako je označen:

1. Ako tražite pojam i nađete ga ispod trenutne pozicije, bit ćete postavljeni na taj tekst.
2. Ako se ovaj pojam ne nalazi ispod trenutne pozicije, tražit će se od vrha teksta.
3. Ako je pojam pronađen, oglasit će se kratki zvučni signal koji vas obavještava da je pronađeni tekst iznad vaše trenutne pozicije i da ste postavljeni na njegovu poziciju.
4. Ako ovaj pojam uopće nije pronađen, prikazuje se poruka da tekst nije pronađen.

Promjenom ovog potvrdnog okvira i izvođenjem pretraživanja spremit će se novo stanje (označeno ili neoznačeno) za aktivni profil. Otkazivanjem pretraživanja neće se promijeniti njegovo stanje na aktivnom profilu, čak i ako ste ga promijenili prije otkazivanja pretraživanja.

### osjetljivost na velika i mala slova

NVDA već nudi potvrdni okvir osjetljivosti na velika i mala slova kako bi omogućio pretraživanje s obzirom na velika i mala slova. Ovaj dodatak proširuje ovu funkcionalnost spremanjem stanja ovog potvrdnog okvira u aktivnom profilu, tako da možete imati profile s ovim konfiguriranim drugačije.

#### Kako radi?

Jednostavno instalirajte dodatak. Promjena potvrdnog okvira osjetljivosti na velika i mala slova i izvođenje pretraživanja spremit će novo stanje (označeno ili neoznačeno) za aktivni profil. Otkazivanjem pretraživanja neće se promijeniti njegovo stanje na aktivnom profilu, čak i ako ste ga promijenili prije otkazivanja pretraživanja.

### kontekstualne informacije o pretraživanjima

Način na koji se NVDA ponaša kada se pronađe traženi pojam je sljedeći: postavljeni ste na mjesto traženog pojma i red se čita od traženog pojma dalje.

Ovo je oduvijek bilo problematično kada nešto trebate pretraživati ​​nekoliko puta (koristeći NVDA + F3), jer prvo što slušate je sam traženi pojam, kada taj pojam znate jer ste ga upravo tražili.

Ovaj dodatak postavlja pokazivač na poziciju izraza, ali umjesto da čita od pojma, on čita cijeli redak, dajući vam kontekst u kojem je taj pojam pronađen.

Na primjer, pretpostavimo da tražite "Marlon" jer znate da postoji gumb koji se zove "Target Marlon somehwere". Ne želite tražiti metu jer postoje drugi gumbi koji se zovu "Cilj, x, y, z" i želite pronaći metu Gumb Marlon.

Evo teksta:

Izbriši Marlonove komentare

Odgovori izravno Marlonu

Prijavite Marlona kao spamera

Ciljajte Marlona na odgovor

Kad biste tražili Marlona prije ovog bloka, čuli biste
Komentari Marlona

Ako nastavite pritiskati NVDA + F3 čut ćete
Marlon

Marlon kao spamer

Marlon na odgovoru

To bi smanjilo vašu produktivnost jer biste prvo čuli samo marlon, a da ništa ne znate o ovoj pojavi.

Sljedeći put biste čuli Marlona i morali biste čekati da se kao spammer progovori, jer ni vi ne biste znali što je o Marlonu u ovom tekstu.

Slično tome, sljedeći put ćete morati pričekati na odgovor, jer ni vi ne biste bili sigurni što je to s Marlonom.

Štoviše, ako biste brzo pritisnuli NVDA + F3, čuli biste Marlon, Marlon, Marlon, Marlon ... što nije produktivno jer znate da tražite Marlona.

#### Kako radi?

Jednostavno instalirajte dodatak.

Nakon što se instalira, očitava se trenutni redak pronađenog traženog pojma i nalazite se na pojmu koji se nalazi u njemu.

U našem gornjem primjeru, kada ste prvi put izvršili pretraživanje čuli biste

Izbriši Marlonove komentare

Ako nastavite pritiskati NVDA + F3 čut ćete

Odgovori izravno Marlonu

Prijavite Marlona kao spamera

Ciljajte Marlona na odgovor

Nadalje, ako ste brzo pritisnuli NVDA + F3, čut ćete početak svakog retka, što vam omogućuje da brzo pritisnete Enter na ciljnom retku jer znate da je Marlon prisutan na kasnijoj poziciji u tom istom retku.

## Doprinos i prevođenje

Ako želite doprinijeti ili prevesti ovaj dodatak, pristupite [repozitoriju projekta](https://github.com/marlon-sousa/EnhancedFindDialog) i pronađite upute na contributing.md u direktoriju dokumentacije na engleskom jeziku.

## Suradnici

Posebna zahvala za

* Ângelo Miguel Abrantes - portugalski prijevod
* Rémy Ruiz - španjolski prijevod
* Rémy Ruiz - francuski prijevod
* Tarik Hadžirović - hrvatski prijevod
* Thiago Seus - brazilski portugalski prijevod, kompatibilnost s NVDA 2024.1
* Umut KORKMAZ - turski prijevod
* Valentin Kupriyanov - ruski prijevod
* Ivan Shtefuriak - ukrajinski prijevod
