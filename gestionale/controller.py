import flet as ft

from gestionale.gestoreOrdini import GestoreOrdini


class Controller:
    def __init__(self, view):
        self._view = view
        self._model = GestoreOrdini()

    #QUI DENTRO DEVO  METTERE ANCHE I METODI CHE POI ASSOCIO AGLI ON-CLICK DEI PULSANTI
    def add_ordine(self, e): #ricordati di mettere un secondo argomento = evento che genera il pulsante
        """legge i campi di testo e aggiunge un ordine al mio dec"""

        #prodotto
        nomePstr= self._view._txtInNomeP.value #VALUE NON è UN METODO MA UNA PROPRIETA'

        #incapsulo le convesrioni in un try
        try:
            prezzoP= float(self._view._txtInPrezzo.value)  # float
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Attenzione il prezzo deve essere un numero.", color= "red" ))
            self._view.update_page()
            return

        try:
            quantita = int(self._view._txtInQuantita.value)  # float
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Attenzione la quantità deve essere un numero.", color="red"))
            self._view.update_page()
            return

        #cliente
        nomeC= self._view._txtInNomeC.value
        mail = self._view._txtInMail.value
        categoria = self._view._txtInCategoria.value
        ordine= self._model.crea_ordine(nomePstr, prezzoP, quantita, nomeC, mail, categoria)
        self._model.add_ordine(ordine)

        self._view._txtInNomeP.value = ""
        self._view._txtInPrezzoP.value = ""
        self._view._txtInQuantitaP.value = ""
        self._view._txtInCategoriaP.value = ""
        self._view._txtInNomeC.value = ""
        self._view._txtInMailP.value = ""

        self._view._lvOut.controls.append(
            ft.Text()
        )

    def gestisci_ordine(self, e):
        pass
    def gestisci_all_ordini(self, e):
        pass
    def stampa_sommario(self, e):
        pass