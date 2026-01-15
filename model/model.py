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
        self.album_dict = {}
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
        for album in self.albums_list:
            self.graph.add_node(album)
        for arco1 in self.connection_list:
            if arco1.album_id not in self.album_dict:pass
            for arco2 in self.connection_list:
                if arco2.album_id in self.album_dict and arco1 == arco2 and (arco1.album_id, arco2.album_id) not in self.archi_visitati:
                    try:
                        self.graph.add_edge(self.album_dict[arco1.album_id], self.album_dict[arco2.album_id])
                        self.archi_visitati.add(arco1.album_id, arco2.album_id)
                    except Exception as e: continue
        return self.graph

    def getNodes(self):
        return self.albums_list
    def getNumberEdges(self):
        return self.graph.number_of_edges()

    def getNumberNodes(self):
        return self.graph.number_of_nodes()

    def get_connected(self,node):
        somma = 0
        self.componenti_connesse = nx.node_connected_component(self.graph, self.album_dict[int(node)])
        for componente in self.componenti_connesse:
            somma+=componente.minuti
        return somma,self.componenti_connesse

    def get_max_recursive(self, start, parz, peso_parz, visited, G_filtrato):
        if (len(parz) >= len(self.path_max) and peso_parz > self.peso_tot and peso_parz <= self.dTot) or (len(parz) > len(self.path_max) and peso_parz <= self.dTot):
            self.peso_tot = peso_parz
            self.path_max = list(parz)
        for neighbor in G_filtrato.neighbors(start):
            if  neighbor not in visited and neighbor not in parz:
                parz.append(neighbor)
                peso_parz += start.minuti + neighbor.minuti
                visited.add(neighbor)
                if peso_parz <= self.dTot:
                    self.get_max_recursive(neighbor, parz, peso_parz, visited, G_filtrato)
                parz.pop()
                visited.remove(neighbor)
                peso_parz -= start.minuti + neighbor.minuti

    def get_info(self, source, dTot):
        self.dTot = dTot
        self.peso_tot = 0
        self.path_max = []
        visitati = set()
        G_filtrato = self.graph.subgraph(self.componenti_connesse)
        source = self.album_dict[int(source)]
        visitati.add(source)
        self.get_max_recursive(source, [source], 0, visitati, G_filtrato)
        return self.path_max, self.peso_tot