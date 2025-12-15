import socket

HOST = '192.168.1.116'  #inserisci l'indirizzo IP del Raspberry Pi
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("Connesso al server AlphaBot.")
#Exit si gestisce anche con esc o cntrl + c, dipende dalla situazione
print("Comandi: w=avanti, s=indietro, a=sinistra, d=destra, x=stop, speed N, exit=chiudi")

while True:
    comando = input("-> ").strip().lower()
    client.send(comando.encode())
    if comando == 'exit':
        break
    
client.close()
print("Connessione chiusa.")
