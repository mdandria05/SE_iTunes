import networkx as nx
from database.dao import DAO
from model.album import Album as a

class Model:
    def __init__(self):
        self.album_dict = {}
        self.connection_list = []
        self.graph = nx.Graph()
        self.componenti_connesse = None

    def getAlbums(self, minuti):
        self.albums_list = DAO.get_albums(minuti)
        for album in self.albums_list:
            self.album_dict[album.id] = album

    def getConnections(self):
        self.connection_list = DAO.get_playlist()

    def build_graph(self, minuti: float):
        self.graph.clear()
        self.archi_visitati = set()
        self.getAlbums(minuti)
        self.getConnections()
        for arco1 in self.connection_list:
            if arco1.album_id not in self.album_dict: pass
            for arco2 in self.connection_list:
                if arco2.album_id in self.album_dict and arco1 == arco2 and (arco1.album_id, arco2.album_id) not in self.archi_visitati:
                    try:
                        self.graph.add_edge(self.album_dict[arco1.album_id], self.album_dict[arco2.album_id])
                        self.archi_visitati.add(arco1.album_id, arco2.album_id)
                    except Exception as e: continue
        return self.graph

    def getNodes(self):
        self.albums_list = []
        for node in self.graph.nodes:
            self.albums_list.append(node.title)
        return self.albums_list
    def getNumberEdges(self):
        return self.graph.number_of_edges()

    def getNumberNodes(self):
        return self.graph.number_of_nodes()

    def get_connected(self,node):
        somma = 0
        for n in self.graph.nodes:
            if node == n.title:
                self.componenti_connesse = nx.node_connected_component(self.graph, n)
                break
        for componente in self.componenti_connesse:
            somma+=componente.minuti
        return somma,self.componenti_connesse

    def get_info(self, max_minuti, album_scelto):
        final_path_max = {}
        componenti_list = []
        tot_minuti = 0
        for album in self.componenti_connesse:
            if album.title == album_scelto:
                if float(max_minuti) < album.minuti: return None
                final_path_max[album.title] = album.minuti
                tot_minuti += album.minuti
            else: componenti_list.append(album)
        componenti_list.sort(key=lambda x: x.minuti)
        for album in componenti_list:
            if tot_minuti+album.minuti < float(max_minuti):
                final_path_max[album.title] = album.minuti
                tot_minuti += album.minuti
            else: break
        return final_path_max