# A PART
with open("03.txt") as f:
    text = f.read()
commands = text.split('\n')
#print(commands)
sez = [0 for i in commands[0]]
for command in commands:
    for i, bit in enumerate(command):
        if bit == '1':
            sez[i] += 1
        else:
            sez[i] -= 1
gamma = 0
epsilon = 0
for i, count in enumerate(reversed(sez)):
    if count > 0:
        gamma += 2**i
    else:
        epsilon += 2**i 
print(gamma*epsilon)
# B PART 
#commands = [[a for a in command] for command in commands]

#print(commands)
def rekurzivno(komande, niz):
    if len(komande) == 1:
        gamma = 0
        for i, a in enumerate(reversed(niz+komande[0])):
            gamma += int(a)*2**i
        return gamma
    else:
        nove_komande = []
        count = 0
        for i, komanda in enumerate(komande):
            if komanda[0] == '1':
                count += 1
            else:
                count -= 1
        if count > -1:
            for komanda in komande:
                if komanda[0] == '1':
                    nove_komande.append(komanda[1:])
            return rekurzivno(nove_komande, niz + '1')
        else:
            for komanda in komande:
                if komanda[0] == '0':
                    nove_komande.append(komanda[1:])
            return rekurzivno(nove_komande, niz + '0')
        
def rekurzivno2(komande, niz):
    if len(komande) == 1:
        gamma = 0
        for i, a in enumerate(reversed(niz+komande[0])):
            gamma += int(a)*2**i
        return gamma
    else:
        nove_komande = []
        count = 0
        for i, komanda in enumerate(komande):
            if komanda[0] == '1':
                count += 1
            else:
                count -= 1
        if count >= 0:
            for komanda in komande:
                if komanda[0] == '0':
                    nove_komande.append(komanda[1:])
            return rekurzivno2(nove_komande, niz + '0')
        else:
            for komanda in komande:
                if komanda[0] == '1':
                    nove_komande.append(komanda[1:])
            return rekurzivno2(nove_komande, niz + '1')
print(rekurzivno(commands,'')*rekurzivno2(commands,''))