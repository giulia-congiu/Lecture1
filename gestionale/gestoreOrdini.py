"""
Scrivere un software gestionale che abbia le seguenti funzionalità:
1) supportare l'arrivo e la gestione di ordini.
1bis) quando arriva un nuovo ordine, lo aggiungo ad una coda,
assicurandomi che sia eseguito solo dopo gli altri.
2) avere delle funzionalità per avere statistiche sugli
ordini
3) fornire statistiche sulla distribuzione di ordini per categoria di cliente.
"""
from collections import deque, Counter, defaultdict

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


class GestoreOrdini: #MODELLO
    def __init__(self):
        self._ordini_daProcessare=deque()
        self._ordini_processati=[]  #a quel punto non importa l'ordinamento
        self._statistiche_prodotti= Counter()
        self._ordiniPer_categoria= defaultdict(list) #diz. con chiavi=cateoria e valori=ordini
        #uso il default dic per non gestire il controllo dell 'esiste quella categoria?' no? e allora creamela

    def add_ordine(self, ordine: Ordine):
        """aggiunge un nuovo ordine agli elementi da gestire"""
        self._ordini_daProcessare.append(ordine)
        print(f"Ricevuto un nuovo ordine da parte di {ordine.cliente}.")
        print(f"Ordini ancora da evadere: {len(self._ordini_daProcessare)}")

    def crea_ordine (self, nomeP, prezzoP, quantitaP, nomeC, mailC,categoriaC):
        return Ordine([RigaOrdine(ProdottoRecord(nomeP, prezzoP), quantitaP)], ClienteRecord(nomeC, mailC, categoriaC))

    def processa_prossimo_ordine(self):
        """Questo metodo legge il prossimo ordine in coda e lo gestisce"""
        print("\n" + "-" * 60)
        print("\n" + "-" * 60)
        # controllo se ho ordini da processare:
        if not self._ordini_daProcessare:
            print("Non ci sono ordini in coda")
            return False

        #se esiste, gestisco il primo in coda
        ordine=self._ordini_daProcessare.popleft() #logica FIFO
        print(f"Sto processando l'ordine di {ordine.cliente}")
        print(ordine.riepilogo())

        #aggiorno statistiche interne: per ognuno dei prodotti venduti che sta dentro l'ordine, aggiorno il counter
        for riga in ordine.righe:
            self._statistiche_prodotti[riga.prodotto.name] += riga.quantita
            #ottengo un counter con una lista di nomi di prodotti e per ciascun prodotto,
            #mi verrà detto quante volte è stato venduto

        #raggruppare ordini per categoria
        self._ordiniPer_categoria[ordine.cliente.categoria].append(ordine)
        #questo dizionario, associa alla chiave categoria, l'ordine che sto gestendo ora

        #Archiviamo l'ordine
        self._ordini_processati.append(ordine)

        print("ORDINE CORRETTAMENTE PROCESSATO")

        return True


    #potrei pensare a un metodo che gestisce tutti gli ordini insieme
    def processa_tutti_ordini(self):
        """Processa tutti gli ordini attualmente presenti in coda"""
        print("\n" + "=" * 60)
        print(f"Processando {len(self._ordini_daProcessare)} ordini")
        while self._ordini_daProcessare:
            self.processa_prossimo_ordine()
        print("Tutti gli ordini sono stati processati")

    def get_statistiche_prodotti(self, top_n: int=5): #gli do 5 come valore di default se non ne viene inserito un altro
        """Questo metodo ridà info sui prodotti più venduti"""
        #non fa stampe, da solo informazioni
        valori=[]
        for prodotto, quantita in self._statistiche_prodotti.most_common(top_n): #mi dà i 5 prodotti più venduti
            valori.append((prodotto, quantita))
        return valori #restituisco una lista di tuple

    def get_distribuzione_categorie(self):
        """Questo metodo restituisce info su totale fatturato per ogni categoria presente"""
        valori=[] #lista di tuple
        for categ in self._ordiniPer_categoria.keys(): #ciclo su tutte le chiavi che sarebbero categorie
            ordini= self._ordiniPer_categoria[categ] #per ogni chiave prendo la lista di ordini effettuati associati ad essa
            totale_Fatturato= sum([o.totale_lordo(0.22) for o in ordini]) #per ogni ordine prendo il totale lordo e poi sommo
            valori.append((categ, totale_Fatturato))
        return valori

        #QUESTI GET GLI HO FATTI PERCHE': essendo attributi che ho messo privati, voglio che sia visibile
            #solo quello che decido io quindi con la get SCELGO IO come e cosa restituire

    def stampa_riepilogo(self):
        """Stampa info di massima"""
        print("\n" + "="*60)
        print("Stato attuale del business")
        print(f"Ordini correttamente gestiti: {len(self._ordini_processati)}")
        print(f"Ordini in coda: {len(self._ordini_daProcessare)}")

        print("Prodotti + venduti:")
        for prod, quantita in self.get_statistiche_prodotti():
            print(f"{prod}: {quantita}")

        print(f"Fatturato per categoria:")
        for cat, fatturato in self.get_distribuzione_categorie():
            print(f"{cat}: {fatturato}")

def test_modulo():
    sistema= GestoreOrdini() #creo un istanza della classe
    ordini= [
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)],
            ClienteRecord("Mario Rossi", "mario@gmail.com", "Gold")),
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 2),
            RigaOrdine(ProdottoRecord("Tablet", 500.0), 1),
            RigaOrdine(ProdottoRecord("Cuffie", 250.0), 3)],
            ClienteRecord("Fulvio Bianchi", "fulvio@gmail.com", "Gold")),
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 2),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 2)],
            ClienteRecord("Giulia Congiu", "giulia@gmail.com", "Silver")),
        Ordine([
            RigaOrdine(ProdottoRecord("Tablet", 900.0), 1),
            RigaOrdine(ProdottoRecord("Cuffie", 250.0), 3)],
            ClienteRecord("Alessia Neri", "alessia@gmail.com", "Gold")),
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)],
            ClienteRecord("Antonio Pes", "antonio@gmail.com", "Bronze"))
    ]


    for o in ordini:
        sistema.add_ordine(o)

    sistema.processa_tutti_ordini()
    sistema.stampa_riepilogo()

if __name__ == "__main__":
    test_modulo()
