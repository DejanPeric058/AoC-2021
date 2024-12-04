# A PART
with open("11.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
commands = [[int(a) for a in command] for command in commands]
print(commands)

class Octopus:
    def __init__(self, energy, positiony, positionx):
        self.energy = energy
        self.status = 'unflashed'
        self.positionx = positionx
        self.positiony = positiony

    def __repr__(self):
        return str(self.positiony) + ',' +  str(self.positionx) + ':' + str(self.energy)

    def increase_for_one(self):
        if self.positionx == 0 or self.positiony == 0 or self.positionx == 11 or self.positiony == 11:
            pass
        elif self.status == 'unflashed':
            self.energy += 1
            if self.energy > 9:
                #counter += 1
                self.status = 'flashed'
                self.energy = 0
                octopus_grid[self.positiony-1][self.positionx-1].increase_for_one()
                octopus_grid[self.positiony-1][self.positionx].increase_for_one()
                octopus_grid[self.positiony-1][self.positionx+1].increase_for_one()
                octopus_grid[self.positiony+1][self.positionx-1].increase_for_one()
                octopus_grid[self.positiony+1][self.positionx].increase_for_one()
                octopus_grid[self.positiony+1][self.positionx+1].increase_for_one()
                octopus_grid[self.positiony][self.positionx-1].increase_for_one()
                octopus_grid[self.positiony][self.positionx+1].increase_for_one()
                

octopus_grid = [[Octopus(-999999999,0,i) for i in range(12)]]
for i, command in enumerate(commands):
    octopus_grid += [[Octopus(-999999999,i+1,0)] + [Octopus(a,i+1,j+1) for j, a in enumerate(command)] + [Octopus(-999999999,i+1,11)]]
octopus_grid.append([Octopus(-999999999,12,i) for i in range(12)])
#print(octopus_grid)
#for _ in range(100):
flag = False
round= 0
while flag == False:
    counter = 0
    for octopus_row in octopus_grid[1:-1]:
        #print(octopus_row)
        for octopus in octopus_row[1:-1]:
            if octopus.positionx in [0,11] or octopus.positiony in [0,11]:
                octopus.status = 'flashed'
            octopus.increase_for_one()
    
    for octopus_row in octopus_grid[1:-1]:
        for octopus in octopus_row[1:-1]:
            if octopus.status == 'flashed':
                counter += 1
                octopus.status = 'unflashed'
    if counter == 100:
        flag = True
    round += 1


print(counter, round)

# B PART 