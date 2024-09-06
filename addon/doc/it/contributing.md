# Contribuire

## costruzione del componente aggiuntivo

### Ambiente locale

Sebbene non sia obbligatorio, si suggerisce di eseguire quanto segue:

1. Clona NVDA in una cartella allo stesso livello di questo progetto.  
Ad esempio, se questo progetto viene clonato in c:\projects\EnhancedFindDialog, NVDA dovrebbe essere clonato in c:\projects\nvda.  
Esegui un clone con il flag --recursive. Se NVDA è già clonato, assicurati che sia aggiornato, recuperando e quindi sincronizzando il ramo master con il ramo master upstream di NVDA.  
Esegui un comando git submodule update --init per assicurarti che i sottomoduli git siano sincronizzati correttamente.
2. Esegui un checkout git nel tag release-2024.1 nel progetto NVDA. Non è necessario compilare NVDA, è sufficiente avere solo il codice sorgente nel ramo di rilascio.
3. Installa Visual Studio Code, se non è installato. Sebbene sia possibile utilizzare altri ambienti, la configurazione ottimale richiede Visual Studio Code.
4.Apri la cartella EnhancedFindDialog in VS Code. Dalla riga di comando, esegui il "codice". oppure utilizza i menu file/apri cartella sul codice stesso di Visual Studio e seleziona la cartella in cui è clonato questo progetto.
5. Utilizzare ctrl+Shift+x per accedere al widget delle estensioni di Visual Studio Code. Tab fino alla sezione consigliate ed installare le estensioni consigliate.
6. Riavviare visual studio code.
7. Ora, ogni volta che si naviga nel codice, premendo f12 in un oggetto NVDA si dovrebbe essere portati alla sua origine nel progetto NVDA.

### Dipendenze

Si avrà necessità di:

* python 3.11.
* pip deve essere configurato
* scons (pip install scons)
* markdown (pip install markdown)
* L'utilità msgfmt. Il modo più semplice per ottenerlo è installare git bash e scegliere di includere gli strumenti bash al prompt dei comandi

#### Pre-commit

Si consiglia vivamente di installare pre-commit.

* pip imstall pre-commit
* pre-commit install

Questo installerà pre-commit e configurerà i suoi hook, in modo che ogni volta che esegui un commit verranno applicati diversi controlli.  
Se qualcuno di essi dovesse fallire, il commit non sarà consentito.
Ciò aiuta a garantire che i tuoi commit abbiano qualità. Puoi ignorare il controllo, tuttavia tieni presente che anche un controllo della richiesta pull applicherà questi stessi controlli e l'unione verrà disabilitata nel caso in cui qualcuno di essi fallisse, anche se qualcuno approva la richiesta pull.

Puoi attivare i controlli pre-commit in qualsiasi momento senza eseguire un commit immettendo "pre-commit run --all-files".

#### Flake8

Uno degli hook pre-commit è flake8, un linter Python che, tra le altre cose, aiuta a garantire che il progetto abbia una formattazione coerente e che siano messe in atto buone pratiche.

Le estensioni consigliate di Visual Studio code includono flake8, in modo da poter essere avvisati durante la modifica del codice quando è necessario correggere qualcosa.

L'estensione di Visual Studio code e gli hook flake8 pre-commit utilizzano la stessa configurazione.

### costruzione

Una volta installato tutto, l'emissione di scons alla radice del progetto dovrebbe creare il componente aggiuntivo e generare la documentazione.

## traduzione

### traduzione del componente aggiuntivo

Supponendo che si abbia tutto impostato per la costruzione dell'addom (si veda argomento precedente), l'emissione di scons pot dovrebbe generare un file pot nella directory root del progetto. È possibile generare e contribuire con i file .po per la propria lingua.
Le lingue attuali possono essere trovate nella directory /addon/locale

### traduzione della documentazione

Le traduzioni della documentazione vengono generate da file .tpl.md (non da .md). Questo è il motivo per cui, tranne questo file (readme.md) nella radice del progetto, non troverai altri file .md.
I file .tpl.md sono normali file di markdown con un'aggiunta: se usi ${[var]} all'interno del suo testo, [var] verrà sostituito da una var con lo stesso nome definito in buildvars.py quando dai corrispondenti md Vengono generati file .html.
Se non esiste alcuna variabile con quel nome, la sostituzione non avviene.
Questo è utile ad esempio per generare link e titoli con la versione addon inclusa senza dover riscrivere la documentazione.

Per tradurre la documentazione, prendi il file readme.tpl.md nella radice del progetto e traducilo. Il file tradotto deve essere denominato readme.tpl.md e deve essere inserito nella directory addon/doc/[lang].

Le variabili ${[xxx]} devono rimanere intatte. Per generare i documenti, emettere scons e verranno generati il markdown e l'HTML.