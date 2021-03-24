#Importiamo i moduli
import statistics

#Creiamo i dictionary
mario = {"Matematica":6, "Italiano":6, "Scienze":7, "Inglese":4}
giovanni = {"Matematica":4, "Italiano":6, "Scienze":5, "Inglese":7}
paola = {"Matematica":9, "Italiano":6, "Scienze":8, "Inglese":8}

#Facciamo le medie e stampiamo il tutto
mediaMario = str(statistics.mean(mario.values()))
mediaGiovanni = str(statistics.mean(giovanni.values()))
mediaPaola = str(statistics.mean(paola.values()))
print("La media dei voti di Mario è " + mediaMario)
print("La media dei voti di Giovanni è " + mediaGiovanni)
print("La media dei voti di Paola è " + mediaPaola)