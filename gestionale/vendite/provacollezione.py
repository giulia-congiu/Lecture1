import copy

from gestionale.core.prodotti import ProdottoRecord
from main_colorato import p2

p1=  ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)
p3 = ProdottoRecord("Auricolari", 250.0)

#LISTE

carrello = [p1,p2,p3, ProdottoRecord("tablet", 750.0)]

print("Prodotti nel carrello")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name}-  {p.prezzo_unitario}")

tot = sum(p.prezzo_unitario for p in carrello)
print(f"Totale del carrello: {tot}")

#aggiungere
carrello.append(ProdottoRecord("Monitor", 150.0))
carrello.extend([ProdottoRecord("AAA", 100.0)])
carrello.insert(2, ProdottoRecord("ccc", 250.0))

#rimuovere
carrello.pop() #rimuove ultimo elemento
carrello.pop(2) #rimuove elemento in posizione 2
carrello.remove(p1) #elimino la prima occorrenza di p1
carrello.clear() #elimina tutto

#sorting
carrello.sort() #ordina per ordinamento naturale
carrello.sort(reverse=True) #ordina al contrario
#carrello.sort(key=funciotn )
carrello_ordinato= sorted(carrello) #prende carello lo riordina e gli cambia none.

carrello.reverse() #mi rida la lista al contrario
carrello_copia= carrello.copy() #fa una copia di carrello. °shallow copy: GLI OGGETTI
                                # contenuti nelle due liste sono gli stessi
carrello_copia2= copy.deepcopy(carrello) #crea una lista con oggetti nuovi

#TUPLE--> IMMUTABILE
sede_principale=(45, 8) #coordinate della sede 1: lat e long
sede_Milano=(45,9 )

print(f"Sede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")

aliquoteIva=(
        ("Standard", 0.22),
        ("Ridotta", 0.10),
        ("Alimentari", 0.04),
        ("Esente", 0.0)
    )

for descr, valore in aliquoteIva:
    print(f"{descr}: {valore*100}%")

def calcola_statistiche_carrello(carrello):
    """Restituisce prezzo totale, prezzo medio, massimo e minimo"""
    prezzi = [p.prezzo_unitario for p in carrello]
    return (sum(prezzi), sum(prezzi)/len(prezzi), max(prezzi), min(prezzi))


tot, media, max, min = calcola_statistiche_carrello(carrello)

# tot, *altri_campi = calcola_statistiche_carrello(carrello)
print(tot)

#SET
categorie={"Gold", "Silver", "Bronze", "Gold"}
print(categorie)
print(len(categorie))
categorie2={"Platinum", "Elite"}
categorie_all=categorie | categorie2 #unione
print(categorie_all)

categorie_comuni= categorie & categorie2 #solo elementi comune
print(categorie_comuni)

categorie_esclusive=categorie - categorie2 #elementi presenti in uno dei due
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

elem= ProdottoRecord("bbb", 30)
#togliere
s.remove(elem) #rimuove un elemento. Raise KeyError se non esiste.
s.discard(elem) #rimuove un elemento, senza "arrabbiarsi" se questo non esiste.
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
print(f"Cerco un altro oggetto: {catalogo["non esiste"]}")
prod1= catalogo.get("non esiste")
if prod1 is None:
    print("Prodotto non trovato")
prod2=catalogo.get("non esiste", ProdottoRecord("Sconosciuto", 0))

print(prod2)

keys= list(catalogo.keys())
values= list(catalogo.values())

for k in keys:
    print(k)

for v in values:
    print(v)

for key, val in catalogo.items():
    print(f"Cod {key} è associata a {val}")

#rimuovere dal diz
rimosso= catalogo.pop("LAP002")
print(rimosso)

#DICT COMPREHENSION
prezzi ={codice: prod.prezzo_unitario for codice, prod in catalogo.items()}

#DA RICORDARE PER DICT
# d[key]= v #scrivo sul dizionario
# v =d[key] #leggere--restituisce key error se nn esiste
# v =d.get(key, default) #legge senza rischiare key error.
# #CONTINUAAAAAA

"""ESERCIZIO
per ciascuno dei seguenti casi, decidere quale struttura usare:

1) Memorizzare un elenco di ordini che dovranno essere processati in ordine di arrivo: lista
2) Memorizzare i CF dei clienti (univoco): set 
3) Creare un database di prodotti che posso cercare con un codice univoco: diz con chiave come codice e oggetto prodotto 
4) Memorizzare le coordinate gps della nuova sede di Roma: tupla
5) Tenere traccia delle categorie di clienti che hanno fatto un ordine in un certo range temporale
"""
