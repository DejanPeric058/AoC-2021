# A PART
with open("15.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
commands = [[int(a) for a in command] for command in commands]
print(commands)

class Graph:
    def __init__(self, info_for_nodes):
        self.info_for_nodes = info_for_nodes
        self.nodes = {}
        self.maximum = len(self.info_for_nodes)-1, len(self.info_for_nodes[0])-1

    def create_graph(self):
        for i, row in enumerate(self.info_for_nodes):
            for j, a in enumerate(row):
                self.nodes[str(i) + ',' + str(j)] = (Node(a, i, j))
        #print(self.maximum)
        for i, row in enumerate(self.info_for_nodes):
            for j, a in enumerate(row):
                if i == 0:
                    if j == 0:
                        output = [self.nodes[str(i+1) + ',' + str(j)], self.nodes[str(i) + ',' + str(j+1)]]
                    elif j == self.maximum[1]:
                        output = [self.nodes[str(i) + ',' + str(j-1)],self.nodes[str(i+1) + ',' + str(j)]]
                    else:
                        output = [self.nodes[str(i) + ',' + str(j-1)], self.nodes[str(i+1) + ',' + str(j)], self.nodes[str(i) + ',' + str(j+1)]]
                elif i == self.maximum[0]:
                    if j == 0:
                        output = [self.nodes[str(i-1) + ',' + str(j)],self.nodes[str(i) + ',' + str(j+1)]]
                    elif j == self.maximum[1]:
                        output = [self.nodes[str(i-1) + ',' + str(j)], self.nodes[str(i) + ',' + str(j-1)]]
                    else:
                        output = [self.nodes[str(i-1) + ',' + str(j)], self.nodes[str(i) + ',' + str(j-1)], self.nodes[str(i) + ',' + str(j+1)]]
                elif j == 0:
                    output = [self.nodes[str(i-1) + ',' + str(j)], self.nodes[str(i+1) + ',' + str(j)], self.nodes[str(i) + ',' + str(j+1)]]
                elif j == self.maximum[1]:
                    output = [self.nodes[str(i-1) + ',' + str(j)], self.nodes[str(i) + ',' + str(j-1)], self.nodes[str(i+1) + ',' + str(j)]]
                else:
                    output = [self.nodes[str(i-1) + ',' + str(j)], self.nodes[str(i) + ',' + str(j-1)],self.nodes[str(i+1) + ',' + str(j)], self.nodes[str(i) + ',' + str(j+1)]]
                self.nodes[str(i) + ',' + str(j)].add_neighbours(output)
                #print(str(i) + ',' + str(j))
class Node:
    def __init__(self, cost, i, j):
        self.position = (i, j)
        self.name = str(i) + ',' + str(j)
        self.cost = cost
        self.output = []
        self.distance = 9999999999
        if i == 0 and j == 0:
            self.distance = 0
        
    def add_neighbours(self, output):
        self.output = output

my_caves = Graph(commands)
my_caves.create_graph()


def dijkstra(sptSet={my_caves.nodes['0,0']}):
    while len(list(sptSet)) < (my_caves.maximum[0]+1) * (my_caves.maximum[1]+1):
        neighbours = {}
        for node in sptSet:
            for subnode in node.output:
                #print(subnode)
                if subnode not in sptSet:
                    subnode.distance = node.distance + subnode.cost
                    neighbours[subnode.name] = subnode.distance
        new_node_name = min(neighbours, key=neighbours.get)
        sptSet.add(my_caves.nodes[new_node_name])
    return my_caves.nodes[str(my_caves.maximum[0]-1) + ',' + str(my_caves.maximum[0]-1)].distance

print(dijkstra())
# B PART 