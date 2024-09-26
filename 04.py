# A PART
with open("04.txt") as f:
    text = f.read()
commands = text.split('\n')

numbers = [int(i) for i in commands[0].split(',')]
bingo_cards, bingo_card = [], []
for command in commands[2:]:
    if command == '':
        bingo_cards.append(bingo_card)
        bingo_card = []
    else:
        bingo_card.append([int(i) for i in command.split()])
bingo_cards.append(bingo_card)

def is_bingo(bingo_card):
    for i, row in enumerate(bingo_card):
        if row == [-1 for _ in range(5)]:
            return True
        if [bingo_card[j][i] for j in range(5)] == [-1 for _ in range(5)]:
            return True
    return False
def mark_number(number, bingo_card):
    for i, row in enumerate(bingo_card):
        for j, k in enumerate(row):
            if k == number:
                bingo_card[i][j] = -1
    return bingo_card
aa = True
for num in numbers:
    for i, bingo_card in enumerate(bingo_cards):
        bingo_cards[i] = mark_number(num, bingo_card)
       
        if is_bingo(bingo_cards[i]):
            a = bingo_cards[i]
            break
    else:
        continue
    break
my_sum = 0
for b in a:
    for c in b:
        if c !=-1:
            my_sum += c
print(my_sum*num)
        
# B PART 
bingo_cards, bingo_card = [], []
for command in commands[2:]:
    if command == '':
        bingo_cards.append(bingo_card)
        bingo_card = []
    else:
        bingo_card.append([int(i) for i in command.split()])
bingo_cards.append(bingo_card)
aaaa = [False for _ in range(len(bingo_cards))]
ind=0
for num in numbers:
    for i, bingo_card in enumerate(bingo_cards):
        bingo_cards[i] = mark_number(num, bingo_card)
       
        if is_bingo(bingo_cards[i]) and False in aaaa:
            aaaa[i] = True
            
            ind=i
    if False not in aaaa:
        a = bingo_cards[ind]
        break
my_sum = 0
for b in a:
    for c in b:
        if c !=-1:
            my_sum += c
print(my_sum*num)