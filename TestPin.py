#importo la libreria per i pin di rasberry
from RPi import GPIO
#importo la libreria time per effettuare dei delay
import time
#importo la libreria per leggere i file di config
from ConfigParser import SafeConfigParser

#Modalità di riferimento dei PIN e scelta del programma nel file Config.ini
parser = SafeConfigParser()
parser.read('Config.ini')

programma = parser.get('config', 'programma')
mode = parser.get('config', 'mode')

if programma == "IMPULSI":
    if mode == "CPU":
        #setto la modalità di riferimento dei pin secondo la CPU
        GPIO.setmode(GPIO.BCM) 
        #mi riferisco ad uno specifico pin del rasberry come output (in questo caso il 21 secondo la CPU)
        GPIO.setup(21, GPIO.OUT) 

        #Settaggio dei PIN:
        #Fai all'infinito
        while True:
            #uscita a livello logico alto
            GPIO.output(21, GPIO.HIGH)
            print("Logico: 1")
            #deley di 1 secondo
            time.sleep(1)
            #uscita a livello logico basso
            GPIO.output(21, GPIO.LOW)
            print("Logico: 0")
            #deley di 1 secondo
            time.sleep(1)

    elif mode == "PIN":
        #setto la modalità di riferimento dei pin secondo la scheda
        GPIO.setmode(GPIO.BOARD) 
        #mi riferisco ad uno specifico pin del rasberry come output (in questo caso il 40 secondo la scheda)
        GPIO.setup(40, GPIO.OUT)

        #Settaggio dei PIN:
        #Fai all'infinito
        while True:
            #uscita a livello logico alto
            GPIO.output(40, GPIO.HIGH)
            print("Logico: 1")
            #deley di 1 secondo
            time.sleep(1)
            #uscita a livello logico basso
            GPIO.output(40, GPIO.LOW)
            print("Logico: 0")
            #deley di 1 secondo
            time.sleep(1)

elif programma == "CONTROLLO":
    if mode == "CPU":
        #setto la modalità di riferimento dei pin secondo la CPU
        GPIO.setmode(GPIO.BCM) 
        #mi riferisco ad uno specifico pin del rasberry come input (in questo caso il 21 secondo la CPU)
        GPIO.setup(21, GPIO.IN) 

        #Settaggio dei PIN:
        cont = 0;
        #Fai all'infinito
        while True:
            #se il pulsante viene premuto
            if GPIO.input(21) == True:
                cont++
                print("Pulsante premuto x"+cont)
                time.sleep(0.5)
                
    elif mode == "PIN":
        #setto la modalità di riferimento dei pin secondo la scheda
        GPIO.setmode(GPIO.BOARD) 
        #mi riferisco ad uno specifico pin del rasberry come input (in questo caso il 40 secondo la scheda)
        GPIO.setup(40, GPIO.IN)

        #Settaggio dei PIN:
        cont = 0;
        #Fai all'infinito
        while True:
            #se il pulsante viene premuto
            if GPIO.input(40) == True:
                cont++
                print("Pulsante premuto x"+cont)
                time.sleep(0.5)

#il PIN 40 secondo la scheda e il pin 21 secondo la cpu, si riferiscono allo stesso pin seguendo
#due tipologie di riferimento diversi