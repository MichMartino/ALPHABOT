import socket
import time
import RPi.GPIO as GPIO
from AlphaBot import AlphaBot

#Inizializza il robot
bot = AlphaBot()

#Configura il server TCP
HOST = ''          #accetta connessioni da qualsiasi IP (0.0.0.0)
PORT = 5000
BUFFER = 4096
nClient = 1

#Crea il socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(nClient)

print(f"AlphaBot Server avviato su porta {PORT}")
print("In attesa di connessione da un client...")

conn, addr = server_socket.accept()
print(f"Connessione stabilita con: {addr}")

while True:
    #Ricezione dati dal client
    data = conn.recv(BUFFER).decode().strip()
    if not data:
        print("Connessione interrotta dal client.")
        break

    print(f"Comando ricevuto: {data}")

    #Controllo comandi
    if data == 'w':        #avanti
        bot.forward()
    elif data == 's':      #indietro
        bot.backward()
    elif data == 'a':      #sinistra
        bot.left()
    elif data == 'd':      #destra
        bot.right()
    elif data == 'x':      #stop
        bot.stop()
    elif data.startswith('speed '):
        value = int(data.split()[1])
        bot.setPWMA(value)
        bot.setPWMB(value)
        print(f"Velocità impostata a {value}%")
    elif data == 'exit':
        break
    else:
        print("Comando non riconosciuto.")

    time.sleep(0.1)

#Siamo fuori dal ciclo while, stacco il programma
bot.stop()
GPIO.cleanup()
server_socket.close()
