# A PART
with open("06.txt") as f:
    text = f.read()
commands = text.split(',')
fishes = [int(a) for a in commands]

for x in range(80):
    new_fishes = []
    for i, fish in enumerate(fishes):
        if fish == 0:
            fishes[i] = 6
            new_fishes.append(8)
        else:
            fishes[i] -= 1
    fishes = fishes + new_fishes
print(len(fishes))

# B PART 
# (0), 
fishes = [int(a) for a in commands]
my_dict = { i:0 for i in range(9)}
for a in fishes:
    my_dict[a] += 1
for _ in range(256):
    sez = []
    for i in range(8):
        sez.append(my_dict[i+1])
    novi = my_dict[0]
    for i in range(8):
        my_dict[i] = sez[i]
    my_dict[6] += novi
    my_dict[8] = novi
print(sum(my_dict.values()))
