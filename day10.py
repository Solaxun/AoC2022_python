## this was an exercise in OBO bug-hunting.
instructions = open('day10.txt').read().splitlines()

x,cycle_amounts = 1,[1]
while instructions:
    op,*arg = instructions.pop(0).split()
    if op == 'addx':
        arg = int(arg[0])
        cycle_amounts.extend([x,x+arg])
        x += arg
    else:
        cycle_amounts.append(x)

## part 1
signal_strength = 0
for i in range(19,len(cycle_amounts),40):
    signal_strength += (i+1) * cycle_amounts[i]
print(signal_strength)

## part 2
crt = [list('.'*40) for i in range(6)]
pixel_center = 1
for cycle,xreg in enumerate(cycle_amounts):
    pixel_center = xreg
    pixels = [pixel_center + j for j in range(-1,2)]
    print(cycle,xreg,pixels)
    if cycle % 40 in pixels:
        row = cycle // 40
        col = cycle % 40
        crt[row][col] = '#'
    
for row in crt:
    print("".join(row))