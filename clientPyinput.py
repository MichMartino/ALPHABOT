#Per farlo bisogna fare due funzioni una premi e una rilascia, e poi una invia e giustamente invia il tasto che stai premendo
#invece che mettere il tasto e poi inviare noi premiamo e lui deve prendere i dati in input
#Infine serve l'ascoltatore con with keyboard_Listener che on_press = premi on_release = rilascia (Che sono le mie due funzioni)

import socket
from pynput import keyboard

HOST = '192.168.1.116'  #inserisci l'indirizzo IP del Raspberry Pi
PORT = 5000

#Connessione al server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("Connesso al server AlphaBot.")
print("Controlli:")
print("  W = Avanti")
print("  S = Indietro")
print("  A = Sinistra")
print("  D = Destra")
print("  Q = Stop")
print("  ESC = Esci")
print("\nPremi i tasti per controllare l'AlphaBot...\n")

#Invia quello che ho premuto
def invia(comando):
    client.send(comando.encode())
    print(f"Comando: {comando}")

def premi(key):
    
    #Gestione tasti carattere (w, a, s, d, q)
    if hasattr(key, 'char') and key.char:
        tasto = key.char.lower()
        print(f"Tasto premuto: {tasto}")
        
        if tasto == 'w':
            invia('w')
        elif tasto == 's':
            invia('s')
        elif tasto == 'a':
            invia('a')
        elif tasto == 'd':
            invia('d')
        elif tasto == 'q':
            invia('q')
        else:
            print(f"Tasto non mappato")
    
    #Gestione tasti speciali (come ESC)
    if key == keyboard.Key.esc:
        print("\nUscita...")
        invia('x')
        return False  #Stop listener

def rilascia(key):
    if hasattr(key, 'char') and key.char:
        tasto = key.char.lower()
        print(f"Tasto rilasciato: {tasto}")
        
        #Quando rilasci un tasto di movimento, invia stop
        if tasto in ['w', 's', 'a', 'd']:
            invia('q')  #Stop automatico al rilascio

#Ascoltatore tastiera con le due funzioni
print("Ascoltatore tastiera attivo...\n")
with keyboard.Listener(on_press=premi, on_release=rilascia) as listener:
    listener.join()

#Chiusura connessione
print("\nChiudo la connessione...")
client.close()
print("Connessione chiusa.")