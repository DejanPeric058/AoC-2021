# A PART
with open("10.txt") as f:
    text = f.read()
commands = text.split('\n')
#print(commands)

my_dict1 = {
    ')' : 0,
    ']' : 0,
    '}' : 0,
    '>' : 0
}
for command in commands:
    #print('start: ' + command)
    while '{}' in command or '<>' in command or '()' in command or '[]' in command:
        command = command.replace('{}', '')
        command = command.replace('()', '')
        command = command.replace('<>', '')
        command = command.replace('[]', '')
    command = command.replace('{', '')
    command = command.replace('(', '')
    command = command.replace('<', '')
    command = command.replace('[', '')
    if command != '':
        my_dict1[command[0]] += 1
    #print('end: ' + command)

print(3*my_dict1[')'] + 57*my_dict1[']'] + 1197*my_dict1['}'] + 25137*my_dict1['>'])
# B PART 
commands = text.split('\n')
#print(commands)

my_dict2 = {
    '(' : 1,
    '[' : 2,
    '{' : 3,
    '<' : 4
}
scores = []
for command in commands:
    #print('start: ' + command)
    while '{}' in command or '<>' in command or '()' in command or '[]' in command:
        command = command.replace('{}', '')
        command = command.replace('()', '')
        command = command.replace('<>', '')
        command = command.replace('[]', '')
    command1 = command.replace('{', '')
    command1 = command1.replace('(', '')
    command1 = command1.replace('<', '')
    command1 = command1.replace('[', '')
    if command1 == '':
        trenutno_vsota = 0
        for a in command[::-1]:
            trenutno_vsota = 5*trenutno_vsota + my_dict2[a]
        scores.append(trenutno_vsota)

print(sorted(scores)[len(scores)//2])


    #print('end: ' + command)