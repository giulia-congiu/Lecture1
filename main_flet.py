import flet as ft

from UI.controller import Controller
from UI.view import View


def main(page: ft.Page):
    v = View(page) #creo da solo il view e gli dico dove deve scrivere l'interfaccia
    c = Controller(v) #lo do al controllo
    v.set_controller(c) #do il controller al view
    v.carica_interfaccia() #crea gli oggetti grafici e li associa ai metodi del controller
    
ft.app(target= main) #ha come argomento la funzione che regola il comportamento della interfaccia