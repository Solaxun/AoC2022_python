from itertools import cycle

SHAPES = ['_','+','J','I','O']
JETS = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
JETS = open('day17.txt').read()
SHAPES = {
    '_':((0,2),(0,3),(0,4),(0,5)),
    '+':((1,2),(1,3),(1,4),(0,3),(2,3)),
    'J':((2,2),(2,3),(2,4),(1,4),(0,4)),
    'I':((0,2),(1,2),(2,2),(3,2)),
    'O':((0,2),(0,3),(1,2),(1,3))
}
SHAPES_ORDER = cycle(SHAPES)
JETS_ORDER =   cycle(JETS)

def oob(piece):
    return any(c < 0 or c >= 7 for r,c in piece)
    
def collides(piece):
    return any((x,y) in locked_coords for x,y in piece) or oob(piece)
    
def move_piece(piece_coords,dir):
    moves = {'>':(0,1),'<':(0,-1),'v':(1,0)}
    return tuple(tuple(x+y for x,y in zip(pc,moves[dir])) for pc in piece_coords)

def next_piece():
    return SHAPES[next(SHAPES_ORDER)]

def jet_move(piece):
    dir = next(JETS_ORDER)
    new_piece = move_piece(piece,dir)  
    if not collides(new_piece):
        return new_piece    
    return piece

def down_move(piece):
    new_piece = move_piece(piece,'v')
    if collides(new_piece) or touches_floor(new_piece):
        return piece,True # couldn't move down, lock the piece and respawn
    return new_piece,False

def touches_floor(piece):
    return any(r >= floor for r,c in piece)

def adjust_spawn_four_above_top(piece,highest):
    """Adjust piece coords such that the lowest 'x' in piece is 4 above the
    highest point so far. For example:
    
    adjust_spawn_four_above_top([(0,2),(0,3),(1,2),(1,3)], -2)
    >>((-7, 2),(-7, 3),(-6, 2),(-6, 3))"""
    spawn_row = highest - 4 
    lowest_piece_point = max(x for x,y in piece)
    move_up = spawn_row - lowest_piece_point
    return tuple((x + move_up,y) for x,y in piece)

def spawn_piece():
    piece = next_piece()
    return adjust_spawn_four_above_top(piece,highest)

def tower_height(points):
    # plus 1 because height is inclusive, e.g. 0 to 10 is 11 points
    return max(x for x,y in points) - min(x for x,y in points) + 1

locked_coords = set()
floor = highest = 4
piece = spawn_piece()
rocks = 0
i = 0

def rock_to_cycles(r):
    return (r+3)/1725
    
def cycle_to_height(c):
    return 2694*c - 9*(c-1)

# for part 2 change 2022 to large number e.g. 1Million to observe 
# cycle/rocks relation, which ends up as the formula above for my input
# (will be diff for other inputs since JETS will differ)
while rocks < 2022:
    piece = jet_move(piece)
    piece,is_locked = down_move(piece)
    if is_locked:
        locked_coords.update(piece)
        highest = min(highest,*(x for x,y in piece))
        rocks += 1
        piece = spawn_piece()
    i += 1
    # if rocks % 10_000 == 0 and rocks > 0:        
    #     print(f'rocks: {rocks} height: {tower_height(locked_coords)} iter: {i}')
    if i % len(JETS) == 0:        
        print(f'rocks: {rocks} height: {tower_height(locked_coords)} cycles: {i/len(JETS)} est height: {cycle_to_height(rock_to_cycles(rocks))}')

print(tower_height(locked_coords))
# rocks = cycles * 1722 + 3 * (cycles-1) by observing the above printouts
# but how many cycles to get to 1TRN rocks? Algebra.
# solving the above for cycles yields: cycles = (r + 3) / 1725

# but then need either rocks->height or cycles->height:
# again by observing the printout above we can see the following relation:
# height = 2,694 * ncycles - 9 * (ncycles - 1)

# formula works for complete cycles, but not discrete
# what if we are at 10.128 cycles?
"""
cycles after 1TN rocks = 579710144.9292754
full cycles = 579710144
partial cycle = .9292754

so cycles between 579710144 and 579710145, which yields a height b/w
1556521736649 to 1556521739334 using those cycle ranges

using the continuous cycle output the formula actually produces of
579710144.9292754 results in a height of 1556521739144.1045.  

I just kept guessing lower values until 1556521739139 since I knew that
we were only 92.92754% the way through the final cycle when we hit 1T
rocks, meaning there was probably only a few rocks diff at most."""