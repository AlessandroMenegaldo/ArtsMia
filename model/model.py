import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._artObjectList = DAO.getAllObjects()
        self._grafo = nx.Graph()
        self._grafo.add_nodes_from(self._artObjectList)
        self._idMap = {}
        for v in self._artObjectList:
            self._idMap[v.object_id] = v

    def getConnessa(self, v0int):
        v0 = self._idMap[v0int]

        #modo1 : successori di v0 in DFS
        successors = nx.dfs_successors(self._grafo, v0)
        allSucc = []
        for v in successors.values(): #itero perché ho come successori delle liste di più elementi se un object è
                                      #legato a piu object.
                                      # (Ciò è gia verificato per predecessors perché da un elemento
                                      #risalgo solamente ad un altro object)
            allSucc.extend(v) #extend è come append ma lo fa con tutti gli elementi di iterable (come può essere v)

        # modo1 : predecessori di v0 in DFS
        predecessors = nx.dfs_predecessors(self._grafo, v0)

        # Modo3: conto i nodi dell'albero di visita
        tree = nx.dfs_tree(self._grafo, v0)


        # Modo4: node_connected_component (metodo già dato)
        connComp = nx.node_connected_component(self._grafo, v0)

        #nei metodi 3 e 4 verrà contato anche il nodo source
        #in 1 e 2 invece no

        return len(connComp)





    def creaGrafo(self):
        self.addEdges()

    def addEdges(self):
        allEdges = DAO.getAllConnessioni(self._idMap)
        for e in allEdges:
            self._grafo.add_edge(e.v1, e.v2, weight = e.peso)

    def checkExistece(self, idOggetto):
        return idOggetto in self._idMap

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)