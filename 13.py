# A PART
with open("13.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')

commands2 = []
maximumx, maximumy = 0, 0
for command in commands:
    if command == '':
        break
    commands2.append((int(command.split(',')[0]), int(command.split(',')[1])))
    maximumx, maximumy = max(maximumx, int(command.split(',')[0])), max(maximumy, int(command.split(',')[1]))
folds = []
for command in commands:
    if command != '' and command[0] == 'f':
        info = command.split()[2]
        way = info[0]
        position = int(info.split('=')[1])
        folds.append((way, position))
print(commands2, maximumx, maximumy, folds)
def draw_paper(commands2, maximumx, maximumy):
    paper = []
    for _ in range(maximumy+1):
        row = []
        for _ in range(maximumx+1):
            row += '.'
        paper.append(row)
    for (x, y) in commands2:
        paper[y][x] = '#'
    #for a in paper:
    #    print(a)
    return paper

draw_paper(commands2, maximumx, maximumy)

for (way, position) in folds:
    new_commands2 = set()
    if way == 'y':
        for (x,y) in commands2:
            if y > position:
                new_commands2.add((x,y-2*(y-position)))
            else:
                new_commands2.add((x,y))
        maximumy = position - 1
        commands2 = new_commands2
        paper = draw_paper(commands2, maximumx, maximumy)
        #for a in paper:
        #    print(a)
    else:
        for (x,y) in commands2:
            if x > position:
                new_commands2.add((x-2*(x-position),y))
            else:
                new_commands2.add((x,y))
        maximumx = position - 1
        commands2 = new_commands2
        paper = draw_paper(commands2, maximumx, maximumy)
        #for a in paper:
        #    print(a)
print(folds)
for a in paper:
        print(a)
for row in paper:
    for a in row:
        if a == '#':
            counter += 1
print(counter)
niz = ''
for row in paper:
    for a in row:
        niz += a
    niz += '\n'
print(niz)
# B PART 