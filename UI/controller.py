import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def _fill_dropdown(self):
        self._view.dd_album.options.clear()
        all_album = self._model.getNodes()

        for a in all_album:
            # Solo text e data: value non serve
            option = ft.dropdown.Option(key=a.id,text=a)
            self._view.dd_album.options.append(option)

        # aggiorna il dropdown
        self._view.dd_album.update()

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO
        self._view.lista_visualizzazione_1.controls.clear()
        self._view.update()
        self._model.build_graph(self._view.txt_durata.value)
        self._view.lista_visualizzazione_1.controls.append(ft.Text(value=f'Grafo creato: {self._model.getNumberNodes()} album, {self._model.getNumberEdges()} archi'))
        self._fill_dropdown()
        self._view.update()



    def get_selected_album(self, e):
        """ Handler per gestire la selezione dell'album dal dropdown """""
        # TODO
        self._view.lista_visualizzazione_2.controls.clear()
        self._view.update()

    def handle_analisi_comp(self, e):
        """ Handler per gestire l'analisi della componente connessa """""
        # TODO
        self._view.lista_visualizzazione_2.controls.clear()
        album = self._view.dd_album.value
        minuti,n_componenti = self._model.get_connected(album)
        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Dimensioni componente: {len(n_componenti)}\nDurata totale: {minuti:0.2f} minuti"))
        self._view.update()

    def handle_get_set_album(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del set di album """""
        # TODO
        self._view.lista_visualizzazione_3.controls.clear()
        path,peso = self._model.get_info(self._view.dd_album.value, float(self._view.txt_durata_totale.value))
        self._view.lista_visualizzazione_3.controls.append(ft.Text(f"Set trovato ({len(path)} album, durata: {peso:0.2f} minuti):"))
        for p in path:
            self._view.lista_visualizzazione_3.controls.append(ft.Text(f"- {p.title} ({p.minuti:0.2f} min))"))
        self._view.update()
