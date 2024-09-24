# A PART
with open("02.txt") as f:
    text = f.read()
depth = 0
hor_position = 0
commands = text.split('\n')
commands = [(i.split(' ')[0], int(i.split(' ')[1])) for i in commands]
for way, steps in commands:
    if way == 'forward':
        hor_position += steps 
    if way == 'down':
        depth += steps
    if way == 'up':
        depth -= steps
print(depth*hor_position)
# B PART 
depth = 0
hor_position = 0
aim = 0
for way, steps in commands:
    if way == 'forward':
        hor_position += steps 
        depth += aim * steps
    if way == 'down':
        aim += steps
    if way == 'up':
        aim -= steps
print(depth*hor_position)
