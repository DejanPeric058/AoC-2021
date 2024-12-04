# A PART
import re
with open("14.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
start_molecule = commands[0]
joining_rules = commands[2:]
print(joining_rules)
atoms_count = {}
for a in start_molecule:
    atoms_count[a] = 0



class JoiningRule:
    def __init__(self, command):
        global atoms_count
        self.pattern = command[0:2]
        self.insert = command[-1]
        self.new_pattern = self.pattern[0] + self.insert + self.pattern[1]
        self.new1 = self.pattern[0] + self.insert
        self.new2 = self.insert + self.pattern[1]
        atoms_count[self.insert] = 0

    def in_molecule(self, molecule):
        return self.pattern in molecule
    
    def positions_of_pattern(self, molecule):
        return [m.start() for m in re.finditer('(?='+self.pattern+')', molecule)]
    # [m.start() for m in re.finditer(self.pattern, molecule)]

    def add_rule(self, molecule):
        global rule_dict
        positions = self.positions_of_pattern(molecule)
        for p in positions:
            rule_dict.append((p+1, self.insert))
joining_rules2 = []
for rule in joining_rules:
    joining_rules2.append(JoiningRule(rule))
atoms_count2 = atoms_count.copy()
for _ in range(10):
    rule_dict = []
    for rule in joining_rules2:
        rule.add_rule(start_molecule)
    rule_dict.sort(key=lambda x: x[0], reverse=True)
    for i, (p,new) in enumerate(rule_dict):
        start_molecule = start_molecule[:p] + new + start_molecule[p:]
    #print(start_molecule)
    #print(len(start_molecule))
    #print(rule_dict)

#print(len(start_molecule))
#NBCCNBBBCBHCB
#NBBBCNCCNBBNBNBBCHBHHBCHB
#NBBBCNCCNBBNBBBCHBHHBCHB
#NBBBCNCCNBBNBNBBCHBHHBCHB

#NBNBBCHBHHBCHB
#NBBBCHBHHBCHB
for atom in atoms_count.keys():
    atoms_count[atom] = start_molecule.count(atom)

print(max(atoms_count.values())-min(atoms_count.values()))
# B PART 
start_molecule = commands[0]
my_dict = {}
for rule in joining_rules2:
    my_dict[rule.pattern] = 0
clean_dict = my_dict.copy()
for i in range(len(start_molecule)-1):
    my_dict[start_molecule[i:i+2]] += 1
for _ in range(40):
    temp_dict = clean_dict.copy()
    for rule in joining_rules2:
        temp_dict[rule.new1] += my_dict[rule.pattern]
        temp_dict[rule.new2] += my_dict[rule.pattern]
    #for rule in temp_dict.keys():
    my_dict = temp_dict

print(sum(my_dict.values()))
for a, b in my_dict.items():
    atoms_count2[a[0]] += b
atoms_count2[start_molecule[-1]] += 1
print(max(atoms_count2.values())-min(atoms_count2.values()))