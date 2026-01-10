import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def _fill_dropdown(self):
        """Popola il dropdown con i rifugi presenti nel grafo."""
        self._view.dd_album.options.clear()
        all_album = self._model.getNodes()

        for a in all_album:
            # Solo text e data: value non serve
            option = ft.dropdown.Option(text=a)
            self._view.dd_album.options.append(option)

        # aggiorna il dropdown
        self._view.dd_album.update()

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO
        self._model.build_graph(self._view.txt_durata.value)
        self._view.lista_visualizzazione_1.controls.clear()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(value=f'Grafo creato:{self._model.getNumberNodes()} album, {self._model.getNumberEdges()} archi'))
        self._fill_dropdown()
        self._view.update()



    def get_selected_album(self, e):
        """ Handler per gestire la selezione dell'album dal dropdown """""
        # TODO

    def handle_analisi_comp(self, e):
        """ Handler per gestire l'analisi della componente connessa """""
        # TODO

    def handle_get_set_album(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del set di album """""
        # TODO