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

from gestionale.vendite.ordini import Ordine


class GestoreOrdini:
    def __init__(self):
        self._ordini_daProcessare=deque()
        self._ordini_processati=[]  #a quel punto non importa l'ordinamento
        self._statistiche_prodotti= Counter()
        self._ordiniPer_categoria= defaultdict(list) #diz. con chiavi=cateoria e valori=ordini

    def add_ordine(self, ordine: Ordine):
        """aggiunge un nuovo ordine agli elementi da gestire"""
        self._ordini_daProcessare.append(ordine)
        print(f"Ricevuto un nuovo ordine da parte di {ordine.cliente}.")
        print(f"Ordini ancora da evadere: {len(self._ordini_daProcessare)}")

    def processa_prossimo_ordine(self):
        """Questo metodo legge il prossimo ordine in coda e lo gestisce"""
        if not self._ordini_daProcessare:
            #controllo se ho ordini
            print("Non ci sono ordini in coda")
            return False

        ordine=self._ordini_daProcessare.popleft() #logica FIFO
        print(f"Sto processando l'ordine di {ordine.cliente}")
        print(ordine.riepilogo())

        #aggiorno statistiche interne: per ognuno dei prodotti venduti che sta dentro l'ordine, aggiorno il counter
        for riga in ordine.righe:
            self._statistiche_prodotti[riga.prodotto.name] += riga.quantita
            #ottengo un counter con una lista di nomi di prodotti e per ciascun prodotto,
            #mi verrà detto quante volte è stato venduto

