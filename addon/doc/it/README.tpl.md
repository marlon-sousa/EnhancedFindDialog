# EnhancedFindDialog for NVDA ${addon_version}
Enhanced find dialog addon for NVDA, implementazione di miglioramenti nella ricerca:

* Cronologia delle ricerche
* ricerca dallinizio, configurata per profili
* distinzione tra maiuscole e minuscole, configurata per profili
* informazioni contestuali sulle ricerche

## Download
Scarica [Enhanced Find Dialog ${addon_version} addon](https://github.com/marlon-sousa/EnhancedFindDialog/releases/download/${addon_version}/EnhancedFindDialog-${addon_version}.nvda-addon)

## Funzionalità

### Cronologia delle ricerche
In molti siti ed applicazioni web, il modo più rapido per trovare un determinato elemento è tramite il comando di ricerca, associato di default alla combinazione NVDA+CTRL+f.

La finestra di dialogo di ricerca consente di digitare un testo e di essere posizionati alla sua successiva occorrenza, se esiste.

In molti casi ci si ritroverà a visitare più volte gli stessi siti web durante una sessione di NVDA, ed in molti di questi si dovrà cercare gli stessi termini, soprattutto se questo è l'unico modo per raggiungere rapidamente un collegamento o una sezione di quel sito.

Questo è soprattutto il caso delle persone che lavorano quotidianamente con sistemi basati sul web come parte del loro lavoro.

Tuttavia NVDA non conserva nell'elenco i termini precedentemente cercati. Ciò rallenta la produttività perché a meno che non si stia cercando esattamente lo stesso termine dell'ultima ricerca, sarà necessario digitare nuovamente ciò che si è cercato precedentemente.

Questo componente aggiuntivo conserva una cronologia delle ricerche che dura finché NVDA è in esecuzione. Quindi, all'apertura della finestra di ricerca, basterà premere la freccia verso il basso e scegliere i termini precedentemente cercati per effettuare una nuova ricerca.

Ovviamente è possibile anche cercare nuovi termini che saranno aggiunti alla cronologia, effettuando normalmente la ricerca.

#### Come funziona?

Installa semplicemente il componente aggiuntivo. Quando è attivato, premendo le frecce verticali nel campo di testo della finestra di ricerca potrai navigare nell'elenco dei termini cercati in precedenza.
Puoi in qualsiasi momento digitare un nuovo termine come al solito.

### Ricerca dall'inizio

La ricerca dall'inizio è una funzionalità che, se configurata, non considera la posizione corrente in cui ci si trova in un testo durante l'esecuzione delle ricerche.

Ciò significa che se si cerca qualcosa che non è presente al di sotto della posizione attuale, la ricerca verrà effettuata dall'inizio del testo per verificare se il termine cercato esiste da qualche parte nell'intero testo.

Ciò è particolarmente importante per le persone che lavorano con sistemi basati sul Web ed hanno bisogno di trovare un determinato pulsante o stringa di testo indipendentemente da dove si trovano nella pagina.

Questa opzione è specifica del profilo, il che significa che è possibile avere un profilo in cui è attiva ed un altro nel quale non lo è.

#### Come funziona?

Installa semplicemente il componente aggiuntivo. Quando esso è attivato, la finestra di ricerca conterrà una casella di controllo chiamata ricerca dall'inizio.

Se è selezionata:

1. Se si cerca un termine e questo si trova al di sotto della posizione corrente, si verrà posizionati sul risultato della ricerca.
2. Se quanto cercato non si trova al di sotto della posizione corrente, la ricerca verrà effettuata dall'inizio del testo.
3. Se quanto cercato viene trovato, viene riprodotto un breve segnale acustico per informare che esso si trova al di sopra della posizione attuale, si verrà anche posizionati sul risultato.
4. Se quanto cercato non viene trovato, viene visualizzato il messaggio Testo non trovato.

La modifica di questa casella di controllo e l'esecuzione di una ricerca salveranno il nuovo stato (selezionato o deselezionato) per il profilo attivo. L'annullamento di una ricerca non ne modificherà lo stato sul profilo attivo, anche se è stato modificato prima di annullare la ricerca.
### distinzione tra maiuscole e minuscole

NVDA prevede già la casella di controllo per la distinzione tra maiuscole e minuscole per consentire la ricerca considerando questa distinzione. Questo componente aggiuntivo estende la funzionalità salvando lo stato di questa casella di controllo nel profilo attivo, in modo da poter avere profili con configurati in modo diverso.

#### Come funziona?

Installa semplicemente il componente aggiuntivo. La modifica della casella di controllo per la distinzione tra maiuscole e minuscole e l'esecuzione di una ricerca salveranno il nuovo stato (selezionato o deselezionato) per il profilo attivo. L'annullamento di una ricerca non ne modificherà lo stato sul profilo attivo, anche se è stato modificato prima di annullare la ricerca.

### informazioni contestuali sulle ricerche

Il comportamento di NVDA quando viene trovato un termine cercato è il seguente: si viene posizionati in corrispondenza del termine cercato e viene letta la riga dal esso in poi.

Questo risulta problematico quando è necessario cercare un termine più volte (usando NVDA + f3), perché la prima cosa che si ascolta è la ricerca stessa, conosciuta in quanto appena cercata.

Questo componente aggiuntivo posiziona il cursore nella posizione del risultato, ma invece di leggere da esso legge l'intera riga, fornendo il contesto che contiene quanto cercato.

Ad esempio, supponiamo che si stia cercando "Marlon" perché si sa che da qualche parte esiste un pulsante chiamato indirizza a Marlon. Non si vuole cercare indirizza a, perché ci sono altri pulsanti chiamati "indirizza a x y z" e si vuole trovare proprio il pulsante indirizza a  Marlon.

Questo è il testo:

Elimina i commenti di Marlon

Rispondi direttamente a Marlon

Segnala Marlon come spammer

Indirizza a Marlon

Se si cercasse Marlon prima di questo blocco di testo, si ascolterebbe:
Marlon

Se si continuasse a premere NVDA+f3 si ascolterebbe:

Marlon

Marlon come spammer

Marlon

Ciò ridurrebbe la produttività perché si ascolterebbe solo Marlon, senza sapere altro.

La prossima volta si ascolterebbe Marlon e si dovrebbe aspettare che venga pronunciato il testo come spam, perché non si sa nemmeno cosa si riferisce a Marlon..

Similmente nella prossima ricerca..

Inoltre, se si preme rapidamente NVDA+f3 si ascolterebbe solo Marlon, Marlon, Marlon. Il che non è produttivo, in quanto si sa di aver cercato Marlon

#### come funziona

Installa semplicemente il componente aggiuntivo.

Dopo l'installazione, viene letta l'intera riga del risultato e si viene posizionati al suo termine.
Nel nostro esempio sopra, alla prima esecuzione della ricerca si ascolterebbe

Elimina i commenti di Marlon
Se si continuasse a premere NVDA+f3 si ascolterebbe

rispondi direttamente a Marlon

Segnala Marlon come spammer
Indirizza a Marlon

Inoltre, se si premesse rapidamente NVDA+f3 si ascolterebbe direttamente l'inzio della riga, velocizzando la ricerca in quanto la parola Marlon si trova alla fine di essa.

## Contribuire e tradurre

Se si volesse contribuire o tradurre questo componente aggiuntivo, prego accedere al [repository del progetto](https://github.com/marlon-sousa/EnhancedFindDialog)e seguire le istruzioni nel file contributing.md nella directory della documentazione in lingua inglese.

## Contributori

Un ringraziamento speciale a


* Ângelo Miguel Abrantes - traduzione in Portoghese
* Rémy Ruiz - traduzione in Francese
* Rémy Ruiz - traduzione in Spagnolo
* Tarik Hadžirović - traduzione in Croato
*  Thiago Seus - traduzione in Portoghese Brasiliano, compatibilità con NVDA 2024.1
* Umut KORKMAZ - traduzione in Turco
* Valentin Kupriyanov - traduzione in Russo 
* Ivan Shtefuriak - traduzione in Ukraino
* Leonardo Marenda - traduzione in Italiano
