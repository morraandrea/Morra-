import subprocess
import sys
import string
import numpy as np
import matplotlib.pyplot as plt
from guizero import *

#Importiamo una funzione che crea il grafico partendo dalle informazioni
#contenute nel file che leggeva le coordinate
def leggiFile():
    subprocess.check_call([sys.executable, 'morraandrea.py'])

#Definiamo una funzione che esegue lo script che scrive il file
#con i dati relativi alle coordinate
def scriviFile():
    subprocess.check_call([sys.executable, 'morraandrea-2.py'])


app = App(title="Crea grafico", bg="#f5f5f5", width=500, height=600)

bottoneUno = PushButton(app, text="Genera numeri", command = scriviFile, width=20,)
bottoneDue = PushButton(app, text="Crea Grafico", command = leggiFile, width=20,)

app.display()
