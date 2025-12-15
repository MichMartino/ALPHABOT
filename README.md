Relazione progetto alphabot con db
Nome: Martino Michele, Masoero Andrea
Classe: 5 A ROBOTICA
Obiettivi da raggiungere:
Effettuare la connessione in SSH sull’Alpha BOT, attraverso un reboot di una micro SD con S.O. Raspberry, per poterlo connettere al nostro router.
Mandare con WinSCP i codici da fare eseguire all’Alpha BOT, collegandosi alla stessa rete del Alpha BOT.
I programmi dovranno essere in protocollo di comunicazione TCP, attivando il server sull’Alpha BOT e il client sul nostro pc, i programmi dovranno essere in grado di:
Far muovere il robot con i comandi di base WASD per muoversi nello spazio;
Collegarsi ad un DATABASE per poter eseguire delle query ed ottenere differenti risultati (Come il movimento del robot per la costruzione di forme geometriche sul suolo)



Prerequisiti

Sapere flashare con Balena Etcher una micro SD in modo da poterci inserire sopra la ISO necessaria.
Configurare la micro SD utilizzando la tastiera di Raspberry e il suo setup su riga di comando
Saper programmare un Client/Server TCP e sapere gestire la comunicazione tra Client / Server
Competenze base sulla gestione di un DB 


Conoscenze 

Gestire l’input dei sensori e la corretta regolazione dei sensori
Affinato le conoscenze di collegamento con putty, e gestione degli indirizzi IP.
Come funziona un alphaBot nel dettaglio ed il suo sistema operativo


Abilità 
Programmazione in Python
Uso di librerie specifiche (=sqlite3, AlphaBOT, etc)
Integrazione tra software e hardware
Gestione dei sensori
Lettura dei dati da sensori
Interpretazione dei valori rilevati
Controllo dei motori dell’AlphaBot
Regolare la velocità
Sincronizzare i sensori con i motori
Configurazione di una Raspberry Pi
Formattazione e scrittura dell’ISO
Configurazione iniziale (SSH)
Avvio script e servizi python
Gestione del database con sqlite3 e gestione file
Passaggio dati con WinSCP
Organizzazione dei file e dei permessi
Lavoro in rete
Connessione tra pc e AlphaBot
Avvio del test
Competenze 

Essere in grado di sviluppare un progetto, in un determinato tempo, in un team
Acquisire autonomia nella realizzazione di semplici collegamenti
Gestione di una macchina da remoto




Abstract
Il progetto ha avuto come obiettivo lo sviluppo di un sistema di controllo remoto per un robot AlphaBot, utilizzando una Raspberry Pi come unità centrale. La metodologia ha previsto la configurazione della connettività di rete tramite SSH e l'implementazione di un'architettura client-server basata sul protocollo TCP. I client (PC) comunicano comandi di movimento (WASD) al server (AlphaBot), che esegue le azioni fisiche. Parallelamente, è stata integrata la capacità di interfacciarsi con un database locale SQLite3 per l'esecuzione di query ed elaborazione dati (sui vari comandi e derivati da essi). Il risultato è un sistema robotico che mette in comunicazione una rete di informazioni e il loro successivo utilizzo su hardware (L’alphabot)
Dettaglio delle fasi operative
Effettuare la connessione in SSH sull’Alpha BOT, attraverso un reboot di una micro SD con S.O. Raspberry, per poterlo connettere al nostro router.
Mandare con WinSCP i codici da fare eseguire all’Alpha BOT, collegandosi alla stessa rete del Alpha BOT.
I programmi dovranno essere in protocollo di comunicazione TCP, 
(Server)



attivando il server sull’Alpha BOT e il client sul nostro pc, 
(Client)


i programmi dovranno essere in grado di:
Far muovere il robot con i comandi di base WASD per muoversi nello spazio;


Collegarsi ad un DATABASE per poter eseguire delle query ed ottenere i risultati prestabiliti (In questo caso, fare muovere il robot secondo comandi salvati nei campi del db) 


Risultati raggiunti e autovalutazione
In conclusione sono stati conseguiti gli obiettivi prefissati per la relazione: abbiamo stabilito una connessione versatile con il robot, programmato varie versioni di server-client per funzionamenti diversi e successivamente elaborato il funzionamento dell'alphabot tramite comandi salvati su un database collegato al server. 
Per tale motivo, l'autovalutazione scelta dal team per queste esercitazioni è ottimale, in quanto si è lavorato con efficienza anche durante i momenti più ardui.
Criticità riscontrate e modalità di gestione delle criticità
Abbiamo avuto numerose difficoltà durante la fase di connessione all’Alpha BOT, in particolare il PUTTY, il problema era il mancato collegamento alla rete da parte del robot, e di conseguenza abbiamo iniziato a cercare i vari problemi, come cambiare le batterie e schede SD, dopo numerosi tentativi abbiamo trovato il vero problema, ovvero la nostra micro SD di partenza si era corrotta, capito ciò abbiamo provveduto a fare tutti i passaggi dall’inizio con una nuova micro SD, grazie alla quale siamo riusciti finalmente a collegarci.
Prospettive di sviluppo future
L’utilizzo di Flask (Per fare un’app web che gestisca il movimento del robot), l’elaborazione di codice più complesso per far eseguire all'alpha bot istruzioni più difficili, seguendo sempre i principi studiati e preparati per queste esercitazioni. 

