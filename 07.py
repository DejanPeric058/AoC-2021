# A PART
with open("07.txt") as f:
    text = f.read()
commands = [int(i) for i in text.split(',')]
commands.sort()
median = commands[len(commands)//2]
print(sum([abs(i - median) for i in commands]))
# B PART 
avg = round(sum(commands)/len(commands))
avg -= 1
print(sum([abs(i - avg)*(abs(i - avg)+1)/2 for i in commands]))