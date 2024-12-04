# A PART
with open("08.txt") as f:
    text = f.read()
commands = text.split('\n')
inputs = [a.split(' | ')[0] for a in commands]
outputs = [a.split(' | ')[1] for a in commands]
counter = 0
for output in outputs:
    for a in output.split():
        if len(a) in [2,3,4,7]:
            counter += 1
print(counter)
# B PART 

def ustvari_prevajalnik(sez):
    sez.sort(key=len)
    for i, a in enumerate(sez):
        sez[i] = ''.join(sorted(a))
    ena = sez[0]
    sedem = sez[1]
    stiri = sez[2]
    osem = sez[-1]
    preostali1, preostali2 = sez[3:6], sez[6:9]
    preverit_za_5 = stiri.replace(ena[0], '').replace(ena[1], '')
    for a in preostali1:
        if ena[0] in a and ena[1] in a:
            tri = a
        elif preverit_za_5[0] in a and preverit_za_5[1] in a:
            pet = a
        else:
            dva = a
    for a in preostali2:
        if ena[0] not in a or ena[1] not in a:
            sest = a
        elif preverit_za_5[0] in a and preverit_za_5[1] in a:
            devet = a
        else:
            nic = a
    my_dict = {
        ena : 1,
        sedem : 7,
        stiri : 4,
        osem : 8, 
        tri : 3,
        pet : 5,
        dva : 2,
        sest : 6,
        devet : 9,
        nic : 0
    }
    return my_dict

def vrni_stevilko(sez1, sez2):
    stevilka = 0
    prevajalnik = ustvari_prevajalnik(sez1)
    for a in sez2:
        stevilka = stevilka * 10 + prevajalnik[''.join(sorted(a))]
    return stevilka

inputs = [[b for b in a.split(' | ')[0].split()] for a in commands]
outputs = [[b for b in a.split(' | ')[1].split()] for a in commands]
my_sum = 0
for sez1, sez2 in zip(inputs, outputs):
    my_sum += vrni_stevilko(sez1, sez2)

print(my_sum)