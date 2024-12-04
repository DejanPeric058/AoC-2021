# A PART
with open("09.txt") as f:
    text = f.read()
commands = text.split('\n')
caves = [[9 for i in range(len(commands[0])+2)]]
caves += [[9] + [int(i) for i in command] + [9] for command in commands]
caves += [[9 for i in range(len(commands[0])+2)]]
my_sum = 0
counter = 0
low_points = []
for i in range(1,len(commands)+1):
    for j in range(1,len(commands[0])+1):
        current = caves[i][j]
        up = caves[i-1][j]
        down = caves[i+1][j]
        left = caves[i][j-1]
        right = caves[i][j+1]
        if current < up and current < down and current < left and current < right:
            my_sum += 1 + current
            counter += 1
            low_points.append((i,j))
print(my_sum, counter)
# B PART 

def size_of_basin(i,j):
    
    current = caves[i][j]
    
    if current == 9:
        return -1
    else:
        #print(i,j)
        up = caves[i-1][j]
        down = caves[i+1][j]
        left = caves[i][j-1]
        right = caves[i][j+1]
        caves[i][j] = 9
        if up > current and down > current and left > current and right > current:
            return 4 + size_of_basin(i+1,j) + size_of_basin(i-1,j) + size_of_basin(i,j+1) + size_of_basin(i,j-1)
        elif up > current and down > current and left > current:
            return 3 + size_of_basin(i+1,j) + size_of_basin(i-1,j) + size_of_basin(i,j-1)
        elif up > current and down > current and right > current:
            return 3 + size_of_basin(i+1,j) + size_of_basin(i-1,j) + size_of_basin(i,j+1)
        elif up > current and right > current and left > current:
            return 3 + size_of_basin(i,j+1) + size_of_basin(i-1,j) + size_of_basin(i,j-1)
        elif right > current and down > current and left > current:
            return 3 + size_of_basin(i+1,j) + size_of_basin(i,j+1) + size_of_basin(i,j-1)
        elif right > current and left > current:
            return 2 + size_of_basin(i,j+1) + size_of_basin(i,j-1)
        elif right > current and down > current:
            return 2 + size_of_basin(i,j+1) + size_of_basin(i+1,j)
        elif right > current and up > current:
            return 2 + size_of_basin(i,j+1) + size_of_basin(i-1,j)
        elif up > current and left > current:
            return 2 + size_of_basin(i-1,j) + size_of_basin(i,j-1)
        elif down > current and left > current:
            return 2 + size_of_basin(i+1,j) + size_of_basin(i,j-1)
        elif down > current and up > current:
            return 2 + size_of_basin(i+1,j) + size_of_basin(i-1,j)
        elif right > current:
            return 1 + size_of_basin(i,j+1)
        elif left > current:
            return 1 + size_of_basin(i,j-1)
        elif up > current:
            return 1 + size_of_basin(i-1,j)
        elif down > current:
            return 1 + size_of_basin(i+1,j)
        else:
            return 0
    

basins_sizes = [size_of_basin(i,j) + 1 for i, j in low_points]
basins_sizes.sort(reverse=True)
print(basins_sizes[0]*basins_sizes[1]*basins_sizes[2])