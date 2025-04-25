class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        if node not in self.adjacent_list:
            self.adjacent_list[node] = []
            self.number_of_nodes += 1
            return

    def add_edge(self, node1, node2):
        if node2 not in self.adjacent_list[node1]:
            self.adjacent_list[node1].append(node2)
            self.adjacent_list[node2].append(node1)
            return
        return 'Edge already exists'

    def show_connections(self):
        for node in self.adjacent_list:
            print(f'{node} -->> {" ".join(map(str, self.adjacent_list[node]))}')


myGraph = Graph()
myGraph.add_vertex('0')
myGraph.add_vertex('1')
myGraph.add_vertex('2')
myGraph.add_vertex('3')
myGraph.add_vertex('4')
myGraph.add_vertex('5')
myGraph.add_vertex('6')
myGraph.add_edge('3','1')
myGraph.add_edge('3','4')
myGraph.add_edge('4','2')
myGraph.add_edge('4','5')
myGraph.add_edge('1','2')
myGraph.add_edge('1','0')
myGraph.add_edge('0','2')
myGraph.add_edge('6','5')
myGraph.show_connections()



