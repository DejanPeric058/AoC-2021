# A PART
import pprint

with open("12.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
commands = [(command.split('-')[0], command.split('-')[1]) for command in commands]
#print(commands)


class Cave:
    def __init__(self, name):
        self.name = name
        self.small_cave = True
        self.visited = False
        if name.upper() == name:
            self.small_cave = False
        self.neighbours = []

    def __repr__(self):
        return str(self.neighbours)

    def add_neighbour(self, neighbour_name):
        self.neighbours.append(neighbour_name)

    def find_paths(self, caves, path):
        global counter
        if self.name == 'end':
            counter += 1
            #print(path+ ' - end')
        elif (self.small_cave and (self.name not in path)) or not self.small_cave:
            caves[self.name].visited = True
            path = path + ' - ' + self.name
            for neighbour in self.neighbours:
                new_caves = caves.copy()
                new_caves[neighbour].find_paths(new_caves, path)

    def find_paths_b(self, caves, path, flag):
        global counter
        if self.name == 'end':
            counter += 1
            #print(path+ ' - end')
        elif (self.small_cave and self.name in path) and flag:
            caves[self.name].visited = True
            path = path + ' - ' + self.name
            for neighbour in self.neighbours:
                if neighbour != 'start':
                    new_caves = caves.copy()
                    new_caves[neighbour].find_paths_b(new_caves, path, False)
        elif (self.small_cave and (self.name not in path)) or not self.small_cave:
            caves[self.name].visited = True
            path = path + ' - ' + self.name
            for neighbour in self.neighbours:
                if neighbour != 'start':
                    new_caves = caves.copy()
                    new_caves[neighbour].find_paths_b(new_caves, path, flag)

def add_neighbours(vertex1, vertex2, cave_system):
    cave_system[vertex1].add_neighbour(vertex2)
    cave_system[vertex2].add_neighbour(vertex1)

def add_caves(commands):
    cave_system = {}
    for (a,b) in commands:
        if a not in cave_system.keys():
            cave_system[a] = Cave(a)
        if b not in cave_system.keys():
            cave_system[b] = Cave(b)
        add_neighbours(a,b,cave_system=cave_system)
    return cave_system

my_caves = add_caves(commands=commands)
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(my_caves)
my_caves['start'].find_paths(my_caves, '')
counter = 0
my_caves['start'].find_paths_b(my_caves, '', True)
print(counter)



# Najprej bi samo ustvaru vse jame, in vsaki jami bi
# dodal atribut sosedi, kjer bi dodal sosedne jame.
# Pol bi naredu funkcijo definirano na jami.
# Kinda rekurzivno. Če je jami ime 'End', zaključi,
# dodaj counterju +1. Rekurzivna funkcija vzame zraven 
# slovar jam, kljuci so imena jam, vrednosti so jame.  

# B PART 