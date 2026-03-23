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
        if nomePstr == "":
            self._view._lvOut.controls.append(ft.Text("Attenzione il campo nome prodotto non può essere vuoto", color="red"))
            self._view.update_page()
            return

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
        if nomeC == "":
            self._view._lvOut.controls.append(
                ft.Text("Attenzione il campo nome cliente non può essere vuoto", color="red"))
            self._view.update_page()
            return

        mail = self._view._txtInMail.value
        if mail == "":
            self._view._lvOut.controls.append(ft.Text("Attenzione il campo email non può essere vuoto", color="red"))
            self._view.update_page()
            return

        categoria = self._view._txtInCategoria.value
        if categoria == "":
            self._view._lvOut.controls.append(ft.Text("Attenzione il campo categoria non può essere vuoto", color="red"))
            self._view.update_page()
            return

        ordine= self._model.crea_ordine(nomePstr, prezzoP, quantita, nomeC, mail, categoria)
        self._model.add_ordine(ordine)

        self._view._txtInNomeP.value = ""
        self._view._txtInPrezzo.value = ""
        self._view._txtInQuantita.value = ""
        self._view._txtInCategoria.value = ""
        self._view._txtInNomeC.value = ""
        self._view._txtInMail.value = ""

        self._view._lvOut.controls.append(
            ft.Text("Ordine correttamente inserito.", color="green"))
        self._view._lvOut.controls.append(ft.Text("Dettagli dell'ordine:")
        )
        self._view._lvOut.controls.append( ft.Text(ordine.riepilogo())
        )
        self._view._lvOut.controls.append(ft.Text("\n"))

        self._view.update_page()

    def gestisci_ordine(self, e):
        self._view._lvOut.controls.clear()
        res, ordine = self._model.processa_prossimo_ordine()

        if res: #True= ordine processato
            self._view._lvOut.controls.append(ft.Text("Ordine processato con successo:", color="green"))
            self._view._lvOut.controls.append( ft.Text(ordine.riepilogo()))
            self._view.update_page()

        else:
            self._view._lvOut.controls.append(ft.Text("Non ci sono ordini in coda.", color= "blue"))
            self._view.update_page()


    def gestisci_all_ordini(self, e):
        self._view._lvOut.controls.clear()
        ordini = self._model.processa_tutti_ordini() #LISTA di oggetti di tipo ordine

        if not ordini: #se la lista è vuota nn ho ordini da evadere
            self._view._lvOut.controls.append(ft.Text("Non ci sono ordini in coda.", color="blue"))
            self._view.update_page()
        else:
            self._view._lvOut.controls.append(ft.Text("\n"))
            self._view._lvOut.controls.append(ft.Text(f"Ho processato "
                                                      f"correttamente {len(ordini)} ordini.", color= "green"))
            for o in ordini:
                self._view._lvOut.controls.append( ft.Text(o.riepilogo()))
            self._view.update_page()

    def stampa_sommario(self, e):
        self._view._lvOut.controls.clear()
        self._view._lvOut.controls.append(ft.Text("Di seguito il sommario dello stato del business.", color="orange"))
        self._view._lvOut.controls.append(ft.Text(self._model.get_riepilogo()))
        self._view.update_page()
