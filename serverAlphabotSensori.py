import socket
import time
from AlphaBot import AlphaBot
import RPi.GPIO as GPIO



PORTA = 5000
HOST = "0.0.0.0" #a tutti gli host disponibili
BUFFER = 4096
numeroClient = 1
roborto = AlphaBot()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORTA))
s.listen(numeroClient)
print(f"Il server di roborto è pronto sull'host: {HOST} e porta:{PORTA}...")
print("i comandi per muoversi: w=avanti, s=indietro, a=sinistra, d=destra, x=stop, exit=uscita")

connessione, indirizzo = s.accept()
print(f"il client è connesso sull'indirizzo = {indirizzo}")

esecuzione = True

while esecuzione:

    sensoreSinistro = GPIO.input(roborto.DL)#controlliamo tutti i sensori
    sensoreDestro = GPIO.input(roborto.DR)#controlliamo tutti i sensori
    

    if sensoreSinistro  == 0:
        print("sensore attivato")

        roborto.backward() #comando per farlo andare indietro
        time.sleep(0.5) #attesa di mezzo secondo
        roborto.right() #comando per farlo svoltare a destra
        time.sleep(0.5) #attesa di mezzo secondo
        roborto.stop() #stop del robot
        continue

    elif sensoreDestro == 0:
        print("sensore attivato")

        roborto.backward() #comando per farlo andare indietro
        time.sleep(0.5) #attesa di mezzo secondo
        roborto.left() #comando per farlo svoltare a destra
        time.sleep(0.5) #attesa di mezzo secondo
        roborto.stop() #stop del robot
        continue  
    

    
    connessione.settimeout(0.1)#aspettiamo per la connessione
    comando = connessione.recv(BUFFER)#riceviamo il comando, tra quelli di prima

    if comando:
        direzione = comando.decode('utf-8').strip().lower()
        #serie di controllo su tutti i comandi possibili
        if direzione == 'w':
            print("avanti")
            roborto.forward()
        elif direzione == 's':
            print("indietro")
            roborto.backward()
        elif direzione == 'a':
            print("sinistra")
            roborto.left()
        elif direzione == 'd':
            print("destra")
            roborto.right()
        elif direzione == 'x':
            print("stop")
            roborto.stop()
        elif direzione == 'exit':
            print("uscita forzata.")
            roborto.stop()
            esecuzione = False
        else:
            print(f"Non ho capito: {direzione}")

    time.sleep(0.05)

#fase finale, chiudere la connessione, pulire gli GPOI, stop del robot e chiusura del socket
GPIO.cleanup()
connessione.close()
roborto.stop()
s.close()
print("Tutto chiuso e buffer svuotato")