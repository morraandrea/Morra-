from random import randint
import string
import numpy as np
import matplotlib.pyplot as plt
from guizero import *

# Creiamo una funzione che crea il grafico
def leggiFile():
    f = open(textbox.value, 'r')
    
    coordX = []
    coordY = []
    
    for riga in f:
        valori = str(riga)  # converto in stringa la riga
        valori = valori.strip('\n') # elimino il terminatore di riga
        valori = valori.split(',')  # separo la stringa in due numeri
        valori = list(valori)       # converto in lista
        print(valori)
        coordX.append(int(valori[0])) # aggiungo la coordinata X
        coordY.append(int(valori[1])) # aggiungo la coordinata Y
    
    f.close()  # chiudiamo il file
    
    print ("X: ",coordX)
    print ("Y: ",coordY)
    
    # ordiniamo le liste
    #coordX.sort()
    #coordY.sort()
    
    #print("liste ordinate:") 
    #print ("X: ",coordX)
    #print ("Y: ",coordY)
    
    # stampo il tipo di dati delle coordinate
    print(type(coordX))
    print(type(coordY))
    
    # ora sono pronte per essere usate anche nei grafici
    
    plt.scatter(coordX,coordY)
    plt.ylabel('some numbers')
    plt.show()
    plt.clf()

#Definiamo una funzione che scrive il file
#con i dati relativi alle coordinate
def scriviFile():
    f = open(textbox.value, 'w')
    dati = ""

    for riga in range(100):
        dati = dati + str(randint(1,100)) + "," + str(randint(1,100))
        dati = dati + "\n"

    print(dati)


    f.write(dati)
    f.close()

# Inseriamo i widgtes
app = App(title="Crea grafico", bg="#f5f5f5", width=500, height=600)

titolo = Text(app, text="Inserire il nome del file")
textbox = TextBox(app, width=80, height=10, text="dati.txt")
bottoneUno = PushButton(app, text="Genera numeri", command = scriviFile, width=20,)
bottoneDue = PushButton(app, text="Crea Grafico", command = leggiFile, width=20,)

app.display()
