# A PART
with open("05.txt") as f:
    text = f.read()
commands = text.split('\n')
my_dict = {}
for command in commands:
    start_x, start_y, end_x, end_y = command.split(' -> ')[0].split(',')[0], command.split(' -> ')[0].split(',')[1], command.split(' -> ')[1].split(',')[0], command.split(' -> ')[1].split(',')[1]
    start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(end_x), int(end_y)
    
    if start_x == end_x:
        for a in range(min(start_y, end_y), max(start_y, end_y)+1):
            if str(start_x) + ',' + str(a) not in my_dict.keys():
                my_dict[str(start_x) + ',' + str(a)] = 1
            else:
                my_dict[str(start_x) + ',' + str(a)] += 1
    elif start_y == end_y:
        for b in range(min(start_x, end_x), max(start_x, end_x)+1):
            if str(b) + ',' + str(start_y) not in my_dict.keys():
                my_dict[str(b) + ',' + str(start_y)] = 1
            else:
                my_dict[str(b) + ',' + str(start_y)] += 1
overlaps = [k for k, v in my_dict.items() if v > 1]
print(len(overlaps))
# B PART 
my_dict = {}
for command in commands:
    start_x, start_y, end_x, end_y = command.split(' -> ')[0].split(',')[0], command.split(' -> ')[0].split(',')[1], command.split(' -> ')[1].split(',')[0], command.split(' -> ')[1].split(',')[1]
    start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(end_x), int(end_y)
    
    if start_x == end_x:
        for a in range(min(start_y, end_y), max(start_y, end_y)+1):
            if str(start_x) + ',' + str(a) not in my_dict.keys():
                my_dict[str(start_x) + ',' + str(a)] = 1
            else:
                my_dict[str(start_x) + ',' + str(a)] += 1
    elif start_y == end_y:
        for b in range(min(start_x, end_x), max(start_x, end_x)+1):
            if str(b) + ',' + str(start_y) not in my_dict.keys():
                my_dict[str(b) + ',' + str(start_y)] = 1
            else:
                my_dict[str(b) + ',' + str(start_y)] += 1
    elif start_x - end_x == -(start_y - end_y):
        for a, b in zip(range(max(start_x, end_x), min(start_x, end_x)-1, -1), range(min(start_y, end_y), max(start_y, end_y)+1)):
            if str(a) + ',' + str(b) not in my_dict.keys():
                my_dict[str(a) + ',' + str(b)] = 1
            else:
                my_dict[str(a) + ',' + str(b)] += 1
    elif start_x - end_x == start_y - end_y:
        for a, b in zip(range(min(start_x, end_x), max(start_x, end_x)+1), range(min(start_y, end_y), max(start_y, end_y)+1)):
            
            if str(a) + ',' + str(b) not in my_dict.keys():
                my_dict[str(a) + ',' + str(b)] = 1
            else:
                my_dict[str(a) + ',' + str(b)] += 1
        pass
overlaps = [k for k, v in my_dict.items() if v > 1]
print(len(overlaps))
