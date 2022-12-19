import re

data = open('day5.txt').read()
_ ,instructions = data.split('\n\n')
stacks = ['WTHPJCF','HBJZFVRG','RTPH','THPNSZ',
          'DCJHZFVN','ZDWFGMP','PDJSWZVM','SDN','MFSZD']
stacks = [list(s) for s in stacks]

inst = re.findall('move (\d+) from (\d+) to (\d+)',instructions)
inst = [map(int,x) for x in inst]

for move,from_stack,to_stack in inst:
    f = stacks[from_stack-1]
    moving = [f.pop(0) for _ in range(move)]
    ## part 2 don't reverse 'moving'
    stacks[to_stack-1] = moving[::-1] + stacks[to_stack-1]

print("".join(c[0] for c in stacks))
