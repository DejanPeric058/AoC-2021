# A PART
with open("01.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
commands = [int(j) - int(i) for i,j in zip(commands, commands[1:])]
for num in commands:
    if num > 0:
        counter += 1
print(counter)

# B PART 
counter = 0
commands = text.split('\n')
commands = [int(j) + int(i) + int(k) for i,j,k in zip(commands, commands[1:], commands[2:])]
for num1, num2 in zip(commands,commands[1:]):
    if num2 > num1:
        counter += 1

print(counter)