import networkx as nx
from database.dao import DAO
from model.album import Album as a

class Model:
    def __init__(self):
        self.album_dict = {}
        self.connection_list = []
        self.graph = nx.Graph()

    def getAlbums(self, minuti):
        self.albums_list = DAO.get_albums(minuti)
        for album in self.albums_list:
            self.album_dict[album.id] = album

    def getConnections(self):
        self.connection_list = DAO.get_playlist()

    def build_graph(self, minuti: float):
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