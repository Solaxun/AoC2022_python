ROCKS = open('day14.txt').read()
POINTS = set()
START = (500,0)

def connect_points(from_coord,to_coord):
    (x1,y1),(x2,y2) = from_coord,to_coord
    pts = []
    for x in range(min([x1,x2]),max([x1,x2]) +1):
         for y in range(min([y1,y2]),max([y1,y2]) +1):
             pts.append((x,y))
    return pts
        
for rockline in ROCKS.splitlines():
    segments = [list(map(int,s.split(',')))
                for s in rockline.split(' -> ')]
    lines = [segments[i:i+2] for i in range(0,len(segments)-1)]
    for coord1,coord2 in lines:
        line = connect_points(coord1,coord2)
        POINTS.update(line)
        
def move(pt1,dir):
    return tuple([p+d for p,d in zip(pt1,dir)])

def not_collide(curpos,sand,floor,part=1):
    available = curpos not in sand and curpos not in POINTS
    return available and curpos[1] < floor if part == 2 else available
    
def next_move(pos,sand,floor,part=1):
    moves = [(0,1),(-1,1),(1,1)] 
    return next(filter(lambda x: not_collide(x,sand,floor,part),
                       [move(pos,d) for d in moves]),
                None)   

def simulate(rocks=POINTS,start=START,floor=max(y for x,y in POINTS),part=1):
    def below_floor(pos,floor): return pos[1] >= floor
    sand = set()
    i = 0
    while True:
        cur_pos = START            
        while cur_pos:
            prev_pos = cur_pos
            cur_pos = next_move(cur_pos,sand,floor,part)
            if below_floor(prev_pos,floor): # sand fell below lowest rock
                return len(sand)        
        if prev_pos == START: # filled to the top
            return len(sand)
        sand.add(prev_pos)

p1_floor = max(y for x,y in POINTS)
p2_floor = p1_floor + 2

## part 1 takes a few seconds, part 2 takes ~45 seconds (ouch)
## maybe optimize later.
p1 = simulate(rocks=POINTS,start=START,floor=p1_floor,part=1)
print(p1)
p2 = simulate(rocks=POINTS,start=START,floor=p2_floor,part=2)
print(p2+1) # +1 for final piece of sand at the origin