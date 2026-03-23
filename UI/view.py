import flet as ft
#txt= contiene testo
#In= riceve imput

class View:
    def __init__(self, page):
        self._controller = None  # non è obbligatorio ma è buona norma
        self._page = page
        self._page.title= "TDP 2025 - Software gestionale"
        self._page.horizontal_alignment = "CENTER"
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self._txtInNomeP =None
        self._txtInPrezzo =None
        self._txtInQuantita =None
        self._txtInCategoria =None
        self._txtInMail =None
        self._txtInNomeC = None
        self.update_page()

    def set_controller(self, c):
        self._controller = c   #c=istanza del controller che ho creato nel main

    def carica_interfaccia(self ):
        #prodotto
        self._txtInNomeP = ft.TextField(label = "Nome Prodotto", width=200)
        self._txtInPrezzo= ft.TextField(label = "Prezzo", width=200)
        self._txtInQuantita= ft.TextField(label = "Quantita", width=200)
        row1 = ft.Row(controls=[self._txtInNomeP,self._txtInPrezzo, self._txtInQuantita],
                      alignment= ft.MainAxisAlignment.CENTER)

        #CLIENTE
        self._txtInNomeC= ft.TextField(label = "Nome Cliente", width=200)
        self._txtInMail= ft.TextField(label = "Mail", width=200)
        self._txtInCategoria= ft.TextField(label = "Categoria", width=200)
        row2= ft.Row(controls=[self._txtInNomeC,self._txtInMail, self._txtInCategoria],
                     alignment= ft.MainAxisAlignment.CENTER)

        #BUTTONS
        #aggiungere nuovo ordine
        self._btnAdd= ft.ElevatedButton(text= "Aggiungi ordine", #mi serve cosa c'è scritto sul pulsante
                                        on_click= self._controller.add_ordine, # e cosa succede quando lo clicco
                                        width=200)
        #processare un ordine
        self._btnGestisciOrdine= ft.ElevatedButton(text= "Gestisci prossimo ordine",
                                        on_click= self._controller.gestisci_ordine,
                                        width=200)
        #processare tutti gli ordini
        self._btnGestiscAllOrdini= ft.ElevatedButton(text= "Gestisci tutti gli ordini",
                                        on_click= self._controller.gestisci_all_ordini,
                                        width=200)

        #stampare
        self._btnStampaInfo = ft.ElevatedButton(text= "Stampa sommario",
                                        on_click= self._controller.stampa_sommario,
                                        width=200)

        row3= ft.Row(controls=[self._btnAdd,self._btnGestisciOrdine, self._btnGestiscAllOrdini, self._btnStampaInfo],
                                alignment= ft.MainAxisAlignment.CENTER)

        self._lvOut = ft.ListView(expand=True)
        self._page.add(row1, row2, row3, self._lvOut)






    def update_page(self):
        self._page.update()