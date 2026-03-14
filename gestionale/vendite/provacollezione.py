import copy
from collections import Counter

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine

p1=  ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)
p3 = ProdottoRecord("Auricolari", 250.0)

#LISTE
carrello = [p1, p2, p3, ProdottoRecord("tablet", 750.0)]

print("Prodotti nel carrello:")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

#Aggiungere ad una lista
carrello.append(ProdottoRecord("Monitor", 150.0))

carrello.sort(key = lambda x: x.prezzo_unitario, reverse=True)
#dice a Python come ordinare.
# Per ogni elemento x della lista, usa x.prezzo_unitario come criterio di ordinamento.

print("Prodotti nel carrello")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name}-  {p.prezzo_unitario}")

tot = sum(p.prezzo_unitario for p in carrello)
print(f"Totale del carrello: {tot}")


#aggiungere
carrello.append(ProdottoRecord("Propdo", 100.0))
carrello.extend([ProdottoRecord("aaa", 100.0), ProdottoRecord("bbb", 100.0)])
carrello.insert(2, ProdottoRecord("ccc", 250.0))

#rimuovere
# carrello.pop() #rimuove ultimo elemento
# carrello.pop(2) #rimuove elemento in posizione 2
# carrello.remove(p1) #elimino la prima occorrenza di p1
# carrello.clear() #elimina tutto

#sorting
#carrello.sort() #ordina per ordinamento naturale -- questo non funziona se gli oggetti contenuti non definisco un metodo __lt__
#carrello.sort(reverse=True) #ordina al contrario
#carrello.sort( key=funciotn )
#carrello_ordinato= sorted(carrello) #restituisce una nuova lista ordinata, la lista originale non viene modificata

#copie e altro
carrello.reverse() #mi rida la lista al contrario
carrello_copia= carrello.copy() #shallow copy. fa una copia di carrello e GLI OGGETTI
                                # contenuti nelle due liste sono gli stessi
carrello_copia2= copy.deepcopy(carrello) #crea una lista con oggetti nuovi

#TUPLE--> IMMUTABILE
sede_principale=(45, 8) #coordinate della sede 1: lat e long
sede_Milano=(45,9 )

print(f"Sede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")

AliquoteIva=(
        ("Standard", 0.22),
        ("Ridotta", 0.10),
        ("Alimentari", 0.04),
        ("Esente", 0.0)
    )

for descr, valore in AliquoteIva:
    print(f"{descr}: {valore*100}%")

def calcola_statistiche_carrello(carrello):
    """Restituisce prezzo totale, prezzo medio, massimo e minimo"""
    prezzi = [p.prezzo_unitario for p in carrello]
    return (sum(prezzi), sum(prezzi) / len(prezzi), max(prezzi), min(prezzi))


tot, media, max, min = calcola_statistiche_carrello(carrello)

# tot, *altri_campi = calcola_statistiche_carrello(carrello)
print(tot)

#SET
categorie={"Gold", "Silver", "Bronze", "Gold"}
print(categorie)
print(len(categorie))
categorie2={"Platinum", "Elite"}
#categorie_all= categorie.union(categorie2)
categorie_all = categorie | categorie2 # unione
print(categorie_all)

categorie_comuni= categorie & categorie2 #solo elementi comuni
print(categorie_comuni)

categorie_esclusive=categorie - categorie2 #solo elementi presenti in uno dei due
print(categorie_esclusive)

categorie_esclusive_sym=categorie ^ categorie2 #differenza simmetrica
print(categorie_esclusive_sym)

prodottiOrdine_A= {ProdottoRecord("Laptop", 1200.0),
                   ProdottoRecord("Mouse", 250.0),
                   ProdottoRecord("Auricolari", 250.0)}

prodottiOrdine_B= {ProdottoRecord("Laptop2", 1200.0),
                   ProdottoRecord("Mouse2", 250.0),
                   ProdottoRecord("Tablet", 250.0)}

#Metodi utili per i set
s = set()
s1 = set()

#aggiungere
s.add(ProdottoRecord("aaa", 20.0)) #aggiunge un elemento
s.update([ProdottoRecord("aaa", 20.0), ProdottoRecord("bbb", 20.0)]) #aggiungo più elementi


#togliere
#s.remove(elem) #rimuove un elemento. Raise KeyError se non esiste.
#s.discard(elem) #rimuove un elemento, senza "arrabbiarsi" se questo non esiste.
s.pop() #rimuove e restituisce un elemento.
s.clear()

#operazioni insiemistiche
s.union(s1) # s | s1, ovvero genera un set che unisce i due set di partenza
s.intersection(s1) # s & s1, ovvero solo elementi comuni
s.difference(s1) # s-s1, ovvero elementi di s che non sono contenuti in s1
s.symmetric_difference(s1) #s ^s1, ovvero elementi di s non contenuti in s1 ed elementi di s1 non contenuti in s

s1.issubset(s) #se gli elementi di s1 sono contenuti in s
s1.issuperset(s) # se gli elementi di s sono contenuti in s1
s1.isdisjoint(s) # se gli elementi di s e quelli di s1 sono diversi

#DICTIONARY
catalogo={
    "LAP001": ProdottoRecord("Laptop", 1200.0),
    "LAP002": ProdottoRecord("Laptop2", 250.0),
    "LAP003": ProdottoRecord("mouse", 250.0),
    "LAP004": ProdottoRecord("Auricolari", 250.0)
}
cod = "LAP002"
prod = catalogo[cod]

print(f"Il prodotto con codice {cod} è {prod}")

#print(f"Cerco un altro oggetto: {catalogo["non esiste"]}")

