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
    """Restituisce prezzo totale, medio, minimo"""
    prezzi= [p.prezzo_unitario for p in carrello]
    return (sum(prezzi), sum(prezzi)/len(prezzi), max(prezzi), min(prezzi))

tot, media, max, min = calcola_statistiche_carrello(carrello)
#oppure
#tot, *altri_campi = calcola_statistiche_carrello(carrello)
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

#metodi utili x test
s=set()
s.add((ProdottoRecord("aaa", 20.0)
s.update([ProdottoRe])