prod1= catalogo.get("NonEsiste")

if prod1 is None:
    print("Prodotto non trovato")

prod2=catalogo.get("NonEsiste2", ProdottoRecord("Sconosciuto", 0))

print(prod2)

#ciclare su un dizionario
keys= list(catalogo.keys())
values= list(catalogo.values())

for k in keys:
    print(k)

for v in values:
    print(v)

for key, val in catalogo.items():
    print(f"Cod {key} è associata a {val}")

#rimuovere dal dizionario
rimosso= catalogo.pop("LAP002")
print(rimosso)

#DICT COMPREHENSION: un modo compatto per creare un dizionario in una riga sola.
prezzi ={codice: prod.prezzo_unitario for codice, prod in catalogo.items()}
# dizionario= {chiave: valore for chiave, valore in dizionario.items()}

#esempio versione lunga
# prezzi = {}
# for codice, prod in catalogo.items():
#     prezzi[codice] = prod.prezzo_unitario

#DA RICORDARE PER DICT
# d[key] = v # scrivo sul dizionario
# v = d[key] # leggere -- restituisce key error se non esiste
# v = d.get(key, default) # legge senza rischiare keyerror. Se non esiste rende il default
# d.pop(key) # restiuisce un valore e lo cancella dal diz
# d.clear() # elimina tutto.
# d.keys() # mi restituisce tutte le chiavi definite nel diz
# d.values() # mi resituisce tutti i valori salvati nel diz
# d.items() # restituisce le coppie chiave-valore.
# key in d # condizione che verifica se key è presente nel diz

"""ESERCIZIO
per ciascuno dei seguenti casi, decidere quale struttura usare:"""

"""1) Memorizzare una elenco di ordini che dovranno poi essere processati in ordine di arrivo"""
# Collection? Lista

ordini_da_processare = []
o1 = Ordine([], ClienteRecord("Mario Rossi", "mario@polito.it", "Gold"))
o2 = Ordine([], ClienteRecord("Mario Bianchi", "bianchi@polito.it", "Silver"))
o3 = Ordine([], ClienteRecord("Fulvio Rossi", "fulvio@polito.it", "Bronze"))
o4 = Ordine([], ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"))

ordini_da_processare.append((o1, 0))
ordini_da_processare.append((o2, 10))
ordini_da_processare.append((o3, 3))
ordini_da_processare.append((o4, 45))

"""2) Memorizzare i CF dei clienti (univoco)"""
# Collection? SET
codici_fiscali = {"ajnfkefioe231", "ajnsow241", "njknaskm1094", "ajnsow241"}
print(codici_fiscali)

"""3) Creare un database di prodotti che posso cercare con un codice univoco"""
# Collection? DIZIONARIO
listino_prodotti = {"LAP0001" : ProdottoRecord("Laptop", 1200.0),
                    "KEY001" : ProdottoRecord("Keyboard", 20.0)}

"""4) Memorizzare le coordinate gps della nuova sede di Roma"""
# Collection? TUPLA
magazzino_roma = (45, 6)

"""5) Tenere traccia delle categorie di clienti che hanno fatto un ordine in un certo range temporale"""
# Collection? SET
categorie_periodo = set()
categorie_periodo.add("Gold")
categorie_periodo.add("Bronze")

print("=============================================================")


#COUNTER
lista_clienti = [
    ClienteRecord("Mario Rossi", "mario@polito.it", "Gold"),
    ClienteRecord("Mario Bianchi", "bianchi@polito.it", "Silver"),
    ClienteRecord("Fulvio Rossi", "fulvio@polito.it", "Bronze"),
    ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"),
    ClienteRecord("Mario Bianchi", "mario@polito.it", "Gold"),
    ClienteRecord("Giuseppe Averta", "bianchi@polito.it", "Silver"),
    ClienteRecord("Francesca Pistilli", "fulvio@polito.it", "Bronze"),
    ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"),
    ClienteRecord("Fulvio Corno", "carlo@polito.it", "Silver")
]

categorie = [c.categoria for c in lista_clienti]
categorie_counter = Counter(categorie)

print("Distribuzione categorie clienti")
print(categorie_counter)
# Counter({'Gold': 4, 'Silver': 3, 'Bronze': 2})

print("2 Categorie più frequent1")
print(categorie_counter.most_common(2))
# [('Gold', 4), ('Silver', 3)]

print("totale:")
print(categorie_counter.total())

vendite_gennaio = Counter(
    {"Laptop": 13, "Tablet": 15}
)

vendite_febbraio = Counter(
    {"Laptop": 3, "Stampante": 1}
)

vendite_bimestre = vendite_gennaio+vendite_febbraio

#Aggregare informazione
print(f"Vendite Gennaio: {vendite_gennaio}")
print(f"Vendite Febbraio: {vendite_febbraio}")
print(f"Vendite bimestre: {vendite_bimestre}")
#  Vendite bimestre: Counter({'Laptop': 16, 'Tablet': 15, 'Stampante': 1})

# Fare la differenza
print(f"Differenza di vendite: {vendite_gennaio-vendite_febbraio}")
# Differenza di vendite: Counter({'Tablet': 15, 'Laptop': 10})

#modificare i valore in the fly
vendite_gennaio["Laptop"] += 4
print(f"Vendite Gennaio: {vendite_gennaio}")
# Vendite Gennaio: Counter({'Laptop': 17, 'Tablet': 15})


# metodi da ricordare
#counter.most_common(n) #restituisce gli n elementi più frequenti
#counter.total() # somma dei conteggi

#Defaultdicts